import time
import usb_hid
from adafruit_hid import keyboard
import board
import digitalio

btnESC = digitalio.DigitalInOut(board.GP14)
btnESC.direction = digitalio.Direction.INPUT
btnESC.pull = digitalio.Pull.UP

btnSPACE = digitalio.DigitalInOut(board.GP15)
btnSPACE.direction = digitalio.Direction.INPUT
btnSPACE.pull = digitalio.Pull.UP

btnup = digitalio.DigitalInOut(board.GP13)
btnup.direction = digitalio.Direction.INPUT
btnup.pull = digitalio.Pull.UP

btndown = digitalio.DigitalInOut(board.GP11)
btndown.direction = digitalio.Direction.INPUT
btndown.pull = digitalio.Pull.UP

btnleft = digitalio.DigitalInOut(board.GP12)
btnleft.direction = digitalio.Direction.INPUT
btnleft.pull = digitalio.Pull.UP

btnright = digitalio.DigitalInOut(board.GP10)
btnright.direction = digitalio.Direction.INPUT
btnright.pull = digitalio.Pull.UP

kbd = keyboard.Keyboard(usb_hid.devices)

while True:
    if not(btnESC.value):
        print("ESC")
        kbd.send(keyboard.Keycode.ESCAPE)
        
    if not(btnSPACE.value):
        print("SPACE")
        kbd.send(keyboard.Keycode.SPACEBAR)
        
    if not(btnup.value):
        print("W")
        kbd.send(keyboard.Keycode.W)
        
    if not(btndown.value):
        print("S")
        kbd.send(keyboard.Keycode.S)
        
    if not(btnright.value):
        print("A")
        kbd.send(keyboard.Keycode.A)
        
    if not(btnleft.value):
        print("D")
        kbd.send(keyboard.Keycode.D)