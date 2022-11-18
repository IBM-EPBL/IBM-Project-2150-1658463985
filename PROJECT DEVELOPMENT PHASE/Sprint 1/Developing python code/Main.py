#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
#pip install requests 
import requests, json
import time
import random
myConfig = { 
    "identity": {
        "orgId": "6q4xt1",
        "typeId": "BlackSquid",
        "deviceId":"12345"
    },
    "auth": {
        "token": "w+U5*9o*h3W0I@A-tt"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()



cityName = input("\nEnter the City Name: ")

user_input = input('\nAny school is there(yes/no): ')
user_input1 = input('\nAny hospital is there(yes/no): ')

if user_input1.lower() and user_input.lower() == 'yes':
    speedlimit=20
else:
    speedlimit=30
       
while True:
   
   
        
  
       
     
    #Get Weather data from any city 
    
    #Getting weather apiKey from Openweathermap
    apiKey="d3bcb2501b7fa0ed5ea247df2c8f6969"

    
    #The url provides the weather data about the city
    url =" https://api.openweathermap.org/data/2.5/weather?q="+ cityName + "&appid="+ apiKey + "&units=metric"

    
    response = requests.get(url)

    data =response.json()

    temp=data["main"]["temp"]

    hum=data['main']['humidity']
    
    des=data['weather'][0]['main']
    
    city=cityName.upper()
    
    myData={'temperature':temp, 'humidity':hum, "description":des, "city":city, "speedlimit":speedlimit}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("\nPublished data Successfully:  ", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
