
from Mainduplicate import overall
from RGBTOGRAY import capturing
#from main import junction2 , junction3 , junction4
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
# set up of gpios pins
J1R1=2
J1G1=3
J1Y1=26
J2R2=17
J2G2=27
J2Y2=22
J3R3=10
J3G3=9
J3Y3=11
J4R4=5
J4G4=6
J4Y4=13

GPIO.setup(J1R1,GPIO.OUT)
GPIO.setup(J1Y1,GPIO.OUT)
GPIO.setup(J1G1,GPIO.OUT)
GPIO.setup(J2R2,GPIO.OUT)
GPIO.setup(J2Y2,GPIO.OUT)
GPIO.setup(J2G2,GPIO.OUT)
GPIO.setup(J3R3,GPIO.OUT)
GPIO.setup(J3Y3,GPIO.OUT)
GPIO.setup(J3G3,GPIO.OUT)
GPIO.setup(J4R4,GPIO.OUT)
GPIO.setup(J4Y4,GPIO.OUT)
GPIO.setup(J4G4,GPIO.OUT)
# default traffic signal timings in seconds
Red_time=40
green_time = 30
yellow_time = 5

#additonal time based on traffic in seconds
T=15

J1= overall()
J2= 25000#J2_white
J3= 21000#J3_white
J4= 30000#J4_white
#time changing function
def time_change():
    if(J1<J2 and J1<J3 and J1<J4):
        GPIO.output(J1R1,GPIO.LOW)
        GPIO.output(J1Y1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.HIGH)
        GPIO.output(J2R2,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(green_time)
        GPIO.output(J1Y1,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.HIGH)
        GPIO.output(J1R1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(yellow_time)
    if(J2<J1 and J2<J3 and J2<J4):
        GPIO.output(J1R1,GPIO.HIGH)
        GPIO.output(J1Y1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.LOW)
        GPIO.output(J2Y2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.HIGH)
        GPIO.output(J3R3,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(green_time)
        GPIO.output(J1Y1,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.HIGH)
        GPIO.output(J1R1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(yellow_time)
    if(J3<J1 and J3<J2 and J3<J4):
        GPIO.output(J1R1,GPIO.HIGH)
        GPIO.output(J1Y1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.LOW)
        GPIO.output(J3Y3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.HIGH)
        GPIO.output(J4R4,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(green_time)
        GPIO.output(J1Y1,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.HIGH)
        GPIO.output(J1R1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(yellow_time)
    if(J4<J1 and J4<J2 and J4<J3):
        GPIO.output(J1R1,GPIO.HIGH)
        GPIO.output(J1Y1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.LOW)
        GPIO.output(J4Y4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.HIGH)
        time.sleep(green_time)
        GPIO.output(J1Y1,GPIO.HIGH)
        GPIO.output(J2Y2,GPIO.HIGH)
        GPIO.output(J3Y3,GPIO.HIGH)
        GPIO.output(J4Y4,GPIO.HIGH)
        GPIO.output(J1R1,GPIO.LOW)
        GPIO.output(J1G1,GPIO.LOW)
        GPIO.output(J2R2,GPIO.LOW)
        GPIO.output(J2G2,GPIO.LOW)
        GPIO.output(J3R3,GPIO.LOW)
        GPIO.output(J3G3,GPIO.LOW)
        GPIO.output(J4R4,GPIO.LOW)
        GPIO.output(J4G4,GPIO.LOW)
        time.sleep(yellow_time)

while True:
    capturing()
    time.sleep(25)
    time_change()

    


   