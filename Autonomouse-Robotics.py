'''
   Author: Mr Chanapai Chuadchum 
   Project name:  Autonomouse Robotics vision 
'''
import serial
from nanpy import(ArduinoApi,SerialManager)
from ocrtextout import ocr_msg,pid # OCR text read out function, PID for the process id to kill processing function  
from autocapturefunction import gpid 
from Autonomouscameraman import gpidd
import time   
import os   # Operating system to control the software to open when needed 
sensor1 = 0    # Back sensor of the autonomouse car 
sensor2 = 0    # Front sensor of the autonomouse car 
sensor3 = 0    # Activation sensors for the robot 
ocr_msg_text  = " " # Text message ocr 
try:
   connection = SerialManager()
   motorunit = ArduinoApi(connection=connection) #Connection astrablished 
except:
    print("Motor unit control ")
#try:
 #  sensor_msg = serial.Serial("/dev/ttyUSB0",115200)
#except:
#   print("Sensor read message error please check the sensor unit")
   # Backward function for the robot to move back and detect obstable 
def Backward_active(sensor1,SpeedStart,SpeedEnd,timechange):
      if int(sensor1) >= 50:
             motorunit.analogWrite(6,0)
             motorunit.analogWrite(10,0)
             motorunit.analogWrite(4,0)
             motorunit.analogWrite(3,0)
             motorunit.analogWrite(9,SpeedEnd + 15)  # Backward function with the control speed 
             motorunit.analogWrite(11,SpeedEnd + 15)
             motorunit.analogWrite(2,SpeedEnd + 15)
             motorunit.analogWrite(5,SpeedEnd + 15)
      else:
             #Backward part
             motorunit.analogWrite(6,SpeedStart)     # Roughly 150    
             motorunit.analogWrite(10,SpeedStart)
             motorunit.analogWrite(4,SpeedStart)
             motorunit.analogWrite(3,SpeedStart)
             time.sleep(timechange) # time sleep speed change 0.05
             motorunit.analogWrite(6,SpeedEnd)           # Roughly 127
             motorunit.analogWrite(10,SpeedEnd)
             motorunit.analogWrite(4,SpeedEnd)
             motorunit.analogWrite(3,SpeedEnd)
             #Forward function  
             motorunit.analogWrite(9,0)
             motorunit.analogWrite(11,0)
             motorunit.analogWrite(2,0)
             motorunit.analogWrite(5,0)
    # Forward and detect the obstacle in front 
def Foward_active(sensor1,sensor2,sensor3,SpeedStart,SpeedEnd,timechange,Target): 
       if int(sensor2) >= 600:
             motorunit.analogWrite(6,SpeedEnd)
             motorunit.analogWrite(10,SpeedEnd)
             motorunit.analogWrite(4,SpeedEnd)
             motorunit.analogWrite(3,SpeedEnd)
             motorunit.analogWrite(9,0)
             motorunit.analogWrite(11,0)
             motorunit.analogWrite(2,0)
             motorunit.analogWrite(5,0)


       elif int(sensor2) < 500: 
             #Backward part
             motorunit.analogWrite(6,0)
             motorunit.analogWrite(10,0)
             motorunit.analogWrite(4,0)
             motorunit.analogWrite(3,0)
             motorunit.analogWrite(9,SpeedStart)
             motorunit.analogWrite(11,SpeedStart)
             motorunit.analogWrite(2,SpeedStart)
             motorunit.analogWrite(5,SpeedStart)
             time.sleep(timechange)
             motorunit.analogWrite(6,0)
             motorunit.analogWrite(10,0)
             motorunit.analogWrite(4,0)
             motorunit.analogWrite(3,0)
             motorunit.analogWrite(9,SpeedEnd)
             motorunit.analogWrite(11,SpeedEnd)
             motorunit.analogWrite(2,SpeedEnd)
             motorunit.analogWrite(5,SpeedEnd)

         
       if int(sensor1) >= 50:
                  motorunit.analogWrite(6,0)
                  motorunit.analogWrite(10,0)
                  motorunit.analogWrite(4,0)
                  motorunit.analogWrite(3,0)
                  motorunit.analogWrite(9,SpeedStart)
                  motorunit.analogWrite(11,SpeedStart)
                  motorunit.analogWrite(2,SpeedStart)
                  motorunit.analogWrite(5,SpeedStart)
       elif int(sensor1) < 50: 
                  motorunit.analogWrite(6,0)
                  motorunit.analogWrite(10,0)
                  motorunit.analogWrite(4,0)
                  motorunit.analogWrite(3,0)
                  motorunit.analogWrite(9,0)
                  motorunit.analogWrite(11,0)
                  motorunit.analogWrite(2,0)
                  motorunit.analogWrite(5,0) 
       if int(sensor3) >= 600: 
                  motorunit.analogWrite(6,0)
                  motorunit.analogWrite(10,0)
                  motorunit.analogWrite(4,0)
                  motorunit.analogWrite(3,0)
                  motorunit.analogWrite(9,0)
                  motorunit.analogWrite(11,0)
                  motorunit.analogWrite(2,0)
                  motorunit.analogWrite(5,0)
                  os.system("python autocapturefunction.py")
                  time.sleep(0.3) 
                  os.kill(int(gpid),signal.SIGKILL) # Kill the process function Autocapture  
                  os.system("python ocrtextout.py") 
                  time.sleep(0.3)
                  os.kill(int(pid),signal.SIGKILL)  # Kill the process funciton OCR 
                  ocr_msg_text = ocr_msg.split(",")  # Split the text number function and the charactor 
                  Charactor = ocr_msg_text[0]  # OCR Text Charactor reader code 
                  Number = ocr_msg_text[1] # OCR Number read 
                  if int(Number) == 4:  
                       motorunit.analogWrite(6,0)
                       motorunit.analogWrite(10,0)
                       motorunit.analogWrite(4,0)
                       motorunit.analogWrite(3,0)
                       motorunit.analogWrite(9,0)
                       motorunit.analogWrite(11,0)
                       motorunit.analogWrite(2,0)
                       motorunit.analogWrite(5,0)
                       os.system("python Autonomouscameraman.py")  # Execute the camera man option 
                       delay(10)
                       os.kill(int(gpidd),signal.SIGKILL) 
                  elif int(sensor2) < 500: 
                                #Backward part
                                 motorunit.analogWrite(6,0)
                                 motorunit.analogWrite(10,0)
                                 motorunit.analogWrite(4,0)
                                 motorunit.analogWrite(3,0)
                                 motorunit.analogWrite(9,SpeedStart)
                                 motorunit.analogWrite(11,SpeedStart)
                                 motorunit.analogWrite(2,SpeedStart)
                                 motorunit.analogWrite(5,SpeedStart)
                                 time.sleep(timechange)
                                 motorunit.analogWrite(6,0)
                                 motorunit.analogWrite(10,0)
                                 motorunit.analogWrite(4,0)
                                 motorunit.analogWrite(3,0)
                                 motorunit.analogWrite(9,SpeedEnd)
                                 motorunit.analogWrite(11,SpeedEnd)
                                 motorunit.analogWrite(2,SpeedEnd)
                                 motorunit.analogWrite(5,SpeedEnd)
                       

while True:  
       sensor1 = motorunit.analogRead(0)#Sensor 1 functioning for the Back 
       sensor2 = motorunit.analogRead(1)#Sensor 2 functioning for the front
       print("Back sensor detection:")
       print(sensor1)
       print("Fron sensor distance :")
       print(sensor2)
       Foward_active(sensor1,sensor2,150,125,0.05,4) 
      