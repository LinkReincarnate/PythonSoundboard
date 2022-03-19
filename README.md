## What's this project all about?
Simple Soundboard uses pygame to read usb game controller input and play sounds. Up to 40 buttons are supported across 4 controllers.

## How to install and use
#### Basic install
Installing it should be quite easy. (As long as you dont plan on using the sub-sampling buttons which I had no luck of getting to work on the PI)
Just follow these steps:
1. (Optional) Use a virtualenv
2. Run `pip install -r requirements.txt` - This is going to install all the required packages
3. Make sure you have all the joysticks connected - right now you have to have 4 joysticks to be able to use all the sound effects
4. Run `main.py` - A window should pop-up
5. Now, pressing the buttons 0 to 9 on your Joystick should do something (Most likely play a sound) (See `sound_buttons` in main.py for the button mapping)

If it still doesn't work, please feel free to open an issue, and I'll try to help you out ASAP.

#### Setup required for the sub-sampling button
Now, there's a sub-sampling feature as well, but I couldn't get it to work on the RPI. It requires the usage of PAVUControl to loop-back the desktop audio to an input device which is then captured by the script (See `utility/AudioRecorder.py`).
To setup this loopback, you will have to install PAVUControl and Audacity, this can be done using the `sudo apt-get install PAVUControl` and `sudo apt-get install Audacity` commands.
Once you have both up and running, do the following:
1. Open AudaCity, and start recording
2. Open PAVUControl, and go to the "Recording" tab
3. Audacity should be listed there - Click on "Port" and select whichever port whose name starts wiht "Monitor of"
4. (Optional) Test if the audio is looped back properly. This can be done by playing some audio (YouTube, or just a simple audio file), and check if AudaCity has recorded the same.

Now, this was the easy part... For whatever reason I'm getting errors regarding ALSA when I try to use the recording button. On Linux Mint (on a PC) it works perfectly. If anyone has a solution, please open an issue explaining the solution/PR. **Thank you**.

## Adding new/modifying existing assets/buttons/joys
... is quite simple. In `main.py` there's an array called `sound_buttons`, in there you can add new buttons, modify existing ones, etc...
If you add a new asset (sound that is) and want to use it, you can either add a new `SoundButton` or replace an existing one.
