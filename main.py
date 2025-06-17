# CODDED BY RAYZER
import requests  # By Rayzer
from rich.console import Console  # By Rayzer
from rich.text import Text  # By Rayzer

console = Console()  # By Rayzer

raw_links = [  # By Rayzer
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/socks4.txt",  # By Rayzer
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt",  # By Rayzer
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt",  # By Rayzer
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/all/data.txt"  # By Rayzer
]  # By Rayzer

def clean_proxies(text):  # By Rayzer
    lines = text.splitlines()  # By Rayzer
    clean = []  # By Rayzer
    for line in lines:  # By Rayzer
        line = line.strip()  # By Rayzer
        if not line or 'socks5' in line.lower(): continue  # By Rayzer
        if "://" in line:  # By Rayzer
            line = line.split("://", 1)[-1]  # By Rayzer
        if ":" in line and len(line.split(":")) == 2:  # By Rayzer
            ip, port = line.split(":")  # By Rayzer
            if ip.replace(".", "").isdigit() and port.isdigit():  # By Rayzer
                clean.append(f"{ip}:{port}")  # By Rayzer
    return clean  # By Rayzer

all_proxies = []  # By Rayzer

for url in raw_links:  # By Rayzer
    try:  # By Rayzer
        response = requests.get(url, timeout=10)  # By Rayzer
        if response.status_code == 200:  # By Rayzer
            cleaned = clean_proxies(response.text)  # By Rayzer
            all_proxies.extend(cleaned)  # By Rayzer
    except Exception as e:  # By Rayzer
        pass  # By Rayzer

with open("proxies.txt", "w") as f:  # By Rayzer
    for proxy in all_proxies:  # By Rayzer
        f.write(proxy + "\n")  # By Rayzer

console.print(Text(f"[+] Fetched {len(all_proxies)} Proxies", style="green"))  # By Rayzer
console.print(Text("[+] Saved To proxies.txt", style="green"))  # By Rayzer
