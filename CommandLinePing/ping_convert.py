import re
import json

def parse_ping_file(file_path):
    ping_transmissions = []
    transmission_number = 1
    timestamp = None
    end_of_transmission_pattern1 = re.compile(r'rtt max/min/avg/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+) ms')
    end_of_transmission_pattern2 = re.compile(r'rtt min/max/avg/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+) ms')


    with open(file_path, 'r') as file:
        ping_data = []

        for line in file:
            # Extract the timestamp
            timestamp_match = re.search(r'Timestamp: (\d+)', line)
            if timestamp_match:
                timestamp_str = timestamp_match.group(1)
                timestamp = int(timestamp_str)

            # Extract relevant information using regular expressions
            match = re.match(r'(\d+) bytes from ([\w\-?.]+) (\(([\d.]+)\))?: seq=(\d+) ttl=(\d+) time=([\d.]+) ms', line)
            match2 = re.match(r'(\d+) bytes from ([\w\-?.]+): icmp_seq=(\d+) ttl=(\d+) time=([\d.]+) ms', line)
            if match:
                ping_info = {
                    'bytes': int(match.group(1)),
                    'ip_address': match.group(3),
                    'sequence': int(match.group(5)),
                    'ttl': int(match.group(6)),
                    'time': float(match.group(7))
                }
                ping_data.append(ping_info)
            if match2:
                ping_info = {
                    'bytes': int(match2.group(1)),
                    'ip_address': match2.group(2),
                    'sequence': int(match2.group(3)),
                    'ttl': int(match2.group(4)),
                    'time': float(match2.group(5))
                }
                ping_data.append(ping_info)
            
            
            packets_pattern = re.compile(r'(\d+) packets transmitted, (\d+) received, (\d+)% packet loss, time (\d+)ms')
            
            packets_match = packets_pattern.search(line)

            if packets_match:
                transmitted = int(packets_match.group(1))
                received = int(packets_match.group(2))
                loss_percentage = int(packets_match.group(3))
                
            # Check for the end of a transmission
            end_of_transmission_match1 = end_of_transmission_pattern1.search(line)
            end_of_transmission_match2 = end_of_transmission_pattern2.search(line)
            if end_of_transmission_match1:
                rtt_max = float(end_of_transmission_match1.group(1))
                rtt_min = float(end_of_transmission_match1.group(2))
                rtt_avg = float(end_of_transmission_match1.group(3))
                rtt_mdev = float(end_of_transmission_match1.group(4))
                
                if ping_data:
                    transmission = {
                        'transmission_number': transmission_number,
                        'timestamp': timestamp,
                        'ping_data': ping_data,
                        'packets_sent': transmitted,
                        'packets_rcvd': received,
                        'loss_percentage': loss_percentage,
                        'rtt_min': rtt_min,
                        'rtt_avg': rtt_avg,
                        'rtt_max': rtt_max,
                        'rtt_mdev': rtt_mdev
                    }
                    ping_transmissions.append(transmission)
                    transmission_number += 1
                    ping_data = []
            if end_of_transmission_match2:
                rtt_min = float(end_of_transmission_match2.group(1))
                rtt_max = float(end_of_transmission_match2.group(2))
                rtt_avg = float(end_of_transmission_match2.group(3))
                rtt_mdev = float(end_of_transmission_match2.group(4))
                
                if ping_data:
                    transmission = {
                        'transmission_number': transmission_number,
                        'timestamp': timestamp,
                        'ping_data': ping_data,
                        'packets_sent': transmitted,
                        'packets_rcvd': received,
                        'loss_percentage': loss_percentage,
                        'rtt_min': rtt_min,
                        'rtt_avg': rtt_avg,
                        'rtt_max': rtt_max,
                        'rtt_mdev': rtt_mdev
                    }
                    ping_transmissions.append(transmission)
                    transmission_number += 1
                    ping_data = []

    return ping_transmissions

# Usage example
file_path = 'lan3-ping.txt'  # Replace with the path to your raw ping file
ping_transmissions = parse_ping_file(file_path)

# Convert ping transmissions to JSON format
json_data = json.dumps(ping_transmissions, indent=4)

# Store JSON data in a file
output_file = 'lan_files/lan3-ping-new.json'  # Replace with the desired output file path
with open(output_file, 'w') as file:
    file.write(json_data)

print(f"Parsed ping data saved to {output_file}.")
