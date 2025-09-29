from scapy.all import IP, TCP, sr1, RandShort, Ether, ARP, srp
import json
import requests

def scan_ports(host, ports=[21, 22, 80, 443, 8080], timeout=1):
    open_ports = []
    for port in ports:
        packet = IP(dst=host)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=timeout, verbose=0)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
    return open_ports

def scan_network(ip_range="192.168.1.0/24", ports=[21, 22, 80, 443, 8080]):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    hosts = [received.psrc for sent, received in result]
    
    scan_results = {}
    for host in hosts:
        open_ports = scan_ports(host, ports)
        if open_ports:
            scan_results[host] = open_ports
    return scan_results

def send_to_laravel(data, api_url="http://localhost:8000/api/scans"):
    try:
        response = requests.post(api_url, json={"results": data})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    results = scan_network()
    print("Résultats du scan :", json.dumps(results, indent=2))
    print("Envoi à Laravel :", send_to_laravel(results))