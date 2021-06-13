
import time
from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc"
host_temp="hosts"
redirect="127.0.0.1"

website_list=["www.youtube.com",'www.facebook.com']

print(dt.now())

while True:
    if( dt(dt.now().year,dt.now().month,dt.now().day,15)< (dt.now()) < dt(dt.now().year,dt.now().month,dt.now().day,18)):
        print("Working hour .....")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +' '+website+"\n")



    else:
        print("Resting hour ....")
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

                file.truncate()


            time.sleep(20)





