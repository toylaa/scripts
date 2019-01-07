#!/usr/bin/env bash
#
#urls look like this 
#https://www.instagram.com/p/BU7SuvAlbcY/

# List all files in CURRENT directory 
#ls -p . | grep -v /$


#Build a list of all files in DATASTORE dir
fileCnt=0
FILES=/var/www/html/bot/DataStore/*
for fnamefull in $FILES
do
  ulink="$(cat "$fnamefull")"
  #
  fnamefull="$(cut -d'/' -f7 <<< "$fnamefull")"
  fname="$(cut -d'.' -f1 <<< "$fnamefull")"
  #
  
  # Take action on each file in directory 
  printf "Processing file $((fileCnt+1)): $fname"
  usn="$(cut -d'-' -f1 <<< "$fname")"
  url="$(cut -d'-' -f2 <<< "$fname")"
  #
  # TBD - Write each combination to URL log file
  printf "\n"
  #USN_array[$fileCnt]=$usn
  printf "usn   :  $usn"
  printf "\n"
  #URL_array[$fileCnt]=$url
  printf "url   :  $url"
  printf "\n"
  #ULINK_array[$fileCnt]=$ulink
  printf "ulink :  $ulink"
  printf "\n"
  python3 spawner.py $usn $url $ulink
  printf "\n"
  #printf "Spawner Called!" 
  # 
  fileCnt=$((fileCnt+1)) 
  #
  echo "-------------------------------------------------"
  #
done
#
#echo 
#echo ${USN_array[@]}
#echo ${URL_array[@]}
#echo ${ULINK_array[@]}

