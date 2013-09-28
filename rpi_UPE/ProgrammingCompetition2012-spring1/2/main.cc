#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include"ship.h"
using namespace std;

int main (  int argc, char ** argv ){

    if(argc != 3) {
        cerr<< " Usage: ./a.out input output"<<endl;
    }

    ifstream input(argv[1]); 
    ofstream output(argv[2]);

	string line ;
	
	int n_test;
	getline( input, line);

	stringstream str(line);
	str>>n_test;
	
	int s1, n1, x1;
	string info1;
	vector< Ship  > battle;

	while( getline( input, line ) ){
		
		stringstream str1(line);
		str1 >> s1;
		str1 >> n1; 
		str1 >> x1;
		
		getline(input, line);
		stringstream str2(line);
		str2 >> info1; 

		Ship st(s1, n1, x1, info1 );
		
		battle.push_back(st);
	}

	for( int i=0; i!= battle.size(); i++ ){
		output<< battle[i].prob()<<endl;
	}

	return 0 ;
}


