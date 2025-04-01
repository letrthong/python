import threading
import queue
import time

# Create a queue
task_queue = queue.Queue()


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
    def show(self):
          print("Dog barks")


# Define a worker function
def worker():
    while True:
        animal = task_queue.get()
        if task is None:
            print("worker break")
            break
        #print(f'Processing task: {task}')
        animal.speak()
        time.sleep(1)  # Simulate a task taking some time
        task_queue.task_done()

# Create and start worker threads
num_worker_threads = 3
threads = []
for i in range(num_worker_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Add tasks to the queue
for task in range(10):
    task_queue.put(  Animal())
    task_queue.put(  Dog())

# Block until all tasks are done
task_queue.join()

# Stop workers
for i in range(num_worker_threads):
    task_queue.put(None)
for thread in threads:
    thread.join()

print('All tasks are completed.')


 
