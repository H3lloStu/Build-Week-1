import socket
def scan_ports(target_host, start_port, end_port):
    print(f"Scanning {target_host} per porte aperte...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)        
        try:
            sock.connect((target_host, port))
            servizio = socket.getservbyport(port)
            print(f"Porta {port} aperta {servizio}")
        except (socket.timeout, socket.error):
            pass
        finally:
            sock.close()
if __name__ == "__main__":
    target_host = input("Inserisci l'indirizzo IP del target: ")
    start_port = int(input("Inserisci la porta di inizio dello scanning: "))
    end_port = int(input("Inserisci la porta di fine dello scanning: "))
    scan_ports(target_host, start_port, end_port)
    
    