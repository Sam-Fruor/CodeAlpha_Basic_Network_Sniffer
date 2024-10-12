from scapy.all import sniff

# Callback function to process each captured packet
def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet['IP'].proto

        # Protocol Identification
        if protocol == 6:  # TCP
            protocol_name = "TCP"
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
        elif protocol == 1:  # ICMP
            protocol_name = "ICMP"
        else:
            protocol_name = "Other"
        
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol_name}")
    else:
        print("Non-IP packet captured")

# Sniff packets from the network (interface "eth0" or change to "wlan0" for Wi-Fi)
def start_sniffing(interface="eth0"):
    print(f"Sniffing on {interface}... Press Ctrl+C to stop.")
    sniff(iface=interface, prn=process_packet, store=False)

# Start capturing packets
if __name__ == "__main__":
    interface = "eth0"
    start_sniffing(interface)
