#!/usr/bin/python2
import webbrowser as w
options='''
press  1  to  open default web browser :   
press  2  to  check currnet logined user  :   
press  3  to  ask user input  and search in google  :   
press  4  to  check number of tabs in your web browser :   
press  5  to  logout your system graphically  :   
press  6  to  login  facebook account  :   
press  7  to  send email to someone  :   
press  8  to  list all connected ip and mac in your current network  :  
''' 
print options 
choice=raw_input()
# put your if else code here 
print choice
if choice=='1':
    w.open('new tab')
#elif choice=='2':
elif choice=='3' :
    print 'Enter for search on google'
    q=raw_input()
    w.open_new_tab('www.google.com/search?q='+q)
#elif choice=='4' :
#elif choice=='5' :
#elif choice=='6' :    
#elif choice=='7' :
#elif choice=='8' :    
