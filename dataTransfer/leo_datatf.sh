#!/bin/bash

#this is the data transfer measurement run from Leo
#tcpdump captures packets as 5 files are downloaded from the internet
#crontab is used to run every 4 hours
#results are stored in .pcap files that must be transferred to local machine and analyzed with Wireshark
#scp works best for the file transfer (more details in lab notebook)

currentDateTime=$(date "+%Y-%m-%d_%H-%M-%S")
# Start tcpdump to capture packets (adjust interface and ports as needed)
sudo tcpdump -s 96 -i eno2 '(host mirror.umd.edu or host ftp.usf.edu or host mirrors.maine.edu or host mirrors.mit.edu or host archive.linux.duke.edu) and (port 80 or 443)' -w /home/ebmutter42/tcp_${currentDateTime}.pcap &
    # Start downloading files using curl
sudo -s curl https://mirror.umd.edu/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null 
sudo -s curl http://ftp.usf.edu/pub/fedora/linux/releases/39/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-39-1.5.iso > /dev/null 
sudo -s curl http://mirrors.maine.edu/Fedora/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null 
sudo -s curl https://mirrors.mit.edu/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null 
sudo -s curl https://archive.linux.duke.edu/fedora/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null 

    # Sleep 10 seconds to allow all files time to download (important step, tcpdump does not capture packets without this sleep)
sleep 10
    # Kill tcpdump instances until next interval
sudo pkill -x "tcpdump"
