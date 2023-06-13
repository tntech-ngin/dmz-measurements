
#!/bin/bash

echo "Enter IP Addresses:"
read -r ipAddress

echo "Enter Start Time (e.g., '10:00 AM'):"
read -r startTime

echo "Enter Filename (e.g., traceTest):"
read -r fileName
#adjust for test period
runtime="5 days"
endTime=$(date -ud "$runtime" +%s)

IFS=' '

read -r -a strarr <<< "$ipAddress"

while [[ $(date +%s) -le "$endTime" ]]; do
    currentDate=$(date "+%Y-%m-%d")
    currentTime=$(date "+%H:%M:%S")
    dateTime="$currentDate $currentTime"
    echo "Traceroute Test Started: $dateTime"
    for index in "${!strarr[@]}"; do
        filename="$fileName$index.log"
       # echo "Traceroute to ${strarr[index]} >> $filename"
        {
            traceroute -M icmp -q 1 "${strarr[index]}"
        } >>"$filename" 2>&1
    done
    #adjust for test interval
    sleep 1800
done &  # Run the script in the background



