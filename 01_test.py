# test_thread_and_queue.py
import unittest
from unittest.mock import Mock
from threading import Thread
from time import sleep
from queue import Queue
from sub import ThreadAndQueue, Animal, Dog

class TestThreadAndQueue(unittest.TestCase):

    def test_processData_count(self):
        # Create an instance of ThreadAndQueue
        my_instance = ThreadAndQueue()
        
        # Create mock objects for Animal and Dog
        mock_animal = Mock(spec=Animal)
        mock_dog = Mock(spec=Dog)
        
        # Replace the speak method with a mock
        mock_animal.speak = Mock()
        mock_dog.speak = Mock()
        
        # Add mock objects to the queue
        for _ in range(30):
            my_instance.add_oject(mock_dog)
            my_instance.add_oject(mock_animal)
        
        # Start the thread
        my_instance.start_thread()
        
        # Allow some time for processing
        sleep(5)
        
        # Stop the thread
        my_instance.destroy_thread()
        
        # Check that the speak method was called the correct number of times
        self.assertEqual(mock_animal.speak.call_count, 30)
        self.assertEqual(mock_dog.speak.call_count, 30)

if __name__ == '__main__':
    unittest.main()
