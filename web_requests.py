
import requests
import config
import unidecode




def git_version ():
   # https://api.github.com/repos/{owner}/{repo}/releases/latest
    response = requests.get("https://api.github.com/repos/TomasSpusta/pipi_reader/releases/latest")
    config.git_release = response.json()["name"]
    print (config.git_release)
        
def crm_request_rfid ():
    #scanned_rfid = str (scanned_rfid)
    payload = {"rfid":config.card_id}
    
    try:
        crm_response = requests.post ("https://betacrm.api.ceitec.cz/get-contact-by-rfid", json = payload)
        crm_data = crm_response.json()
        #print (crm_data)
        
        if len (crm_data) == 0:
            config.in_database = False
            print ("User is not in database") # User is not in CRM database so we can continue with the process
            
        else:          
            config.in_database = True
            user_name = crm_data[0]["firstname"]
            config.user_full_name = crm_data[0]["full_name"]
            config.user_name = unidecode.unidecode (user_name)
            config.user_id = crm_data[0]["contactid"]
            #print (config.user_name)
            #print ("User ID is {} and User's first name is {}" .format(config.user_id, config.user_name))
             
    except Exception as e:
        print("Error in crm_request_rfid:")
        print (e)
   
def crm_send_dataset ():
    payload = {"vutid":config.vut_id, "rfid":config.card_id}

    try:
        crm_response = requests.patch ("https://crm.api.ceitec.cz/save-rfid-by-vutid", json = payload)
        crm_data = crm_response.json()
        
        print (crm_data)
        print (crm_response.status_code)
        
        if crm_response.status_code == 200:
            print ("Writing to database successful")
        else:
            print ("Writing to database failed.")
             
    except Exception as e:
        print("Error in crm_request_rfid:")
        print (e)
 