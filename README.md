# CodeAlpha_Basic_Network_Sniffer
# Python Network Sniffer

This project implements a simple network sniffer in Python using the Scapy library. The sniffer captures and analyzes network traffic, providing basic information about IP packets.

## Features

- Captures network packets in real-time
- Identifies IP, TCP, UDP, and ICMP protocols
- Displays source and destination IP addresses for each packet
- Easy to run and customize

## Code
The full source code for this network sniffer is provided in the attached Network_Sniffer.txt file. You can find the implementation details there.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the Scapy library using pip:

   ```
   pip install scapy
   ```

3. Clone this repository or download the script.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with sudo privileges (required for packet capturing):

   ```
   sudo python3 network_sniffer.py
   ```

   Note: Replace `python3` with `python` if your system uses `python` for Python 3.

4. By default, the script will sniff on the "eth0" interface. To use a different interface (e.g., "wlan0" for Wi-Fi), modify the `interface` variable in the script.

5. Press Ctrl+C to stop the sniffer.

## How It Works

1. The script uses Scapy's `sniff` function to capture network packets.
2. Each captured packet is processed by the `process_packet` function.
3. If the packet has an IP layer, the script extracts the source and destination IP addresses.
4. The script identifies the protocol (TCP, UDP, ICMP, or Other) based on the protocol number.
5. Information about each packet is printed to the console.

## Customization

- To capture packets on a different network interface, change the `interface` variable in the `if __name__ == "__main__":` block.
- Modify the `process_packet` function to extract additional information or perform more detailed analysis.
- Add additional protocol identifications by extending the if-elif structure in the `process_packet` function.

## Security and Legal Considerations

This tool is intended for educational and network diagnostics purposes only. Ensure you have permission to capture and analyze network traffic on the target network. Unauthorized packet sniffing may be illegal in some jurisdictions.

## Contributing

Contributions to improve the sniffer are welcome. Please fork the repository and submit a pull request with your changes.

## Disclaimer

This tool is provided as-is, without any warranties. The authors are not responsible for any misuse or damage caused by this tool.
