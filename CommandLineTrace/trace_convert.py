import re
import json

def parse_traceroute_file(file_path):
    traceroutes = []
    transmission_number = 1

    with open(file_path, 'r') as file:
        current_traceroute = None
        timestamp = None
        for line in file:
            # Extract the timestamp
            timestamp_match = re.search(r'Timestamp: (\d+)', line)
            if timestamp_match:
                timestamp_str = timestamp_match.group(1)
                timestamp = int(timestamp_str)

            if line.startswith('traceroute'):
                # Start of a new traceroute
                if current_traceroute:
                    traceroutes.append(current_traceroute)
                    transmission_number += 1
                current_traceroute = {
                    'transmission_number': transmission_number,
                    'timestamp': timestamp,
                    'destination': None,
                    'max_hops': None,
                    'hops': [],
                }
                match = re.match(r'traceroute to (.+) \(([\d.]+)\), (\d+) hops max, (\d+) byte packets', line)
                if match:
                    current_traceroute['destination'] = match.group(2)
                    current_traceroute['max_hops'] = int(match.group(3))
            else:
                # Parse hop information
                match = re.match(r'\s*(\d+)\s+(.+?)\s+\(([\d.]+)\)\s+([\d.]+)\s+ms', line)
                if match:
                    hop_info = {
                        'hop_number': int(match.group(1)),
                        'host': match.group(2),
                        'ip_address': match.group(3),
                        'rtt': float(match.group(4)),
                    }
                    current_traceroute['hops'].append(hop_info)

    if current_traceroute:
        traceroutes.append(current_traceroute)

    return traceroutes

# Usage example
file_path = 'lan3-trace.txt'  # Replace with the path to your raw traceroute file
traceroutes = parse_traceroute_file(file_path)

# Convert traceroutes to JSON format
json_data = json.dumps(traceroutes, indent=4)

# Store JSON data in a file
output_file = 'lan_files/lan3-trace-new.json'  # Replace with the desired output file path
with open(output_file, 'w') as file:
    file.write(json_data)

print(f"Parsed traceroute data saved to {output_file}.")
