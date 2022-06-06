#!/usr/bin/python

import thread
import time
import Queue
import random

BUF_SIZE = 200

q = Queue.Queue(BUF_SIZE)

# Define a function for the thread
def ProducerThread( threadName, delay):
   count = 0
   while True:
        if not q.full():
                item = random.randint(1,10)
                q.put(item)
                time.sleep(0.1)
                print( "ProducerThread %s " % ( threadName   ))

def ConsumerThread( threadName, delay):
    count = 0
    while  True:
        if not q.empty():
            item = q.get()
            count = count +1
            print(  "ConsumerThread %s qsize=%d  count=%d" % ( str(item) ,  q.qsize() ,count ))


# producer ->  Consumer 


# Create two threads as follows
try:
    for x in range(0, 200):
        threadName= "threadName-" + str( x)
        thread.start_new_thread( ProducerThread, (threadName, 1, ) )
    thread.start_new_thread( ConsumerThread, ("ConsumerThread", 1, ) )
    
except:
   print ("Error: unable to start thread")

while 1:
   pass