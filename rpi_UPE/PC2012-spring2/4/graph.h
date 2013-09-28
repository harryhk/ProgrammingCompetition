#include<vector>
#include<iostream>
using namespace std;

#define MaxVertex 10 
#define MaxCost 10000
enum {White, Gray, Black};

class GEdge{
	public:
		GEdge(){};
		GEdge(int c, int w ): child(c), weight(w){};
		int child, weight;
};



class GVertex{
	public:
		GVertex(){};
		GVertex(string s):id(s){};
		string id;
		int colour, parent, cost, discover, finish, inDegree;
		vector<GEdge> edges;
};

class Graph{
	public:
		Graph(istream & input);
		Graph(){};
	    void addEdge(string x, string y, int w );	
		void printGraph();
		void depthFirstTraversal();
		void dfTraverse(int id);
		void followPath(int id);
		void bfTraverse(int id);
		void dijkstra(int id ); 
		void bellmanFord(int id);
		void prim(int id);

		int numV;
		int time; 
		vector<GVertex> vertex;
		vector<string>  v_id;
};
