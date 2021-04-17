from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# hardware
led_red = LED(14)
led_blue = LED(15)
led_green = LED(18)

# GUI DEFINITIONS
win = Tk()
win.title = ("RPi GUI with 3 LEDS")
myFont = tkinter.font.Font(family = "Frutiger", size = 12, weight = "bold")

# FUNCTIONS
def ledRedToggle():
    if led_red.is_lit:
        led_red.off()
        red_button["text"] = "Turn Red LED ON"
    else:
        led_red.on()
        red_button["text"] = "Turn Red LED OFF"

def ledBlueToggle():
    if led_blue.is_lit:
        led_blue.off()
        blue_button["text"] = "Turn Blue LED ON"
    else:
        led_blue.on()
        blue_button["text"] = "Turn Blue LED OFF"

def ledGreenToggle():
    if led_green.is_lit:
        led_green.off()
        green_button["text"] = "Turn Green LED ON"
    else:
        led_green.on()
        green_button["text"] = "Turn Green LED OFF"
                
def close():
        RPi.GPIO.cleanup()
        win.destroy()

# WIDGETS
red_button = Button(win, text = "Turn Red LED ON", font = myFont, command = ledRedToggle, bg = "red", height = 1, width = 24)
red_button.grid(row = 0, column = 1)

blue_button = Button(win, text = "Turn Blue LED ON", font = myFont, command = ledBlueToggle, bg = "blue", fg = "white", height = 1, width = 24)
blue_button.grid(row = 4, column = 1)

green_button = Button(win, text = "Turn Green LED ON", font = myFont, command = ledGreenToggle, bg = "green", fg = "white", height = 1, width = 24)
green_button.grid(row = 8, column = 1)

exit_button = Button(win, text = "Exit", font = myFont, command = close, bg = "black", fg = "white", height = 1, width = 24)
exit_button.grid(row = 12, column = 1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever


