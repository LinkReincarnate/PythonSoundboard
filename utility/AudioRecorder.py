import sounddevice as sd
import numpy as np
import sys

# Sample rate of recorded sound
SAMPLE_RATE = 44100

# Device index, use above little script to print it all
DEV_IDX = None

recorded_data = None
recorder_stream = None

def start_record():
    global recorder_stream
    global recorded_data

    def rec_callback(indata, frames, time, status):
        global recorded_data
        if status:
            print(status, file=sys.stderr)
        recorded_data = np.append(recorded_data, indata.copy())

    recorder_stream = sd.InputStream(
        samplerate=SAMPLE_RATE, 
        device=None,
        channels=1, 
        callback=rec_callback
    )
    recorder_stream.start()
    recorded_data = np.empty(0, dtype=np.int16)

def stop_record():
    global recorder_stream
    recorder_stream.close()

player_stream = None
def start_play():
    global recorded_data
    global current_frame
    global player_stream

    if not len(recorded_data):
        return

    print(f"play, sz: {len(recorded_data)}")
    recorded_data = recorded_data.reshape(-1, 1) # gotta reshape it to be 2D


    def play_callback(outdata, frames, time, status):
        global current_frame
        global recorded_data
        if status:
            print(status)
        chunksize = min(len(recorded_data) - current_frame, frames)
        outdata[:chunksize] = recorded_data[current_frame:current_frame + chunksize]
        if len(recorded_data) <= current_frame: # Loop on end
            current_frame = 0
        #print(current_frame)
        if chunksize < frames:
            outdata[chunksize:] = 0
            #raise sd.CallbackStop()
        current_frame += chunksize
    #sd.play()    
    
    current_frame = 0
    player_stream = sd.OutputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        callback=play_callback
    )
    player_stream.start()

def stop_play():
    global player_stream
    player_stream.close()
