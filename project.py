#!/usr/bin/python

options='''
press 1 to check no. of tabs with their url:
press 2 to open default web browser:
press 3 to search on google:
press 4 to get ip and mac of network:
press 5 to logout all users in linux:
'''
print options
n1=raw_input("enter no:")
import webbrowser
import os
import subprocess
if n1 == '3':
	s=raw_input("type ")
	webbrowser.open_new_tab("https://www.gooogle.com/search?q="+s) 

elif n1=='4':
	os.system('arp -a')
elif n1=='2':
	webbrowser.open('https://www.google.com')

elif n1=='1':
	controller.open(url,new=0,autoraise=True)
elif n1=='5':
	os.system('logout')
	
	
else:
print "invalid"
