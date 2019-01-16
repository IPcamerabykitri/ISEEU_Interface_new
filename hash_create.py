import hashlib
import sys
import threading
import time

"""
create SHA-1 hash value then store into hash_result.txt
"""

def hash():

    f=open('filename','rb')
    data=f.read()
    f.close()

    sys.stdout=open('hash_result.txt','w')

    print("SHA-1: " + hashlib.sha1(data).hexdigest())
    print(time.ctime())

    threading.Timer(5,hash).start()

hash()




