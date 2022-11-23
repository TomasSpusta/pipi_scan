import config
import pygame
import LCD_display
import time
import web_requests


def key_input ():
    if config.in_database == False:
        # If the card is not in database, initialize pygame module to scan for key presses
        pygame.init()
        window = pygame.display.set_mode((100, 100)) #pygame window needs to be open and active to scan for keypresses
        
        #initial variables       
        enter_pressed_count = 0
        pressed_keys = []
        inputs = True
        pressed_key = 0
     
        LCD_display.clear ()
        LCD_display.write ("Enter your VUT ID:",1)
        try:
            #scanning for key inputs
            while inputs:
                #for every key input it will do specific things
                for event in pygame.event.get():
                    # if quit is called - pygame window is closed
                    if event.type == pygame.QUIT:
                        inputs = False
                    # keypress section
                    if event.type == pygame.KEYDOWN:
                        #if the numbers on numerical calculator are pressed, they are converted to the "top" numbers    
                        if event.key >= 0x100 and event.key <= 0x109:
                            event.key = event.key - 0xD0
                            pressed_key = pygame.key.name(event.key) 
                            pressed_keys.append(pressed_key)
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)        
                                       
                        # if characters other than numbers are pressed, it will pass, and do not show them on display 0x30 is 0 and 0x39 is 9
                        elif event.key >= 0x30 and event.key <=0x39:                      
                            event.key = event.key
                            pressed_key = pygame.key.name(event.key)
                            pressed_keys.append(pressed_key)
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            
                        #if BACKSPACE is presed, last character on the screen is deleted
                        elif event.key == pygame.K_BACKSPACE:
                            if pressed_keys == []:
                                pass
                            else:
                                del pressed_keys[-1]
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            
                        #if ESCAPE is pressed program will return to "Scan your card please" screen, reset variables
                        elif event.key == pygame.K_ESCAPE:
                            enter_pressed_count = 0
                            pressed_keys = []
                            pygame.quit() 
                            
                        #if ENTER is pressed, program will continue to next stage according to how many times enter was pressed    
                        elif event.key == pygame.K_RETURN:
                            
                            if pressed_keys == []:
                                LCD_display.display ("VUT ID", 'is more than', "0 characters",'', clear = True)
                                time.sleep (2)
                                LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
 
                            else:
                                enter_pressed_count += 1
                                print ("enter_pressed_count: " + str (enter_pressed_count))
                                if enter_pressed_count == 1:
                                    
                                    first_id = ""
                                    first_id = first_id.join(pressed_keys)
                                    pressed_keys = []

                                    print ("first ID set: " + str(first_id))
                                    LCD_display.display ("Enter VUT ID again.", '', pressed_keys,'', clear = True)
                                    time.sleep (1)
                                    LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                                    
                                    
                                elif enter_pressed_count == 2:
                                    enter_pressed_count = 0
                                    second_id = ""
                                    second_id = second_id.join (pressed_keys)                  
                                    pressed_keys = []
                                    
                                    print ("second ID set: " + str(second_id))
                                    
                                    #Compare the 1st and 2nd IDs
                                    if (first_id == second_id) and len (first_id) != 0 and len (second_id) != 0 :
                                        print ("VUT IDs are same, sending data pair to CRM")
                                        
                                        LCD_display.display ("Sending data", 'to the database.', "Thank You!",'', clear = True)
                                        time.sleep (5)
                                        config.vut_id = str(second_id)
                                        #web_requests.crm_send_dataset ()
                                        status_code = web_requests.crm_send_dataset ()
                                        print (status_code)
                                        
                                        if status_code == 200:
                                            LCD_display.display ("Writing completed.", 'Data are saved.', "Blue boxes online",'', clear = True)
                                        else:
                                            LCD_display.display ("Error.", 'Something went wrong.', "Try to repeat,",'or visit user office', clear = True)

                                        time.sleep (5)
                                        #print ("VUT ID is: " + str (config.vut_id) + str (type(config.vut_id)))
                                        #print ("Card ID is: " + str (config.card_id) + str (type(config.card_id)))
                                        #LCD_display.clear ()          
                                        pygame.quit()
                                    
                                    else:
                                        LCD_display.display ("Entered IDs", 'are not identical.', "Try again.",'', True)
                                        time.sleep (2)
                                        LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            
                        
                        else:
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            #print (pressed_keys)
        
        except Exception as e:
            print (e)                       
                        
                    
