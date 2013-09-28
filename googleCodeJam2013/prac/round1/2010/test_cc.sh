#!/bin/bash

for i in 1000000  100000000 1000000000; do 
	echo $i >> pylog 
	sed  "s/HHHH/$i/" test.cc > t.cc
	g++ t.cc

	time ./a.out 2>&1 
done
