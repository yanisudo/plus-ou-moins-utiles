import ssl
import socket
from datetime import datetime

def get_ssl_certificate_info(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            return {
                "issuer": dict(x[0] for x in cert['issuer']),
                "subject": dict(x[0] for x in cert['subject']),
                "notBefore": cert['notBefore'],
                "notAfter": cert['notAfter'],
                "serialNumber": cert['serialNumber'],
            }

if __name__ == "__main__":
    hostname = "www.exemple.com"
    cert_info = get_ssl_certificate_info(hostname)
    print(cert_info)
