
#
#  pip install apscheduler
#  file name: scheduler.py
#  python3 scheduler.py
# 


from apscheduler.schedulers.background import BackgroundScheduler
import time

def job(arg1):
    print(f'Task is running... {arg1}')

scheduler = BackgroundScheduler()
job1= scheduler.add_job(job, 'interval', seconds=10, args=[1])
job2=scheduler.add_job(job, 'interval', seconds=5, args=[2])
scheduler.start()

time.sleep(20)  
scheduler.remove_job(job2.id)

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
