import config
import pygame
import LCD_display
import time
import web_requests


def key_input ():
    if config.in_database == False:
        pygame.init()
        window = pygame.display.set_mode((100, 100))
        #pygame.display.set_caption("Pygame Demonstration")

        enter_pressed_count = 0
        pressed_keys = []
        inputs = True
        
        


        LCD_display.clear ()
        LCD_display.write ("Enter your VUT ID:",1)
        try:
            while inputs:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        inputs = False

                    if event.type == pygame.KEYDOWN:
                        pressed_key = pygame.key.name(event.key)
                        print ("event key")
                        print (event.key)
                        
                        if event.key == pygame.K_BACKSPACE:
                            if pressed_keys == []:
                                pass
                            else:
                                del pressed_keys[-1]
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                        
                        elif event.key == pygame.K_ESCAPE:
                            enter_pressed_count = 0
                            pressed_keys = []
                            pygame.quit() 
                            
                            
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
                                    if (first_id == second_id) and len (first_id) != 0 and len (second_id) != 0 :
                                        print ("VUT IDs are same, sending data pair to CRM")
                                        LCD_display.display ("Sending data", 'to the database.', "Have a nice day!",'', clear = True)
                                        time.sleep (3)
                                        
                                        
                                        config.vut_id = str(second_id)
                         
                                        print ("VUT ID is: " + str (config.vut_id) + str (type(config.vut_id)))
                                        print ("Card ID is: " + str (config.card_id) + str (type(config.card_id)))
                                        
                                        ###
                                        # TODO : API for uploading data sets VUT_ID - CARD_ID to CRM/APOLLO
                                        web_requests.crm_send_dataset ()
                                        
                                        
                                        ###
                                        
                                        #LCD_display.display ("Please wait for", "X minutes and swipe", "your card again","to verify procedure", clear = True)
                                        LCD_display.clear ()          
                                        pygame.quit()
                                    
                                    else:
                                        LCD_display.display ("Entered IDs", 'are not identical.', "Try again.",'', True)
                                        time.sleep (2)
                                        LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            
                        
                        else:
                            pressed_keys.append(pressed_key)
                            LCD_display.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                            #print (pressed_keys)
        
        except Exception as e:
            print (e)                       
                        
                    
