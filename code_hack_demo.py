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


time.sleep(0)
kbd.send(keyboard.Keycode.WINDOWS)
time.sleep(1)
kbd.send(keyboard.Keycode.C)
kbd.send(keyboard.Keycode.M)
kbd.send(keyboard.Keycode.D)
time.sleep(1)
kbd.send(keyboard.Keycode.ENTER)
time.sleep(1)
kbd.send(keyboard.Keycode.C)
kbd.send(keyboard.Keycode.O)
kbd.send(keyboard.Keycode.L)
kbd.send(keyboard.Keycode.O)
kbd.send(keyboard.Keycode.R)

kbd.send(keyboard.Keycode.SPACE)
kbd.send(keyboard.Keycode.A)
kbd.send(keyboard.Keycode.ENTER)

kbd.send(keyboard.Keycode.T)
kbd.send(keyboard.Keycode.R)
kbd.send(keyboard.Keycode.E)
kbd.send(keyboard.Keycode.E)
kbd.send(keyboard.Keycode.ENTER)



