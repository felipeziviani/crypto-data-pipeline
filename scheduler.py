import schedule
import time
from main import main

schedule.every().day.at("09:00").do(main) 
schedule.every().day.at("15:00").do(main)  
schedule.every().day.at("21:00").do(main) 

print("Scheduler iniciado...")

while True:
    schedule.run_pending()
    time.sleep(60)