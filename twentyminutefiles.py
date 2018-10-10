import os

from os import listdir

from os.path import join

from datetime import datetime

from datetime import timedelta

print("Files created in the last 20 minutes")

x=input("input ur directory location")
dir_path = x
os.chdir(dir_path)
stat = os.stat(dir_path)

for file in listdir(dir_path):
        path_to_file =join(dir_path, file)
        stat = os.stat(path_to_file)
        time = stat.st_mtime
        modified_time = datetime.fromtimestamp(time)
        remaining_time = datetime.now()- modified_time
        if remaining_time.days == 0: 
            remaining_time_minute = remaining_time.seconds/60
            if(remaining_time_minute < 21.00):
                print(dir_path+"/"+file +"                "+ str(modified_time))
    
