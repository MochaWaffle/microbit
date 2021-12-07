from microbit import *

compass.calibrate()

def north():
    display.show(Image('90009:'

                   '99009:'

                   '90909:'

                   '90099:'

                   '90009'))

def east():
    display.show(Image('99999:'
                    
                    '90000:'
                    
                    '99999:'
                    
                    '90000:'
                    
                    '99999:'))
                    
def south():
    display.show(Image('99999:'
                    
                    '90000:'
                    
                    '99999:'
                    
                    '00009:'
                    
                    '99999:'))
  
def west():
    display.show(Image('90009:'
                    
                    '90009:'
                    
                    '90909:'
                    
                    '99099:'
                    
                    '90009:'))
while True:
    direction = compass.heading()
    if button_a.was_pressed():
        
        if (direction > 315) or (direction < 45): 
            north()
        if (direction > 45) and (direction < 135):
            east()
        if (direction > 135) and (direction < 225):
            south()
        if (direction > 225) and (direction < 315):
            west()