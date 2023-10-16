import time
import usb_hid
from adafruit_hid import keyboard
import board
import digitalio

btn_H = digitalio.DigitalInOut(board.GP10)
btn_H.direction = digitalio.Direction.INPUT
btn_H.pull = digitalio.Pull.UP

btn_G = digitalio.DigitalInOut(board.GP11)
btn_G.direction = digitalio.Direction.INPUT
btn_G.pull = digitalio.Pull.UP

btn_T = digitalio.DigitalInOut(board.GP12)
btn_T.direction = digitalio.Direction.INPUT
btn_T.pull = digitalio.Pull.UP

btn_Y = digitalio.DigitalInOut(board.GP13)
btn_Y.direction = digitalio.Direction.INPUT
btn_Y.pull = digitalio.Pull.UP

kbd = keyboard.Keyboard(usb_hid.devices)

while True:
    if not(btn_H.value):
        print("H")
        kbd.send(keyboard.Keycode.H)
        time.sleep(0.1)

    if not(btn_G.value):
        print("G")
        kbd.send(keyboard.Keycode.G)
       
    if not(btn_T.value):
        print("T")
        kbd.send(keyboard.Keycode.T)

    if not(btn_Y.value):
        print("Y")
        kbd.send(keyboard.Keycode.Y)