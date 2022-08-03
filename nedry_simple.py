##########  import modules  ##########
from IPython.display import Image
from IPython.display import display
from pygame import mixer
import time
##########  create function  ##########
def jp_protocol():
    jp_string = "Jurassic Park, System Security Interface\nVersion 4.0.5, Alpha E\nReady..."
    gif = Image("nedry.gif")
    print(jp_string)
    def request_access():
        request_number = 1
        while (request_number < 3):
            print("> " + input())
            time.sleep(0.7)
            print("access: PERMISSION DENIED")
            request_number += 1
        print("> " + input())
        time.sleep(0.7)
        print("access: PERMISSION DENIED.", end = "")
        time.sleep(1)
        print("...and....")
        time.sleep(1)
        ah_ah_ah()
    def text_func():
        mock = 1
        while (mock <= 15):
            print("YOU DIDN'T SAY THE MAGIC WORD!")
            time.sleep(0.1)
            mock += 1
    def audio_func():
        mixer.init()
        mixer.music.load("Nedry_AhAhAh.mp3")
        mixer.music.play()
    def ah_ah_ah():
        text_func()
        display(gif)
        time.sleep(0.2)
        audio_func()
    request_access()
##########  run function  ##########
jp_protocol()