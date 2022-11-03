from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


# Jobs
scheduler = BackgroundScheduler()
# scheduler.add_job(job1, "interval", seconds=10, next_run_time=datetime.now())
# scheduler.add_job(job2, "cron", hour=7, minute=0)
