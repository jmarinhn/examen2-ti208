#!/bin/bash
while true
     do 
       valor1=$(python3 lectura.py | grep "OFF21" | cut -d " " -f 3 | cut -b 24-28)
       valor2=$(python3 lectura.py | grep "ON21" | cut -d " " -f 3 | cut -b 24-27)
       echo $valor1
       echo $valor2
        if [[ $valor1 == "OFF21" && $valor2 == "" ]]
            then
                echo 0 > estado.txt
        elif [[ $valor2 == "ON21" && $valor1 == "" ]]
            then
                echo 1 > estado.txt
        fi
    done
