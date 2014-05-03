#!/bin/bash

for i in 1000000  100000000 1000000000; do 
	echo $i >> pylog 
	time python test.py $i  2>&1 
done
