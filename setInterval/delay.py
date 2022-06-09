# python3  set_interval.py
import time
def get_nano_secs_01():
    nanosec =  time.time_ns()
    return nanosec


def get_nano_secs_02(mil_secs):
    nanosec   = time.perf_counter()*1000000000
    return nanosec
    
   