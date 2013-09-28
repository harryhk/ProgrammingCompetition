#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include"Laser.h"
using namespace std;




int main (  int argc, char ** argv ){
	
	if(argc != 3) {
		cerr<< " Usage: ./a.out input output"<<endl;
	}

	ifstream input(argv[1]); 
	ofstream output(argv[2]);
	vector<Laser> testShot;

	int n_test;
	int lt, xt, ht, bt;
	double r1t;

	string line ;

	getline(input, line);
	stringstream line_str(line);

	line_str >> n_test; 


	while( getline( input, line  )  ){
		
		stringstream str_t(line);
		str_t>>lt;
		str_t>>r1t;
		getline(input, line);
		stringstream str_tt(line);
		str_tt >> xt; 
		str_tt >> ht; 
		str_tt >> bt; 

		Laser a( lt, r1t, xt, ht, bt );
		testShot.push_back( a );
		getline(input, line);

	}

	for( int i=0; i!= n_test; i++  ){
		int j=testShot[i].hit();
		if( j==0 ) {
			output << "miss" <<endl;
		}else{
			output << "hit"  <<endl;
		}
	}


	return 0; 
}

