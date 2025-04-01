import threading
import time
import queue

class ThreadAndQueue:
    def __init__(self):
        print(f"Object is created")
        self.object_list = queue.Queue()
        self.is_running = False

    def __del__(self):
        self.is_running = False
        print(f"Object is destroyed")

    def worker(self):
        while self.is_running == True:
            if  self.object_list.empty():
                time.sleep(1)
                continue   
            item = self.object_list.get()
            self.processData(item)
            self.object_list.task_done()

    def processData(self, item):
        item.speak()

    def add_oject(self, new_object): 
        if self.object_list.full():
            print(f"the queue is full")
            time.sleep(1)
        self.object_list.put(new_object)

    def start_thread(self):
        self.is_running = True
        thread = threading.Thread(target=self.worker)
        thread.start()

    def destroy_thread(self):
        print("destroy_thread")
        self.is_running = False

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
     

# # Create an instance of the class and start the thread
# my_instance = ThreadAndQueue( )
# my_instance.start_thread()

# for item in range(30):
#     my_instance.add_oject( Dog())
#     my_instance.add_oject( Animal())

# for index in range(30):
#     print("time.sleep(1)")
#     time.sleep(1)

# my_instance.destroy_thread()
# del  my_instance

# print("End ")
