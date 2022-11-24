import time
from RPLCD.i2c import CharLCD
import config

#initialize the LCD display, (expander chip, port)
lcd = CharLCD('PCF8574', 0x27)

#write to display:
    #lcd.write_string('Hello\r\n  World!')
    #lcd.write_string('Raspberry Pi HD44780')
    #lcd.cursor_pos = (2, 0) => (row, column)
    #lcd.write_string('https://github.com/\n\rdbrgn/RPLCD')
#Backlight control:
    #lcd.backlight_enabled = True/False
#Clear display:
    #lcd.clear()
#

def display (line1, line2, line3, line4, clear = True,):
    # display ("Your VUT card is not", "in database yet.", "Let's change that.","", clear = True)
    if clear == True:
        lcd.clear()
    write (line1,1)
    write (line2,2)
    write (line3,3)
    write (line4,4)   


def backlight (status=True):
    lcd.backlight_enabled = status  

def clear():
    lcd.clear()

def write (text, row):
    lcd.cursor_pos = (row-1, 0)
    lcd.write_string (text)

def version ():
    backlight (True)
    lcd.clear() #clear the display
    write ("Version:",1)
    write (config.git_release,2)

def LCD_init (ip, mac):
    backlight (True)
    lcd.clear() #clear the display
    write ("IP adress:", 1) #show IP adress
    
    if ip == 0: #if there is not internet connection, therefore IP is 0
        write ("Not Connected", 2)     #show not connected
    else:
        write (ip, 2) # otherwise display IP adress
    write ("MAC adress:",3) # display MAC adress
    write (mac,4)
    
def LCD_waiting ():
    backlight (True)
    display ("Hello!", "Please scan your", "VUT card.","", clear = True)
 
def not_in_database ():
    #user not in database, enter VUT ID
    backlight (True)
    display ("Your VUT card is not", "in database yet.", "Let's change that.",'', clear = True)
    time.sleep (3) 
    
def in_database ():
    #user card is in internal database
    backlight (True)
    display ("Hello " + str(config.user_name) + ",", 'your card is set.', "RFID blue boxes","will work now.", clear = True)
    time.sleep (3) 
    

    
