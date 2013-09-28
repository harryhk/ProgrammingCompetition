#include<fstream>
#include<string>
#include<sstream>
#include<iostream>
#include"maxlist.h"

using namespace std;

int main(int argc, char ** argv){
	if(argc!=3){
		cerr<<"Usage ./a.out input output"<<endl;
		return -1;
	}

	ifstream input(argv[1]);
	ofstream output(argv[2]);

	string line;

	getline(input, line);
	
	istringstream line_str(line);

	int n_test;

	line_str>> n_test;

	for( int i=0; i!= n_test ; i++  ){
		
		getline(input, line);
		istringstream line_s1(line);
		int n_list;
		vector<int> tmp;
		line_s1 >> n_list;
		getline(input, line);
		
		istringstream line_s2(line);
		for(int j=0; j!=n_list; j++  ){
			int s;
			line_s2 >> s;
			tmp.push_back(s);
		}

		MaxList list_test(n_list, tmp);

			

		cout<< list_test.maxsum()<<endl;
	}

	return 0;
}

