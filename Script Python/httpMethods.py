import requests

def scan_metodi_http(ip_bersaglio):
	metodi_http =["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

	for method in metodi_http:

		try:
			url=f"http://{ip_bersaglio}/"
			response = requests.request(method, url, verify=False)
			print(f"{method}: {response.status.code}")
		except requests.exceptions.RequestException as e:
			print(f"{method}: Errore - {e}")
if __name__ == "__main__":
	ip_bersaglio=input("Inserici l'indirizzo ip target: ")
	scan_metodi_http(ip_bersaglio)
