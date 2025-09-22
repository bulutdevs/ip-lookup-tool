#!/usr/bin/env python3
import sys
try:
    import requests
except Exception:
    print("requirements: pip install requests")
    sys.exit(1)
import webbrowser
banner = r"""
      .--.
   .-(    ).      _  _  _    _    _   _  _   _  _ 
  (.))    ()()( ) (_ ) (_ )()() ()()
     \/  _      _   _   _  _   _   ___  _  _  _
    /\ / /\    ()()(_ )() ( ) () ()() ()
   '  /' '  /'          bulutdevs tarafından yazıldı
"""
print(banner)
ip = input("IP adresi girin (boş bırakılırsa kendi IP'niz kullanılır): ").strip()
url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
try:
    resp = requests.get(url, timeout=8)
    data = resp.json()
except Exception as e:
    print("İstek hatası:", e)
    sys.exit(1)
if data.get("status") != "success":
    print("Sorgu başarısız:", data.get("message", "bilinmeyen hata"))
    sys.exit(1)
output_lines = [
    f"IP: {data.get('query')}",
    f"Ülke: {data.get('country')}",
    f"Bölge: {data.get('regionName')}",
    f"Şehir: {data.get('city')}",
    f"Posta Kodu: {data.get('zip')}",
    f"Enlem: {data.get('lat')}",
    f"Boylam: {data.get('lon')}",
    f"Zaman Dilimi: {data.get('timezone')}",
    f"ISP: {data.get('isp')}",
    f"Organizasyon: {data.get('org')}",
    f"AS: {data.get('as')}",
    f"Mobil: {data.get('mobile')}",
    f"Proxy/VPN/Hosting: {data.get('proxy')}",
]
print("\n".join(output_lines))
lat = data.get("lat")
lon = data.get("lon")
if lat is not None and lon is not None:
    map_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=12/{lat}/{lon}"
    print("\nHarita bağlantısı:", map_url)
    try:
        webbrowser.open(map_url)
        print("Harita tarayıcıda açıldı.")
    except Exception as e:
        print("Tarayıcıda açılırken hata:", e)
else:
    print("Koordinat bilgisi bulunamadı.")
print("\n— bulutdevs —")
