import time 

epoch = time.time()

seconds_day = 24 * 60 * 60
seconds_hour = 60 * 60
seconds_min = 60

day = epoch // seconds_day
hours = (epoch % seconds_day) // seconds_hour + 8
minutes = (epoch % seconds_day) % seconds_hour // seconds_min
seconds = (epoch % seconds_day) % seconds_hour % seconds_min
print("%s: %s: %s: %s" %(day, hours, minutes, seconds))
print("Beijing Current time is %d: %d: %d: %d" %(day, hours, minutes, seconds)) 
