#include"graph.h"
#include<fstream>

using namespace std;

int main(int argc, char ** argv){
	

	//Graph graph(input);
	//graph.depthFirstTraversal();
	
	//graph.bellmanFord(0);
	//
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
		
		Graph graph;

        getline(input, line);
        istringstream line_s1(line);
        int n_list;
        vector<int> tmp;
        line_s1 >> n_list;

        for(int j=0; j!=n_list; j++  ){
            string s1, s2;
            int weight;
            
            getline(input, line);
        	istringstream line_s2(line);
			line_s2>>s1>>s2>>weight;
			graph.addEdge(s1, s2, weight);
			
			
        }

	
	

	
	//graph.printGraph();

	return 0;
}
