# 🧪 **Setup ARP Poisoning Lab**

This guide walks you through setting up a virtual lab environment to simulate ARP poisoning attacks. We'll configure a router using **Ubuntu Server**, with **Kali Linux** as the attacker and **Windows 10** as the victim. The lab uses **Host-Only networking** for isolation, and all systems will be configured on **VMware Workstation**.

---

## 📋 **Lab Overview**

| Machine         | Role              | Network Adapter | IP Address       | Gateway     |
|-----------------|-------------------|-----------------|------------------|-------------|
| **Ubuntu Server** | Router/Gateway    | NAT + Host-Only | NAT: Dynamic<br>Host-Only: `192.168.2.2` | `192.168.2.2` |
| **Kali Linux**   | Attacker          | Host-Only       | DHCP-assigned    | `192.168.2.2` |
| **Windows 10**   | Victim            | Host-Only       | DHCP-assigned    | `192.168.2.2` |

Network: **192.168.2.0/24**  
DNS Server: **8.8.8.8**

---

## 🛠️ **Setup Steps**

### **1️⃣ Create a Host-Only Network (vnet1)**

1. Open **VMware Workstation**.  
2. Go to **Edit** → **Virtual Network Editor**.  
3. Create a new Host-Only network:
   - Click **Add Network** and select **VMnet1**.
   - Configure **Subnet IP**: `192.168.2.0`.
   - Disable DHCP for **vnet1** (we will use Ubuntu as the DHCP server).  
   - Save the changes.  

---

### **2️⃣ Configure Virtual Machines**

#### **2.1 Ubuntu Server (Router/Gateway)**

1. **VM Settings**:
   - **Adapter 1**: NAT (ens33).
   - **Adapter 2**: Host-Only (ens37).
   - CPU: 2-4 cores.
   - RAM: 3GB.
   - Disk: Minimum 20GB.

2. **Install Ubuntu Server**:
   During installation, leave the network configuration as default. We'll configure it later.

3. **Set Up Network Interfaces**:
   After installation, configure the network manually:
   
   ```bash
   sudo nano /etc/netplan/50-cloud-init.yaml
   ```
   Add the following:
   
   ```yaml
   network:
    ethernets:
        ens33:
            dhcp4: true
        ens37:
            addresses:
            - 192.168.2.2/24
            dhcp4: false
            nameservers:
                addresses:
                - 8.8.8.8
    version: 2
   
   ```
   Apply changes:
   
   ```bash
   sudo netplan apply
   ```
4. **Enable IP Forwarding:**
   Edit the sysctl configuration file:
   
   ```bash
   sudo nano /etc/sysctl.conf
   ```
   Uncomment:
   
   ```bash
   net.ipv4.ip_forward=1
   ```
   Apply changes:
   
   ```bash
   sudo sysctl -p
   ```
5. **Install and Configure DHCP: Install the DHCP server:**
   
   ```bash
   sudo apt update
   sudo apt install isc-dhcp-server
   ```
   Configure DHCP:
   
   ```bash
   sudo nano /etc/dhcp/dhcpd.conf
   ```
   Add:
   
   ```bash
   subnet 192.168.2.0 netmask 255.255.255.0 {
     range 192.168.2.50 192.168.2.150;
     option routers 192.168.2.2;
     option domain-name-servers 8.8.8.8, 8.8.4.4;
   }
   ```
   Restart the DHCP service:
   
   ```bash
   sudo service isc-dhcp-server restart
   ```
6. **Set Up NAT for Internet Access: Configure iptables:**
    
   ```bash
   sudo iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE
   sudo apt install iptables-persistent
   sudo netfilter-persistent save
   ```

---

#### **2.2. Kali Linux (Attacker)**
1. **VM settings:**
   - Network Adapter : Host-only (eth0)
   - CPU : 2-4 cores.
   - RAM : Minimum 2GB
   - Disk : 20GB.
2. **Install Kali Linux**
   Use DHCP for Automatic IP assignment (default)
3. **Verify Connection**
   Check IP and Ping the gateway
   
   ```bash
   ip a
   ping 192.168.2.2
   ```
   Or check the network configuration with ip route on Kali Linux. The output should look like:
   
   ```bash
   default via 192.168.2.2 dev eth0
   192.168.2.0/24 dev eth0 proto kernel scope link src 192.168.2.128
   ```
   If not, restart the networking service:
   
   ```bash
   sudo systemctl restart networking
   ```

#### **2.3. Windows 10 (Victim)**
1. **VM setting**:
  - Network Adapter : Host-only
  - CPU : 4 cores.
  - RAM : 4GB.
  - Disk : 40GB.
2. **Install Windows 10** Home or Pro : Use DHCP for automatic IP
3. **Verify Connection**
  Open Command Prompt
  
  ```cmd
  ipconfig
  ```
  Ensure gateway : 192.168.2.2
  If not, you can try:

  ```cmd
  ipconfig /release
  ipconfig /renew
  ```
 *⚠️ Windows blocks ping (ICMP) requests by default.*

**Now you can ping google.com or connect to the Internet from Kali linux or Windows 10 using Ubuntu Server as Gateway**



   


   
