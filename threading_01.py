import threading

class MyThreadedClass:
    def __init__(self, function_to_call):
        self.function_to_call = function_to_call

    def start_thread(self):
        thread = threading.Thread(target=self.function_to_call)
        thread.start()

# Example function to be called by the thread
def example_function():
    print("Function is called by thread")

# Create an instance of the class and start the thread
my_instance = MyThreadedClass(example_function)
my_instance.start_thread()
