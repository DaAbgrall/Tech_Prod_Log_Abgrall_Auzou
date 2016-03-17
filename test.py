import os
import time

a=0

if(os.fork()==0):
    a=2
    print("fini")
else:
    time.sleep(5)
    print(a)