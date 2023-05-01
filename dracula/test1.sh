#!/bin/bash
str=$(tr -c 'a-zA-Z' '\n' <dracula.txt)
str2=$(sort -b <<<$str)
mapfile -t array <<<$str2
var="${array[0]}"
var2=""
var3=$'\n'
count=$((0))
count2=$((0))
for word in ${array[@]}
do
if [[ $var = $word ]]
then
count=$(($count+1))
else 
if [[ $var-ne$var2 ]]
then
arr[$count2]="$count $var$var3"
fi
var=$word
count=$((1))
count2=$(($count2+1))
fi;
done
arr[$count2]="$count $var"
sortarray=$(sort -nr<<<"${arr[@]}")
mapfile -t sortarr <<<$sortarray
for i in {0..9}
do
echo "${sortarr[i]}"
name=$(tr -d '0-9' <<<${sortarr[i]})
touch "${name}_$i"
done 
