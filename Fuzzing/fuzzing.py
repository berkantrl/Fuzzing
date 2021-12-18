import requests
from requests import status_codes

# 192.168.1.108 : Metasploitable 2 

header = {"Cookie":"security=low; PHPSESSID=d605d8af08bcc03c0e7206257cd62463;"}



def fuzzing():
    
    url = "http://192.168.1.108"
    file = open("fuzzing.txt","r")
    content = file.read()
    file.close();

    for i in content.splitlines():
        url_request = url+str(i)
        result =  requests.get(url = url_request, headers=header)
        if (int(result.status_code) == 200 or int(result.status_code) == 302):
            print("File and Directory name: " , i )

def subdomain():
    url = "192.168.1.108"
    file = open("subdomain.txt","r")
    content = file.read()
    file.close();

    for i in content.splitlines():
        url_request = f"http://{i}"+url
        result =  requests.get(url = url_request, headers=header)
        if (int(result.status_code) == 200 or int(result.status_code) == 302):
            print("File and Directory name: " , i )

choice = input("1 -- Fuzing \n2 -- Subdomain \nChoice a number: ")

if (int(choice) == 1):
    fuzzing()

elif (int(choice) == 2):
    subdomain()
    
else :
    print ("Wrong choice")
