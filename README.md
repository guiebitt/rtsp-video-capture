# RTSP Video Capture

## Requirements

- Python >= 3
- [Open CV](https://pypi.org/project/opencv-python/) `pip install opencv-python`
    > Opensource library that allows the manipulation of visual resources that we will use to access the camera's video.
- [Dot Env](https://pypi.org/project/python-dotenv/) `pip install python-dotenv`
    > Allows the definition of environment variables using an .env file. Use this file to store variables that will contain username, password and IP of the camera to be accessed.

## Usage

### Clone this repository

Make a copy of the repository to run the program that will allow you to access the camera.

### Create .env file

Create a .env file at the root of the directory containing the following environment variables with the values ​​corresponding to the camera you want to access.

```
RTSP_USERNAME=your_username
RTSP_PASSWORD=your_password
RTSP_IP=your_camera_ip
RTSP_PORT=your_camera_port
```

Yoosee example:

```
RTSP_USERNAME=admin
RTSP_PASSWORD=Set the password in the App: More Settings > NVR Connection
RTSP_IP=Get the IP from the device information in the App
RTSP_PORT=554
```

### Run the program basic_example

The program has very simple logic:
- Gets the necessary data defined in the environment variables that are loaded through the .env file;
- Sets up the URL to access the camera that supports the RTSP protocol;
- Uses the Open CV library to capture video from the camera and present;
- It has a loop with an interval of 1 second;
- If you want to end the program, just press the "q" key;