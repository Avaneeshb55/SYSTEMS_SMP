#!/bin/bash

# Script : whosonline.sh 
#Description : Displays active TCP/UDP network connections and process info


#Column meaning :

#  Netid              : Protocal type (TCP/UDP)
#  State              : Current connection status 
#  Recv-Q             : Amount of data that has arrived to your machine but not read by the application(In bytes)
#  Send-Q             : Amount of data sent by the application but not confirmed/received by the other side(In bytes)
#  Local address:Port : Your machine's IP address and port 
#  Peer address:Port  : Destination IP address and port
#  Process            : Program/process using the connection


if [ "$EUID" -ne 0 ]; then
echo "Error : This script must be run as root"
echo "Try : sudo ./whosonline.sh"
exit 1
fi
 

echo -e "_________________________________________________________________________________________________________________________________________________________________________________________________________________________\n"
echo -e "                                                                                   ACTIVE INTERNET CONNECTIONS                                                                                        "
echo -e "_________________________________________________________________________________________________________________________________________________________________________________________________________________________\n"
 
ss -tunp 

echo -e "\n========================================================================================================================================================================================================================"
 
