import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","reuter.com","www.reuters.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working Hours.....")
        with open(host_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+website+"\n")
            
       
    else:
        with open(host_path, 'r+') as file:
            content =  file.readlines()
            file.seek(0)
            print(content)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("no trabajo")


    time.sleep(5)