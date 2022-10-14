
import pygame
import lcd_pokus
import time


def key_input ():
    pygame.init()
    window = pygame.display.set_mode((100, 100))
    #pygame.display.set_caption("Pygame Demonstration")

    enter_pressed_count = 0
    pressed_keys = []
    inputs = True
    
    


    lcd_pokus.clear ()
    lcd_pokus.write ("Enter your VUT ID:",1)
    try:
        while inputs:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inputs = False

                if event.type == pygame.KEYDOWN:
                    pressed_key = pygame.key.name(event.key)
                    
                    if event.key == pygame.K_BACKSPACE:
                        if pressed_keys == []:
                            pass
                        else:
                            del pressed_keys[-1]
                        lcd_pokus.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                    
                    elif event.key == pygame.K_RETURN:
                        
                        if pressed_keys == []:
                            lcd_pokus.display ("VUT ID", 'is more than', "0 characters",'', clear = True)
                            
                            time.sleep (2)
                            lcd_pokus.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                        
                    
                        
                        else:
                            enter_pressed_count += 1
                            print ("enter_pressed_count: " + str (enter_pressed_count))
                            if enter_pressed_count == 1:
                                
                                first_id = ""
                                first_id = first_id.join(pressed_keys)
                                pressed_keys = []

                                print ("first ID set: " + str(first_id))
                                lcd_pokus.display ("Enter VUT ID again.", '', pressed_keys,'', clear = True)
                                time.sleep (1)
                                lcd_pokus.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                                
                                
                            elif enter_pressed_count == 2:
                                enter_pressed_count = 0
                                second_id = ""
                                second_id = second_id.join (pressed_keys)
                                                    
                                pressed_keys = []
                                print ("second ID set: " + str(second_id))
                                if (first_id == second_id) and len (first_id) != 0 and len (second_id) != 0 :
                                    print ("VUT IDs are same, sending data pair to CRM")
                                    lcd_pokus.display ("Sending data", 'to the database.', "Have a nice day!",'', clear = True)
                                    time.sleep (3)
                                    lcd_pokus.clear () 
                                                
                                    pygame.quit()
                                   
                                else:
                                    lcd_pokus.display ("Entered IDs", 'are not identical.', "Try again.",'', True)
                                    time.sleep (2)
                                    lcd_pokus.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                        
                    
                    else:
                        pressed_keys.append(pressed_key)
                        lcd_pokus.display ("Your VUT ID:", '', pressed_keys,'', clear = True)
                        print (pressed_keys)
    
    except Exception as e:
        print (e)                       
                    
                    


key_input ()

time.sleep (3)

key_input ()