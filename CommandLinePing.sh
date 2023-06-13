#!/bin/bash

echo "Enter IP Addresses (separated by space):"
read -r ipAddress

echo "Enter File Prefix for Storing Raw Results:"
read -r filePrefix

IFS=' '
read -r -a ipArray <<< "$ipAddress"

#adjust to however long the test period needs to be
runtime="5 days"
endTime=$(date -ud "$runtime" +"%s")

for ip in "${ipArray[@]}"; do
    fileName="$filePrefix-$ip.log"
    nohup bash -c "
    while [[ \$(date +"%s") -le $endTime ]]; do
        currentDate=\$(date "+%Y-%m-%d")
        currentTime=\$(date "+%H:%M:%S")
        dateTime=\"\$currentDate \$currentTime\"
       # echo \"Ping Test for $ip Started: \$dateTime\"
        ping -c 10 $ip >> $fileName
        #adjust to however long the test interval should be
        sleep 1800
    done" &
done

echo "Ping tests scheduled for IP addresses: ${ipArray[@]}"
