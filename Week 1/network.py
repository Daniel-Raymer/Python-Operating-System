#!/usr/bin/env python3
import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return True

def check_connectivity():
        request = requests.get("http://www.google.com")
        if request.status_code == 200:
                return True

if check_localhost() and check_connectivity():
    print("Everything ok")