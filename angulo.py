import time
import math
import matplotlib.pyplot as plt
import random
import json

anglex=[20,50,350,370]
angley=[10,40,340,365]
# Wait for 5 seconds
while(True):
    time.sleep(1)
    i=random.sample(anglex,k=1)
    j=random.sample(angley,k=1)
    #print("rotateX % 3d" %(i[0]))  
    angle = {'rotateX':i[0], 'rotateY':j[0]}
    as_json = json.dumps(angle)
    #print(type(as_json))
    print(as_json)
  

