.

🧪 Setup ARP Poisoning Lab
This guide walks you through setting up a virtual lab environment to simulate ARP poisoning attacks. We'll configure a router using Ubuntu Server, with Kali Linux as the attacker and Windows 10 as the victim. The lab uses Host-Only networking for isolation.

📋 Lab Overview
Machine	Role	Network Adapter	IP Address	Gateway
Ubuntu Server	Router/Gateway	NAT + Host-Only	NAT: Dynamic
Host-Only: 192.168.2.2	192.168.2.2
Kali Linux	Attacker	Host-Only	DHCP-assigned	192.168.2.2
Windows 10	Victim	Host-Only	DHCP-assigned	192.168.2.2

