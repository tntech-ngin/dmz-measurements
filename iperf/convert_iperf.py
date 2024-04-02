import re
import json

def parse_iperf_file(file_path):
    iperfs = []
    transmission_number = 1

    with open(file_path, 'r') as file:
        current_iperf = None
        timestamp = None
        for line in file:
            # Extract the timestamp
            timestamp_match = re.search(r'(\d{10})', line)
            if timestamp_match:
                timestamp_str = timestamp_match.group(1)
                timestamp = int(timestamp_str)

            if line.startswith('Connecting to host'):
                # Start of a new traceroute
                if current_iperf:
                    iperfs.append(current_iperf)
                    transmission_number += 1
                current_iperf = {
                    'transmission_number': transmission_number,
                    'timestamp': timestamp,
                    'server': None,
                    'server_port': None,
                    'client': '149.149.2.70',
                    'client_port': None,
                    'top': [],
                    'sender':[],
                    'receiver': []
                }
                match = re.match(r'Connecting to host ([\d.]+), port (\d+)', line)
                if match:
                    current_iperf['server'] = match.group(1)
                    current_iperf['server_port'] = int(match.group(2))
            else:
                # Parse hop information
                match = re.match(r'\[  5\][\s]+(\d+\.\d+)-(\d+\.\d+)[\s]+sec[\s]+(\d+\.?\d+?) ([a-zA-Z]+)ytes[\s]+(\d+\.?\d+?) ([a-zA-Z]+)its\/sec[\s]+(\d+)[\s]+(\d+\.?\d+?) ([a-zA-Z]+)ytes', line)
                sender_match = re.match(r'\[  5\][\s]+(\d+\.\d+)-(\d+\.\d+)[\s]+sec[\s]+(\d+\.?\d+?) ([a-zA-Z]+)ytes[\s]+(\d+\.?\d+?) ([a-zA-Z]+)its\/sec[\s]+(\d+)?[\s]+sender', line)
                receiver_match = re.match(r'\[  5\][\s]+(\d+\.\d+)-(\d+\.\d+)[\s]+sec[\s]+(\d+\.?\d+?) ([a-zA-Z]+)ytes[\s]+(\d+\.?\d+?) ([a-zA-Z]+)its\/sec[\s]+receiver', line)

                if match:
                    iperf_info = {
                        'interval_start': float(match.group(1)),
                        'interval_end': float(match.group(2)),
                        'transfer': float(match.group(3)),
                        'transfer_class': (match.group(4)) + "ytes",
                        'bitrate': float(match.group(5)),
                        'bitrate_class': (match.group(6)) + "its/sec",
                        'retr' : float(match.group(7)),
                        'cwnd' : float(match.group(8)),
                        'cwnd_class' : (match.group(9)) + "ytes"
                    }
                    current_iperf['top'].append(iperf_info)

                elif sender_match:
                    iperf_info = {
                        'interval_start': float(sender_match.group(1)),
                        'interval_end': float(sender_match.group(2)),
                        'transfer': float(sender_match.group(3)),
                        'transfer_class' : (sender_match.group(4)) + "ytes",
                        'bitrate': float(sender_match.group(5)),
                        'bitrate_class' : (sender_match.group(6)) + "its/sec",
                        'retr' : int(sender_match.group(7)),
                    }
                    current_iperf['sender'].append(iperf_info)

                elif receiver_match:
                    iperf_info = {
                        'interval_start': float(receiver_match.group(1)),
                        'interval_end': float(receiver_match.group(2)),
                        'transfer': float(receiver_match.group(3)),
                        'transfer_class' : (receiver_match.group(4)) + "ytes",
                        'bitrate': float(receiver_match.group(5)),
                        'bitrate_class' : (receiver_match.group(6)) + "its/sec"
                    }
                    current_iperf['receiver'].append(iperf_info)
                
                # match2 = re.match(r'\[  6\]   (\d+\.\d+)-(\d+\.\d+)   sec   (\d+) MBytes  (\d+\.\d+) Mbits\/sec  (\d+)?   sender|reciever', line)
                # if match2:
                #     iperf_info = {
                #         'interval_start': float(match2.group(1)),
                #         'interval_end': float(match2.group(2)),
                #         'transfer': int(match2.group(3)),
                #         'bitrate': float(match2.group(4)),
                #         'retr' : int(match2.group(5)),
                #         'state' : (match2.group(6))
                #     }
                #     current_iperf['bottom'].append(iperf_info)
            
            
            

    if current_iperf:
        iperfs.append(current_iperf)

    return iperfs

# Usage example
file_path = '/Users/emily/Desktop/DMZ_REU/pf1_iperf.log'  # Replace with the path to your raw traceroute file
iperfs = parse_iperf_file(file_path)

# Convert traceroutes to JSON format
json_data = json.dumps(iperfs, indent=4)

# Store JSON data in a file
output_file = '/Users/emily/Desktop/DMZ_REU/pf1_iperf.json'  # Replace with the desired output file path
with open(output_file, 'w') as file:
    file.write(json_data)

print(f"Parsed traceroute data saved to {output_file}.")

