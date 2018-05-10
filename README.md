# Desktop Buddy
Desktop Buddy is an open-source platform for displaying custom modules on a 32x32 LED matrix running on a Raspberry Pi.

![DesktopBuddy](https://media.giphy.com/media/YByM148NfvTamH6tA7/giphy.gif)

> __This is not a finished project. Please reach out to me if you have any questions about setup.__

## Getting Started
### Prerequisites
Things you will need to get started:
* Raspberry Pi with Wi-Fi
* 32 x 32 LED Matrix
    * I'm using [this model from Adafruit](https://www.adafruit.com/product/607)
* [Adafruit RGB Matrix HAT + RTC for Raspberry Pi](https://www.adafruit.com/product/2345) or equivalent
* Amazon Web Services account

### Setup and Installation
* Follow [these steps](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi) to get your matrix up and running if you're using the Adafruit Matrix HAT listed above.
* Clone this repository to your Raspberry Pi
    * `git clone https://github.com/oct0f1sh/DesktopBuddy`
* Set up a new AWS IoT Thing, download the certificates, and edit the paths of the `endpoint`, `root_ca_path`, `certificate_path`, and `private_key_path` strings in `aws_service.py` to your new values.

## Running the Service
Navigate to the directory that you cloned the project and run the `aws_service.py` file.

## Author
oct0f1sh, duncan@duncanmacdonald.us