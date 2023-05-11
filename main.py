import threading
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, LinePlot
import numpy as np
from kivy.clock import Clock

#from tools import AudioPlayer
from kivy.core.audio import SoundLoader


import time
import wave
from audiostream import get_input

frames = []

'''
def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)

# get the default audio input (mic on most cases)


mic = get_input(callback=mic_callback)
mic.start()

time.sleep(5)

mic.stop()

wf = wave.open("test.wav", 'wb')
wf.setnchannels(mic.channels)
wf.setsampwidth(2)
wf.setframerate(mic.rate)
wf.writeframes(b''.join(frames))
wf.close()




def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)
    print('size of frames: ' + len(frames))

def bcallback(instance):
    mic = get_input(callback=mic_callback, source='mic')
    mic.start()
    #mic.poll()
    time.sleep(5)
    mic.stop()

class MyApp(App):
    def build(self):
        btn1 = Button(text='Audio Record')
        btn1.bind(on_press=bcallback)
        return btn1

#if name == 'main':
if __name__=='__main__':
    MyApp().run()
'''    
    
def __init__(self, **kw):
    super().__init__(**kw)
    self.samples_per_second = 60 # variables which stores the number of audio samples recorded per second
    self.audioData = [] # creates a list to store the audio bytes recorded
    import sys
    importlib.reload(sys.modules['audiostream']) # reloads the audiostream module - thought this might solve the problem; it doesn't!!
    self.mic = get_input(callback=self.micCallback, rate=8000, source='default', buffersize=2048) # initialises the method get_input from the module 'audiostream' with the properties required to ensure the audio is recorded correctly

def micCallback(self, buffer):
    # method which is called by the method 'get_input' to store recorded audio data (each buffer of audio samples)
    self.audioData.append(buffer) # appends each buffer (chunk of audio data) to variable 'self.audioData'

def start(self):
    # method which begins the process of recording the audio data
    self.mic.start() # starts the method 'self.mic' recording audio data
    Clock.schedule_interval(self.readChunk, 1 / self.samples_per_second) # calls the method 'self.readChunk' to read and store each audio buffer (2048 samples) 60 times per second

def readChunk(self, sampleRate):
    # method which coordinates the reading and storing of the bytes from each buffer of audio data (which is a chunk of 2048 samples)
    self.mic.poll()  # calls 'get_input(callback=self.mic_callback, source='mic', buffersize=2048)' to read the byte content. This byte content is then dispatched to the callback method 'self.micCallback'

def stop(self):
    # method which terminates and saves the audio recording when the recording has been successful
    Clock.unschedule(self.readChunk) # un-schedules the Clock's rythmic execution of the 'self.readChunk' callback
    self.mic.stop() # stops recording audio
    return self.audioData    
    
messageFile_voice = SoundLoader.load("recording2.wav")
messageFile_voice.play()    
    
if __name__=='__main__':
    MyApp().run()    
    
    
    
