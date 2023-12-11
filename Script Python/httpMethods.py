import requests

def scan_metodi_http(ip_bersaglio):
	metodi_http =["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
#il ciclo for manda una richiesta per ogni metodo e da in risultato il codice di stato
	for method in metodi_http:
		try:
			url=f"http://{ip_bersaglio}/"
			response = requests.request(method, url, verify=False)
			print(f"{method}: {response.status_code}")
		except requests.exceptions.RequestException as e:
			print(f"{method}: Errore - {e}")
if __name__ == "__main__":
#questa sezione di codice è utilizzata in caso lo script venga avviato come "main" e non come modulo di uno script esterno
	ip_bersaglio=input("Inserici l'indirizzo ip target: ")
	scan_metodi_http(ip_bersaglio)
