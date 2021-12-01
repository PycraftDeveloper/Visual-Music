# Visual-Music
This is a short program that takes the input from your microphone and uses OpenGL to draw a live colourful pattern

## Installation and Setup
This project will not have any documentation written up for on http://readthedocs.io, all the information you need should be here; if you encounter any issues of cource feel free to email me at: thomasjebbo@gmail.com or message me on Twitter: https://twitter.com/PycraftDev.

Assuming you have already installed Python, you can install the project by:
1. Open terminal or command prompt (Depending on you're OS).
2. type in the following commands:
```
pip install moderngl
pip install moderngl-window
pip install sounddevice
pip install numpy
```
3. Once those files have downloaded and installed, download the files or the project from here.
4. Then take the downloaded zip file and extract it.
5. Then navigate to the file labeled main.py
6. Double click the file to try and run it, if it works first time then you should see some graphics on screen. If you do not see any on-screen effects, make sure the program is still running and not crashed, and try to play some music. If that does not work then feel free to contact me, after trying the steps below (v).
7. If the program closes with an error allong the lines of: "Error querying device", then make sure you have an audio input device and its enabled. If you do not own a microphone or want cleaner audio, then things get a bit more complex:
8. [for devices running windows 7 or newer] Open the 'Change System Sounds' menu (it should come up in windows search), then navigate to the recording tab. If your device supports it then you will see a device called "line-in", if you have this device then enable it (and plug an audio lead from your speakers or source device into an audio port that supports microphones) and try running the program again, it should work for you this time.

## Final Notices

There isn't much else left to say, but I hope you enjoy using the project, feel free to share the project or use any aspect of this in your own work; this project is based off py previous work with audio maniplulation in Python, and the work of the folks over at modernGL here: https://github.com/moderngl/moderngl.

Also for those interested in privacy. this project in no way saves or distributes any information from the microphone. Thank you for reading and enjoy!
