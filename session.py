#@reboot python3 /home/pi/RFID/client_pokus_RFID.py
#sudo killall python3


import time
import RPi.GPIO as GPIO
import LCD_display
import web_requests
import config



def user_check ():
    web_requests.crm_request_rfid()
    if config.in_database == False:
        # If card ID is not it the internal database, LCD displays the error 
        LCD_display.not_in_database() 
    else:
        LCD_display.in_database() 
        print ('User in RFID CRM database')
        
def session_end ():
    print ("Ending session")
    #when session is ended by time out, or by pressing the button    
    config.vut_id = 0
    config.card_id = 0
    config.in_database = False

    # GPIO.cleanup(config.button_pin) # it is necessary to figure out how the button pin reacts on cleaning
    print ("Recording ended")     
    time.sleep(1)

