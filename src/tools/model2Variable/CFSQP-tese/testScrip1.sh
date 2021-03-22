#!/bin/bash

path="../s2/"
numScenarios="501"

echo "starting the numerical evaluation, for "$numScenarios "..."

numTasks="10"
xmlFileName=$path"s"$numTasks

i="1"
sleepTime="0"

while [ $i -lt $numScenarios ]
do

     schedtool -F -p 99 -e  	./teste.o 0 3  $i $numTasks $xmlFileName$i".xml" >> result.aux

    i=$[$i+1]
    sleepTime=$[$sleepTime+1]

    if [ 70 -le $sleepTime ]; then
        sleep 5s
        sleepTime="0"
    fi
done

cat result.aux >> resultInt$numTasks.text
rm  result.aux

numTasks="20"
xmlFileName=$path"s"$numTasks

i="1"
sleepTime="0"

while [ $i -lt $numScenarios ]
do
    schedtool -F -p 99 -e  ./teste.o 0 4  $i $numTasks $xmlFileName$i".xml" >> result.aux

    i=$[$i+1]
    sleepTime=$[$sleepTime+1]

    if [ 70 -le $sleepTime ]; then
        sleep 5s
        sleepTime="0"
    fi
done

cat result.aux >> resultInt$numTasks.text
rm  result.aux

numTasks="30"
xmlFileName=$path"s"$numTasks

i="1"
sleepTime="0"

while [ $i -lt $numScenarios ]
do

    schedtool -F -p 99 -e  ./teste.o 0 9  $i $numTasks $xmlFileName$i".xml" >> result.aux

    i=$[$i+1]
    sleepTime=$[$sleepTime+1]

    if [ 70 -le $sleepTime ]; then
        sleep 5s
        sleepTime="0"
    fi
done

cat result.aux >> resultInt$numTasks.text
rm  result.aux

numTasks="50"
xmlFileName=$path"s"$numTasks

i="1"
sleepTime="0"

while [ $i -lt $numScenarios ]
do

    schedtool -F -p 99 -e  ./teste.o 0 9  $i $numTasks $xmlFileName$i".xml" >> result.aux

    i=$[$i+1]
    sleepTime=$[$sleepTime+1]

    if [ 70 -le $sleepTime ]; then
        sleep 5s
        sleepTime="0"
    fi
done

cat result.aux >> resultInt$numTasks.text
rm  result.aux

