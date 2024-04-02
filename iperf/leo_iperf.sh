#this script will run iperf3 client mode to collect throughput data from gcp-leo
#crontab is used to run this measurement every 12 hours
#!/bin/bash
currentDateTime=$(date +"%s")

echo "$currentDateTime" >> ~ebmutter42/iperf.log
iperf3 -c 35.207.33.118 >> ~ebmutter42/iperf.log &
sleep 90
sudo pkill -x "iperf3"
echo "------------------------------------" >> ~ebmutter42/iperf.log

