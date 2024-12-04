import time 
import random
name = input("Hello,what is your name?")
time.sleep(2) 
print("Hello "+ name)
feeling = input("How are you today?")
time.sleep(2)
if "good" in feeling:
 print("i'm feeling good tool") 
else:
 print("i m sorry to hear that!") 
 time.sleep(2)
favcolour=input("what is your favorite colour?")
colours=["Red","Green","Blue"]
time.sleep(2)
print("My favourite colour is "+random.choice(colours))
