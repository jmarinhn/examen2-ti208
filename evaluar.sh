#!/bin/bash
while true
     do 
       valor1=$(python3 read.py | grep "OFF21" | cut -d " " -f 3 | cut -b 24-28)
       valor2=$(python3 read.py | grep "ON21" | cut -d " " -f 3 | cut -b 24-27)
       echo $valor1
       echo $valor2
        if [ $valor1 == "OFF21" ]
                                    then
                                        echo 0 > /home/josue_marin/estado.txt
            else
                if [ $valor2 == "ON21" ]
				    then
                                       echo 1 > /home/josue_marin/estado.txt
		fi
	   fi
    done