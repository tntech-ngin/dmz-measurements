#!/bin/bash

echo Enter IP Address :

read ipAddress

echo Enter Start Time *ex. 10am Jul 31* :

read startTime

echo Enter filename *pingTest + startTime* :

read file

echo $file

IFS=' '

read -r -a strarr <<< "$ipAddress"

for index in "${!strarr[@]}";
do
        filename=$file$index.log;
        echo $filename;
        echo "$index ${strarr[index]}";
        printf "$val\n"
        ping ${strarr[index]} -c 144 -i 600 >> $filename | at $startTime &
done
