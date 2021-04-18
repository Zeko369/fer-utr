#!/bin/bash

raw_count="$(ls -l ./tests | wc -l)"
count="$(($raw_count - 2))"

if [ -z "$1" ]
then
  errors=""
  error_count=0

  for i in $(seq 0 $count)
  do
    dir=$(printf "%0*d\n" 2 $i)
    echo "Test $dir"

    res=`python3 main.py < tests/test$dir/t.ul | diff tests/test$dir/t.iz -`

    if [ "$res" != "" ]
    then
      echo "Fail"
      echo $res

      error_count="$(($error_count + 1))"

      if [ -z "$errors" ]
      then
        errors+="$dir"
      else
        errors+=", $dir"
      fi
    else
      echo "Ok"
    fi
  done

  if [ "$errors" != "" ]
  then
    echo "Errors: $errors"
  fi
  echo "Completed: $(($count-$error_count+1))/$(($count + 1))"
elif [ -z "$2" ]
then
  echo "Test $1"
  res=`python3 main.py < tests/test$1/t.ul | diff tests/test$1/t.iz -`

  if [ "$res" != "" ]
  then
    echo "Fail"
    echo $res
  else
    echo "Ok"
  fi
else
  echo "Test $1"

  echo "My:"
  echo `python3 main.py < tests/test$1/t.ul`

  echo "Their:"
  echo `cat tests/test$1/t.iz`
fi
