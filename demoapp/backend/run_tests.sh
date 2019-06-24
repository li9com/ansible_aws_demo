#!/bin/bash

bin="python test_data.py -ie sender@example.com"
send_to="-a send -ep https://4ihon6g0hf.execute-api.us-east-1.amazonaws.com/latest/exam"


data=(
  "-t 2001 -pe arya.start@winterfell.got -pfn Arya -pln Stark"
  "-t 2002 -pe sansa.stark@winterfell.got -pfn Sansa -pln Stark"
  "-t 2002 -pe ned.stark@winterfell.got -pfn Ned -pln Stark"
  "-t 2003 -pe bran.stark@winterfell.got -pfn Bran -pln Stark"
  "-t 3001 -pe cersei.lannister@casterly.rock.got -pfn Cersei -pln Lannister"
  "-t 3002 -pe tyrion.lannister@casterly.rock.got -pfn Tyrion -pln Lannister"
  "-t 3002 -pe jaime.lannister@casterly.rock.got -pfn Jaime -pln Lannister"
  "-t 3002 -pe tywin.lannister@casterly.rock.got -pfn Tywin -pln Lannister"
)


for i in $(seq $((${#data[@]} - 1))); do
  $bin -e linux ${data[$i-1]} $send_to
done


