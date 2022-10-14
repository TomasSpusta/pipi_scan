# Main Pipi scan file
'''
1. Check internet connection, obtain IP and MAC address => internet module
2. Check git for new version 
3. Display Waiting screen "Please scan your User Card" 
4. Display message to scan user card
    if card already in CRM database - display message and display VUT ID and user name with "Is this you?" question
        if yes, display message that everything is correct and happy day and return to Waiting screen
        else, display message that something is wrong with pair VUT ID and USER card ID to visit user office
    else card is not in database - message to input the VUT ID 1st time and message to input VUT ID 2nd time
        if 1st and 2nd VUT IDs are same, post API request to write VUT ID - CARD ID pair to CRM -> return to Waiting screen
        else -they are not same - return to VUT ID input

'''


#Import section
import faulthandler
import RPi.GPIO as GPIO
import time
from keyboard_input import key_input


from network_check import network_check
from github_check import github_check

try:
    faulthandler.enable ()
    #Check internet connection, acquire IP address and MAC address
    network_check ()
    time.sleep (3)

    #Connect to GIT HUB and download the latest version from "main" or "develop" branch
    github_check (branch = "master")
    time.sleep (5)
    
    from card_reader import card_reader
    import session
    import LCD_display
    
    
    time.sleep (3)
    
    

    while 1:
        try:
            #initial waiting screen
            LCD_display.LCD_waiting()
            
            #Wait for the card swipe 
            card_reader ()
            
            #check if user's card is in the RFID/CRM database
            session.user_check ()
            
            #input module to obtain VUT ID
            key_input ()
                      
            # when session ends reset variables for new user
            session.session_end ()
        
        except Exception as e:
            print("Error in main code")
            print(e)   

except KeyboardInterrupt:
    print("CTRL + V pressed, script ended in pipi_reader script")
    
    time.sleep (0.5)
    LCD_display.backlight (False)
    LCD_display.clear ()        
    GPIO.cleanup ()
    
