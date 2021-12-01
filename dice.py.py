# Add your Python code here. E.g.
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        choice = random.randrange(1,6)
        if choice == 1:
            display.show(Image('00000:'

                   '00000:'

                   '00900:'

                   '00000:'

                   '00000'))
        if choice == 2:
            display.show(Image('90000:'

                   '00000:'

                   '00000:'

                   '00000:'

                   '00009'))
        if choice == 3:
            display.show(Image('90000:'

                   '00000:'

                   '00900:'

                   '00000:'

                   '00009'))
        if choice == 4:
            display.show(Image('90009:'

                   '00000:'

                   '00000:'

                   '00000:'

                   '90009'))
        if choice == 5:
            display.show(Image('90009:'

                   '00000:'

                   '00900:'

                   '00000:'

                   '90009'))
        if choice == 6:
            display.show(Image('90909:'

                   '00000:'

                   '00000:'

                   '00000:'

                   '90909'))