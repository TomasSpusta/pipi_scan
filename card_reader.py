from mfrc522 import SimpleMFRC522
import config

#create RFID reader instance
reader = SimpleMFRC522() 

#Function dealing with sending and recieving the data.
#Parameter rfid is card number from MFRC522 reader

def card_reader():
    card_id, text = reader.read()
    config.card_id = str (card_id)
    #print ('Readed card: ' + str(rfid))