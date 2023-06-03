# Fill in this file with the code from parsing JSON exercise
import urllib.parse
import requests
from time import localtime

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "3y7GkpK20CyP53UV4SvPjawz1N7xSw3T"

print("BIENVENIDO")
print(localtime())

#Aqui se ingresa el origen y el destino
while True:
    orig = input("Punto de comienzo: ")
    if orig == "quit" or orig == "q":
        break
    
    dest = input("Punto de destino: ")
    if orig == "quit" or orig == "q":
        break

#Aqui muestra la url y verifica si es una respuesta exitosa
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + "= a successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:	" + (json_data["route"]["formattedTime"])) 
        print("Miles:	" + str(json_data["route"]["distance"]))
        print("=============================================")
        print("Kilometers:	" + str((json_data["route"]["distance"])*1.6100)) 
        print("Kilometers:	" + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
    

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
            print("=============================================\n")
    elif json_status == 402: 
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n") 
    else:
        print("************************************************************************") 
        print("For Status Code: " + str(json_status) + "; Refer to:") 
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") 
        print("************************************************************************\n")


    


