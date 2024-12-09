# ARP-Poisoning-Lab
## 📖 Overview
This repository contains an ARP Poisoning Lab designed for educational purposes to demonstrate network vulnerabilities and teach mitigation techniques. The lab environment includes three virtual machines (Ubuntu Server, Kali Linux, and Windows 10) configured in a Host-Only network using VMware Workstation. The lab setup simulates an ARP poisoning attack to explore network security principles.

---

## 🛠️ Features
- Custom ARP Poisoning Script: A Python script (arp_poisoning.py) leveraging Scapy for ARP spoofing, DoS attacks, and ARP table restoration.
- Isolated Virtual Network: Ensures all activities are confined within a private lab environment.
- Hands-On Learning: Demonstrates attack vectors, impact on victim devices, and countermeasures.
- Cross-Platform Testing: Works across Linux (Kali) and Windows (Victim) platforms.
  
## 🔧 Requirements
### Software
  - VMware Workstation or equivalent virtualization software.
  - Python 3.6+ installed on the attacker machine
  - Hardware
      Minimum 8GB RAM and 100GB disk space across all virtual machines.
#### On Kali Linux (Attacker):
  Scapy library for network packet manipulation:
  ```bash
  pip install scapy
  ```
---

## 📂 Repository Contents
  - ARP_Poisoning.py: Python script for ARP spoofing and DoS attacks.
  - Setup ARP Poisioning Lab.md : Detailed lab setup instructions.
  - LICENSE: License for the repository.
  - README.md: Overview of the project.

---

## 🚀 How to Use
### 1. Clone the Repository:

```bash
git clone https://github.com/Heaven229-c/ARP-Poisoning-Lab.git
cd ARP-Poisoning-Lab
```
### 2. Set Up the Lab: Follow the instructions in Setup ARP Poisoning Lab.md to configure the virtual machines and the network environment.

### 3. Run the Script:
**Start the Python script on the Kali Linux machine:**
```bash
python3 ARP_Poisoning.py
```
Choose the desired operation from the menu (e.g., scan network, ARP spoofing, DoS attack).

**4.Observe and Analyze:**
  - Use Wireshark or similar tools to analyze the traffic.
  - Monitor the victim’s device for connectivity issues or altered ARP tables.

**5.Restore Network:**
Ensure ARP tables are restored after testing by selecting the appropriate option in the script.

---

## ⚠️ Legal Disclaimer
This project is for educational and research purposes only. Do not use it for unauthorized testing or malicious purposes. Always obtain proper permissions before conducting tests.

---

## 🔮 Future Development
Mitigation Tutorials: Add guides for configuring ARP table static entries or using tools like arpwatch.
Automated Reporting: Implement a feature to generate detailed logs and reports of ARP attacks.
Expanded Lab Scenarios: Include additional attack simulations (e.g., DNS spoofing, MITM attacks).
Dockerized Lab Environment: Provide a pre-configured, containerized lab setup for ease of deployment.

---

## 📫 Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

##🌟 Acknowledgments
Special thanks to the open-source community and developers of Scapy for enabling powerful and flexible network packet manipulation.






