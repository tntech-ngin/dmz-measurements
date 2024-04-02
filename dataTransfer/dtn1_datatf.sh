#this is part one of running the data transfer measurements on DTN1. 
#due to the security measures of the DMZ disallowing students to be root, this must be set up in cron by Dr. Renfro
YYYYMMDDHHMM=$(date +%Y%m%d-%H%M)
timeout --kill-after=1 900 tcpdump -s 96 -B 10240 -i p1p1 \
  '(host mirror.umd.edu or host ftp.usf.edu or host mirrors.maine.edu or host mirrors.mit.edu or host archive.linux.duke.edu) and (port 80 or port 443)' \
  -w ~ebmutter42/${YYYYMMDDHHMM}.pcap
chown ebmutter42 ~ebmutter42/${YYYYMMDDHHMM}.pcap
