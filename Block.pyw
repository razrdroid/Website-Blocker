##r for row string if any path starts with \n py will understand it as break line so we
##add r so it should read it as row
import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
with open ("Websites.txt",'r') as file:
    websites=file.read().split("\n")
##websites=["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 4)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,5):
  ##      print("working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website + ' \n')
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in websites):
                    file.write(line)
            file.truncate()
       ## print("Fun Hours..")
    time.sleep(2)
        
