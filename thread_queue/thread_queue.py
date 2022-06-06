#!/usr/bin/python

import thread
import time
import Queue
import random

BUF_SIZE = 100

q = Queue.Queue(BUF_SIZE)

# Define a function for the thread
def ProducerThread( threadName, delay):
   count = 0
   while True:
        if not q.full():
                item = random.randint(1,10)
                q.put(item)
                time.sleep(0.1)

def ConsumerThread( threadName, delay):
   
   while  True:
      if not q.empty():
            item = q.get()
            print(  "ConsumerThread %s " % ( str(item)   ))
             


# producer ->  Consumer 


# Create two threads as follows
try:
   thread.start_new_thread( ProducerThread, ("Thread-1", 2, ) )
   thread.start_new_thread( ConsumerThread, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass