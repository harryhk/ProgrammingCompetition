#! /usr/bin/python
from decimal import *
import sys

f = open( sys.argv[1] , "r" )
o = open( "ctest_output", "w" )

for case in range( int( f.readline() ) ):
	
	n = f.readline() 
	number = str( ( ( Decimal( "3" ) + Decimal( "5" ).sqrt() ) ** Decimal( n ) ) % Decimal( "1000" ) ).split( "." )[0]

	if len( number ) == 1:
		number = "0" + number

	if len( number ) == 2:
		number = "0" + number
	print number
	o.write( "Case #" + str( case + 1 ) + ": " + str( number ) + "\n" )
