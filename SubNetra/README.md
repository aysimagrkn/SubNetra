# SubNetra | IPv4/IPv6 Network Calculator

**SubNetra** is a minimalist command-line IP network calculation tool for cybersecurity and networking students and administrators. It analyzes IPv4 and IPv6 networks, determines subnet details, and quickly calculates network parameters.

---

## ✨ Features

* **IPv4 calculations:** Network address, broadcast address, subnet mask, wildcard mask, binary subnet mask, IP class (A, B, C, D, E), prefix length, public/private type, CIDR notation, binary / integer / hex network ID, usable and total host counts, first/last host, and a host list for small subnets.
* **IPv6 analysis:** Network address, CIDR notation, prefix length, total IP capacity, private / loopback / link-local checks, and integer / hex network ID.
* **Single IPs supported:** An address without a prefix is treated as `/32` (IPv4) or `/128` (IPv6).
* **Lightweight:** Pure Python, no third-party dependencies.

---

## 🛠️ Technologies Used

* Python 3 (standard library `ipaddress` module)

---

## 🚀 Installation and Execution

Python 3.8 or newer is recommended. No extra packages are required, so there is nothing to install (see `requirements.txt`).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aysimagrkn/SubNetra.git
   ```
2. **Go to the project folder:**
   ```bash
   cd SubNetra/subnetra
   ```
3. **Run the program:**
   ```bash
   python3 app.py
   ```
4. Enter a network such as `192.168.1.0/24` or `2001:db8::/64`. Press Enter without typing anything to use the default `192.168.1.0/24`, and type `q` to quit.

---

