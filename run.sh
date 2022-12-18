#!/bin/bash

function check_input() {
    if [ ! -f day_$1/input ]; then
        echo "[Day ${1}] Please download your input file and save it to 'day_$1/input'"
        return 1
    fi
}

if [ "$#" -ne 1 ]; then
    check_input "1" && python day_1/main.py
    check_input "2" && python day_2/main.py
    check_input "3" && python day_3/main.py
    check_input "4" && python day_4/main.py
    check_input "5" && python day_5/main.py
    check_input "6" && python day_6/main.py
else
    check_input $1 && python day_$1/main.py
fi