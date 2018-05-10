from ezmatrix import *
from animation import *
from modules import *

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import time
import json
import threading

endpoint = 'avhmfui1t673z.iot.us-west-2.amazonaws.com'
root_ca_path = '/home/pi/Desktop/aws/root-CA.crt'
certificate_path = '/home/pi/Desktop/aws/RaspPi.cert.pem'
private_key_path = '/home/pi/Desktop/aws/RaspPi.private.key'

topic = 'rpi/desktopbuddy'
response = 'rpi/desktopbuddy/logs'

matrix = EzMatrix()

class ClockAttributes(object):
    def __init__(self, json):
        self.unit = json['unit']
        self.zip_code = json['zip_code']
        self.region = json['region']
        
        try:
            temp_color_json = json['temp_color']
            self.temp_color = Color(temp_color_json['r'], temp_color_json['g'], temp_color_json['b'])
        except KeyError:
            self.temp_color = Color.green()
            
        try:
            day_color_json = json['day_color']
            self.day_color = Color(day_color_json['r'], day_color_json['g'], day_color_json['b'])
        except KeyError:
            self.day_color = Color.white()
        
        try:
            date_color_json = json['date_color']
            self.date_color = Color(date_color_json['r'], date_color_json['g'], date_color_json['b'])
        except KeyError:
            self.date_color = Color.gray()
        
        try:
            hour_color_json = json['hour_color']
            self.hour_color = Color(hour_color_json['r'], hour_color_json['g'], hour_color_json['b'])
        except KeyError:
            self.hour_color = Color.red()
            
        try:
            minute_color_json = json['minute_color']
            self.minute_color = Color(minute_color_json['r'], minute_color_json['g'], minute_color_json['b'])
        except KeyError:
            self.minute_color = Color.blue()
            
class AnimationThread(threading.Thread):
    def __init__(self, anim=None):
        super(AnimationThread, self).__init__()
        self.should_stop = False
        self.anim = anim
        
    def run(self):
        while not self.should_stop:
            matrix.run_anim(self.anim)
            
class CanvasThread(threading.Thread):
    def __init__(self, canvas):
        super(CanvasThread, self).__init__()
        self.should_stop = False
        self.canvas = canvas
        
    def run(self):
        while not self.should_stop:
            matrix.draw_canvas(self.canvas)
            
class ClockThread(threading.Thread):
    def __init__(self, ref_rate, unit, zip_code, region, temp_color, day_color, date_color, hour_color, minute_color):
        super(ClockThread, self).__init__()
        self.should_stop = False
        self.ref_rate = ref_rate * 60 # convert ref_rate from minutes to seconds
        self.unit = unit
        self.zip_code = zip_code
        self.region = region
        self.temp_color = temp_color
        self.day_color = day_color
        self.date_color = date_color
        self.hour_color = hour_color
        self.minute_color = minute_color
        
    def run(self):
        temp_cvs = Module.temperature_canvas(self.unit, self.zip_code, self.temp_color)
        
        tme = int(time.time())
        
        while not self.should_stop:
            if int(time.time()) - tme == self.ref_rate:
                temp_cvs = Module.temperature_canvas(self.unit, self.zip_code, self.temp_color)
                tme = int(time.time())
                
            time_cvs = Canvas(25, 19).add_subcanvas(
                Module.time_canvas(
                    self.region,
                    self.day_color,
                    self.date_color,
                    self.hour_color,
                    self.hour_color,
                    self.minute_color), Point(0, 6))
            
            time_cvs.add_subcanvas(temp_cvs, Point(9, 0))
            
            matrix.draw_canvas(Canvas().add_subcanvas(time_cvs, Point(3, 6)))

class CallbackContainer(object):
    def __init__(self, client):
        self._client = client
        self.thread = AnimationThread()
        
    def interpritMessage(self, client, userdata, message):
        try:
            msg = json.loads(message.payload)['message']
        except ValueError:
            print('MISSING DELIMITER IN JSON')
            return
        
        if 'args' in message.payload:
            try:
                args = json.loads(message.payload)['args']
            except ValueError:
                print('MISSING DELIMITER IN JSON')
        else:
            args = ''
        
        print('Message received: \"{}\" from topic {}'.format(msg, message.topic))
        
        if self.thread.isAlive():
            print('JOINING THREAD')
            self.thread.should_stop = True
            self.thread.join()

        if 'clock' in msg:
            clock_attrs = ClockAttributes(args)
            
            self.thread = ClockThread(
                3,
                clock_attrs.unit,
                clock_attrs.zip_code,
                clock_attrs.region,
                clock_attrs.temp_color,
                clock_attrs.day_color,
                clock_attrs.date_color,
                clock_attrs.hour_color,
                clock_attrs.minute_color)
            
            self.thread.should_stop = False
            self.thread.start()
        if 'image' in msg:
            cvs = Module.image_canvas_from_url(args)
            
            if cvs.has_data():
                self.send_message(True, 'successfully downloaded image')
            else:
                self.send_message(False, 'failed to download image')
            
            self.thread = CanvasThread(cvs)
            self.thread.start()
                
        if 'gif' in msg:
            args = './gifs/' + args + '.gif'
            
            anim = Module.gif_anim(args)
            
            if len(anim) > 1:
                self.send_message(True, 'successfully compiled gif')
            else:
                self.send_message(False, 'failed to compile gif')
            
            self.thread = AnimationThread(anim)
            self.thread.should_stop = False
            self.thread.start()
            
    def send_message(self, is_success, message):
        message = json.dumps({'did_succeed': is_success,
                              'message': message})
        print('Sending message to {}:\n'.format(response) + str(message))
        self._client.publishAsync(response, message, 1)

if __name__ == "__main__":
    print('STARTING...')
    client = AWSIoTMQTTClient('desktopBuddy')
    # the argument in above line is the clientID, if left empty it will be randomly generated by AWS
    client.configureEndpoint(endpoint, 8883)
    client.configureCredentials(root_ca_path, private_key_path, certificate_path)

    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureOfflinePublishQueueing(-1)
    client.configureDrainingFrequency(2)
    client.configureConnectDisconnectTimeout(10)
    client.configureMQTTOperationTimeout(5)

    myCallbackContainer = CallbackContainer(client)

    client.connect()

    client.subscribe(topic, 1, myCallbackContainer.interpritMessage)
    print('STARTED SERVICE')

    while True:
        time.sleep(3)