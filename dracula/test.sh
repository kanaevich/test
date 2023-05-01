#!/bin/bash
str=$(tr -c 'a-zA-Z' '\n' <dracula.txt)
str2=$(sort -b <<<$str)
mapfile -t array <<<$str2
var="${array[0]}"
var2=""
count=$((0))
for word in ${array[@]}
do
if [[ $var = $word ]]
then
count=$(($count+1))
else 
if [[ $var-ne$var2 ]]
then
echo "$count $var"
fi
var=$word
count=$((1))
fi;
done
echo "$count $var"
