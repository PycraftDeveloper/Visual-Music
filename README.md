# Visual-Music
This is a short program that takes the input from your microphone and uses OpenGL to draw a live colourful pattern

## Installation and Setup
This project will not have any documentation written up for on http://readthedocs.io, all the information you need should be here; if you encounter any issues of course feel free to email me at: thomasjebbo@gmail.com or message me on Twitter: https://twitter.com/PycraftDev.

Assuming you have already installed Python, you can install the project by:
1. Open terminal or command prompt (Depending on your OS).
2. type in the following commands:
```
pip install moderngl
pip install moderngl-window
pip install sounddevice
pip install numpy
```
3. Once those files have downloaded and installed, download the files or the project from here.
4. Then take the downloaded zip file and extract it.
5. Then navigate to the file labelled main.py
6. Double click the file to try and run it, if it works first time then you should see some graphics on screen. If you do not see any on-screen effects, make sure the program is still running and not crashed, and try to play some music. If that does not work then feel free to contact me, after trying the steps below (v).
7. If the program closes with an error along the lines of: "Error querying device", then make sure you have an audio input device and its enabled. If you do not own a microphone or want cleaner audio, then things get a bit more complex:
8. [for devices running windows 7 or newer] Open the 'Change System Sounds' menu (it should come up in windows search), then navigate to the recording tab. If your device supports it then you will see a device called "line-in", if you have this device then enable it (and plug an audio lead from your speakers or source device into an audio port that supports microphones) and try running the program again, it should work for you this time.

## Running the project

Running the project is very self-explanatory after setup, double click the Python file to run, then load up some audio (Spotify, YouTube, Soundcloud, ext.) and you will begin to see a pattern appear to the song as its displayed visually. This project very detailed, and if the volume of the song increases then the display zooms out so you can see all the details, ever you go from a really loud song to a quieter one, just press space and it re-sets your view!

## Change-log

This update features many changes, and many bug-fixes, here are all the notable features listed below.

* Bug Fix - Fixed the issue when closing the game in fullscreen and it closing but leaving the blank, unresponsive fullscreen window.
* Feature - Changed aspect ratio for easier mathmatics and calculations.
* Feature - All of the new visuals (and the old ones too) now run relative to the maximum volume, so pressing 'SPACE' is now more relevant than ever, but does create a more accurate effect.
* Feature - The outer 4 pulses move to sounds louder than 3/4 of the loudest sound. These should pulse to the beat of the song.
* Feature - The inner pulse is designed to pulse when the sound is louder than 1/4 of the maximum volume, but less than 7/8 of the maximum sound, to make the centre more interesting during louder pieces.
* Feature - The pulses on the (x,y) axis move with the sound, but if the sound is quieter than 1/4 of the maximum volume, then we move to the new diagonal audio tracks, which are used in quieter parts of the sound.

This update was released on 26/12/2021 (DD/MM/YYYY)

### Key binds:

- SPACE: Re-sets your view
- F11: Toggles full-screen
- ESC: Closes the window (although be aware that at present make sure to NOT be in full screen when doing this as it can cause issues)

###Final Notices

There isn't much else left to say, but I hope you enjoy using the project, feel free to share the project or use any aspect of this in your own work; this project is based off my previous work with audio manipulation in Python, and the work of the folks over at moderngl here: https://github.com/moderngl/moderngl.

Also, for those interested in privacy. this project in no way saves or distributes any information from the microphone. Thank you for reading and enjoy!

## Examples
