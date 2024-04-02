#!/bin/bash
#this measurement runs iperf3 in client mode from pf1 to server gcp to collect throughput data
currentDateTime=$(date +"%s")

echo "$currentDateTime" >> ~ebmutter42/iperf.log
iperf3 -c 35.207.33.118 >> ~ebmutter42/iperf.log &
echo "------------------------------------" >> ~ebmutter42/iperf.log

