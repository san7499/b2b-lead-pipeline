from apscheduler.schedulers.blocking import BlockingScheduler
from scraper.yc_scraper import scrape_yc
from processing.clean_data import clean_data
from database.db import insert_data

def job():
    scrape_yc()
    clean_data()
    insert_data()
    print("Pipeline executed!")

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', hours=12)
scheduler.start()