import ipaddress
try:
    ip_inserido = str(input("Digite o IP:"))
    teste = ipaddress.ip_address(ip_inserido)
    if teste.is_multicast:
        print("nao eh possivel inserir um endereco broadcast.")    
    if teste.is_loopback:
        print("nao eh possivel utilizar ip de loopback.")
    if teste.is_multicast or teste.is_loopback == False:
        print("seu endereco ip",teste,"eh valido")
except (ValueError, NameError):
    print("Este IP nao eh valido")
    
""" """ """ from ipaddress import ip_interface, ip_network
from IPy import IP
import socket
ip_inserido = str(input("Digite o IP:"))

s=ip_inserido
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
     """
""" 
for x in ip:
    print(x)
    print(ip)
 """
""" try:
    socket.inet_aton(ip_inserido)
    # legal
except:
    socket.error
    # Not legal """ """ """
