#!/bin/bash

for i in {1..20}
do
  dir=$(printf "%0*d\n" 2 $i)
  echo "Test $dir"

  res=`python3 main.py < tests/test$dir/test.a | diff tests/test$dir/test.b -`

  if [ "$res" != "" ]
  then
    echo "Fail"
    echo $res
  else
    echo "Ok"
  fi
done
