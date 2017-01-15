#!/bin/bash

for i in {20..40}
do
    total=0
    for j in {1..7}  # усреднение из 7 запусков
    do
        cmd="$(echo -e "12\n$i" | python $1)"
        # 12 - время работы магазина в часах
        cur="$(echo "$cmd" | grep "Время ожидания составило" | sed 's/[^0-9]//g')"
        total=$((total + cur))
    done
    echo $((total / 7))
done
