#this is part 2 of data transfer on DTN1
#this should be set up in cron to run every 4 hours at minute 1 instead of minute 0 since the packet capture is performed in a separate file
  # Start downloading files using curl
    curl  https://mirror.umd.edu/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null
    curl  http://ftp.usf.edu/pub/fedora/linux/releases/39/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-39-1.5.iso > /dev/null
    curl  http://mirrors.maine.edu/Fedora/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null
    curl  https://mirrors.mit.edu/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null
    curl  https://archive.linux.duke.edu/fedora/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso > /dev/null


