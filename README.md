# dmz-measurements

DMZ_REU_graphs.ipynb file contains all scripts to create graphs using data from all measurement experiments. Ping/Trace graphs are separated by Command Line and RIPE Atlas origins.

CommandLinePing contains all scripts necessary to run ping experiments on Leo, DTN1, and Perfsonar1. Google Cloud capable script is not provided but is very similar to the one for the campus nodes. ping_convert.py converts Leo and GCP data to JSON, and ping_convert_DMZ.py converts DTN1 and Perfsonar1 data to JSON. There is a slight difference in ping output that prevents the first script from converting DMZ data to JSON.

CommandLineTrace contains all scripts necessary to run traceroute experiments on Leo, DTN1, and Perfsonar1. Google Cloud capable script is not provided but is very similar to the one for the campus nodes. trace_convert.py converts data from any of the nodes to JSON.

dataTransfer contains scripts necessary to run data transfer experiments on Leo and DTN1. There is only one script for Leo because students are given root permission and are able to run tcpdump with root. But DTN1 requires the experiment to be split into two scripts, one downloading the data with curl, and the other using tcpdump to capture the data. The data capture script on DTN1 must be run by Dr. Renfro with cronjob. DataTransfer.xlsx contains the exact observations examined by the data transfer results and avg_dt.xlsx contains the daily average of those results. DataTF.ipynb allows a user to read a CSV file downloaded from Wireshark, including exclusively Absolute Time and RTT, to return the average RTT and interpacket delay.

iperf contains scripts necessary to run the client side of iperf experiments on Leo and Perfsonar1. The server is run on Google Cloud and the script is not provided but is similar to the client scripts. convert_iperf.py converts the results from Leo and Perfsonar1 to JSON. 

*** Make sure that filepaths and IP addresses in the scripts are changes to suit your machine setup ***
