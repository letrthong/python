import threading
import queue
import time

# Create a queue
task_queue = queue.Queue()

# Define a worker function
def worker():
    while True:
        task = task_queue.get()
        if task is None:
            print("worker break")
            break
        print(f'Processing task: {task}')
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
    task_queue.put(str(task) + " abc ")

# Block until all tasks are done
task_queue.join()

# Stop workers
for i in range(num_worker_threads):
    task_queue.put(None)
for thread in threads:
    thread.join()

print('All tasks are completed.')
