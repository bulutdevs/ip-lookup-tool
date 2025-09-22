# 🌍 IP Lookup Tool

> A simple yet powerful Python script to fetch detailed IP address information — including location, ISP, timezone, and more — using the [ip-api.com](https://ip-api.com/) service.

## 🚀 Features

- 🔍 Detects **your own IP** automatically or lets you query any IP address  
- 🌎 Shows country, region, city, and postal code  
- 🛰️ Displays latitude & longitude with **OpenStreetMap link**  
- 🏢 ISP, organization, and AS number lookup  
- 🛡️ Indicates whether the IP is mobile, proxy, or VPN  
- 🖥️ Opens map directly in your default browser  

---

## 📦 Installation

1. **Clone the repository:**

    git clone https://github.com/bulutdevs/ip-lookup-tool.git  
    cd ip-lookup-tool  

2. **Install dependencies:**

    pip install -r requirements.txt  

---

## ▶️ Usage

Run the script:

    python index.py

- **Press Enter** without typing anything → fetches **your own IP**  
- **Enter an IP address** → fetches data for that IP  

---

## 📸 Example Output

    IP: 8.8.8.8
    Country: United States
    Region: California
    City: Mountain View
    Postal Code: 94035
    Latitude: 37.386
    Longitude: -122.0838
    Timezone: America/Los_Angeles
    ISP: Google LLC
    Organization: Google
    AS: AS15169 Google LLC
    Mobile: False
    Proxy/VPN/Hosting: False

    Map URL: https://www.openstreetmap.org/?mlat=37.386&mlon=-122.0838#map=12/37.386/-122.0838

---

## 🛠️ Requirements

- **Python 3.7+**
- `requests` library (`pip install requests`)

---

## 📄 License

This project is licensed under the MIT License (see LICENSE file).

---

👨‍💻 Author: [bulutdevs](https://github.com/bulutdevs)  
📷 Instagram: [instagram.com/bulutdevs](https://instagram.com/bulutdevs)
