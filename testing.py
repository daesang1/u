import datetime
import os 

now = datetime.datetime.now()
f = open("input.txt","r")
address = open("address.txt", "r")
date = f.read() 
os.system("youtube-dl -i --dateafter " + date + " " + address.read());
f.close()
f = open("input.txt","w")
f.write(now.strftime("%Y%m%d"))
print now.strftime("%Y%m%d")
f.close()

