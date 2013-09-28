#include"graph.h"
#include<string>
#include<sstream>
#include<algorithm>
#include<queue>
#include<list>

using namespace std;

Graph::Graph(istream & input  ){
	// set global traversal time 
	time=0;
	
	string line;
	getline(input, line);
	istringstream line_str(line);
	line_str>>numV;
	//vertex.resize(numV);

	getline(input, line);
	line_str.clear();
	line_str.str(line);
	for(int i=0; i!=numV; i++){
		string tmp;
		line_str>>tmp;
		GVertex a(tmp);
		vertex.push_back(a);
		v_id.push_back(tmp);
	}

	vector<string>::iterator it;

	for(int i=0; i!=numV; i++){
		string tmp;
		getline(input, line);
		line_str.clear();
		line_str.str(line);
		line_str>>vertex[i].id;
		int numEdges;
		line_str>> numEdges; 
		//vertex[i].edges.resize(numEdges);
		for(int j=0; j!= numEdges; j++  ){
			
			string tmp;
			int w;

			line_str>>tmp>>w;
			
			it = find(v_id.begin(), v_id.end(), tmp );

			GEdge ed(it-v_id.begin(), w  );
			vertex[i].edges.push_back(ed);
		}
	}
}

int isNewVertex(Graph & g ,   string x){
	vector<string>::iterator it; 
	it= find( g.v_id.begin() , g.v_id.end(), x  );
	if( it == g.v_id.end()  ){
		return -1;
	}else{
		return it - g.v_id.begin();
	}
}
	

void Graph::addEdge(string x, string y, int weight){
	if(  isNewVertex( *this,   x ) == -1   ){
		v_id.push_back(x);
		vertex.push_back( GVertex(x)  );
	}

	if(  isNewVertex( *this,   y ) == -1   ){
		v_id.push_back(x);
		vertex.push_back( GVertex(x)  );
	}

	int idx_x = isNewVertex( *this, x );
	int idx_y = isNewVertex( *this, y );



}
void Graph::printGraph(){
	for(int i=0; i!=numV; i++){
		cout<<vertex[i].id<<": ";
		for(int j=0; j!=vertex[i].edges.size(); j++){
			cout<<vertex[  vertex[i].edges[j].child ].id
				<<vertex[i].edges[j].weight;
		}
		cout<<endl;
	}
}

void Graph::depthFirstTraversal(){
	for(int i=0; i!=vertex.size(); i++){
		vertex[i].colour=White;
		vertex[i].parent=-1;
	}

	for(int i=0; i!=vertex.size(); i++){
		if( vertex[i].colour==White ) dfTraverse(i);
	}
}


void Graph::dfTraverse(int id){
	cout << v_id[id];

	vertex[id].colour=Gray;
	vertex[id].discover= time;
	++time;
	for(int i=0; i!=vertex[id].edges.size(); i++){
		int edgeIdx= vertex[id].edges[i].child;
		if( vertex[ edgeIdx ].colour == White ) {
			vertex[ edgeIdx ].parent = id;
			dfTraverse( edgeIdx );
		}
	}
	vertex[id].colour=Black;
	vertex[id].finish=time;
	time++;
}

void Graph::followPath(int id){
	if( vertex[id].parent != -1   ){
		followPath( vertex[id].parent );
		cout<<vertex[id].id;
	}
}




void Graph::bfTraverse(int id){
	queue<int> q;
	
	for(int i=0; i!=vertex.size(); i++){
		vertex[i].colour=White;
		vertex[i].parent= -1; 
	}

	q.push(id);
	vertex[id].colour=Gray;

	while( !q.empty() ){
		int idx= q.front();
		cout<<vertex[idx].id<<endl;
		q.pop();
		for( int i=0; i!=vertex[idx].edges.size(); i++ ){
			int k=vertex[idx].edges[i].child;
			if( vertex[k].colour==White  ){
				vertex[k].colour=Gray;
				vertex[k].parent=idx;
				q.push(k);
			}
		}
		vertex[idx].colour=Black;
	}
}


bool isLess( GVertex  i, GVertex   j  ){
	return i.cost <= j.cost;
}

void Graph::dijkstra(int id){
	list<GVertex> q;

	for(int i=0 ;i!=vertex.size(); i++){
		if(i==id){
			vertex[i].cost=0;
			vertex[i].parent=-1;
		}else{
			vertex[i].cost=MaxCost;
			vertex[i].parent= -1;
		}
	}

	for(int i=0; i!=vertex[id].edges.size(); i++){
		int k = vertex[id].edges[i].child;
		vertex[k].cost = vertex[id].edges[i].weight;
		vertex[k].parent = id ;
	}

	//GVertex * ptr;

	for(int i=0; i!= vertex.size(); i++   ){
		q.push_back(  vertex[i] );
	}

	//sort(q.begin(), q.end(), isLess);
	q.sort(isLess);

#if 1
	for(list<GVertex>::iterator it=q.begin(); it !=q.end(); it++){
		cout<<it->id<<" "<<it->cost<<endl;
	}
#endif

	while(!q.empty()){
		
		GVertex  it = q.front();
		q.pop_front();
		if(it.cost == 100)
		{ 
			break ;
		}

		for( int i=0; i!= it.edges.size(); i++  ){
			int k=it.edges[i].child;
			if( it.cost + it.edges[i].weight < vertex[k].cost  ){
				vertex[k].cost = it.cost + it.edges[i].weight;
				vector<string>::iterator tmp_it = find( v_id.begin(), v_id.end(), it.id  );
				vertex[k].parent = tmp_it - v_id.begin();
				// update element in list
				for(list<GVertex>::iterator iter=q.begin(); iter!=q.end(); iter++){
					if(iter->id == v_id[k]){
						iter->cost=it.cost + it.edges[i].weight;
					}
				}


			}
		}
		//sort( q.begin(), q.end(), isLess  );
		q.sort(isLess);
	
	
#if 1
	for(list<GVertex>::iterator it=q.begin(); it !=q.end(); it++){
		cout<<"DEbug: "<<  it->id<<" "<<it->cost<<endl;
	}
#endif
	
	}

	// print path to each vertex
	//
	for(int i=0; i!=vertex.size(); i++){
		cout<<"Cost to "<<vertex[i].id <<":"<<vertex[i].cost;
		followPath(i);
		cout<<endl;
	}
}



void Graph::bellmanFord(int id){
	
//	vector<GVertex *> q;
	
	// initialize q. 
    for(int i=0 ;i!=vertex.size(); i++){
        if(i==id){
            vertex[i].cost=0;
            vertex[i].parent=-1;
        }else{
            vertex[i].cost=MaxCost;
            vertex[i].parent= -1;
        }
    }

//	for(int i=0; i!=vertex.size(); i++){
//		q.push_back(&vertex[i]);
//	}

#if 0
	for(int i=0; i!=q.size(); i++){
		cout<<q[i]->id <<"  "<<q[i]->cost  <<endl;
	}

#endif 


	for( int pass=1 ; pass< numV ; pass++ ){
		for(int i=0; i!=numV; i++) {
			if( vertex[i].cost != MaxCost  ) {
				for(int j=0; j!=vertex[i].edges.size(); j++  ){
					int k=vertex[i].edges[j].child;
					if( vertex[i].cost + vertex[i].edges[j].weight < vertex[k].cost   ){
						vertex[k].cost = vertex[i].cost + vertex[i].edges[j].weight;
						vertex[k].parent = i;
					}
				}
			}
		}
	}

	// final pass test 
	//
	for(int i=0; i!=numV; i++){
		
		if( vertex[i].cost != MaxCost  ){
			for(int j=0; j!=vertex[i].edges.size(); j++  ){
				int k=vertex[i].edges[j].child;
				if( vertex[i].cost + vertex[i].edges[j].weight < vertex[k].cost   ){
					cout<<"negative weight cycle"<<endl;
					return ;
				}
			}
		}

	}

	// print path to each vertex
	//
	for(int i=0; i!=vertex.size(); i++){
		cout<<"Cost to "<<vertex[i].id <<":"<<vertex[i].cost;
		followPath(i);
		cout<<endl;
	}




}

bool isLessPtr(GVertex * i, GVertex * j){
	return i->cost <= j->cost;
}

void Graph::prim(int id){
	
	list<GVertex *> q;

    for(int i=0 ;i!=vertex.size(); i++){
        if(i==id){
            vertex[i].cost=0;
            vertex[i].parent=-1;
        }else{
            vertex[i].cost=MaxCost;
            vertex[i].parent= -1;
        }
    }

    for(int i=0; i!=vertex[id].edges.size(); i++){
        int k = vertex[id].edges[i].child;
        vertex[k].cost = vertex[id].edges[i].weight;
        vertex[k].parent = id ;
    }
	
	q.sort(isLessPtr );
//	q.push_back(&vertex[id]);

	while(! q.empty() ){
		
		GVertex * tmp = q.front();
		q.pop_front();

		for(int i=0; i!=tmp->edges.size(); i++){
			int k= tmp->edges[i].child;
			if(tmp->cost + tmp->edges[i].weight < vertex[k].cost   ){
				vertex[k].cost = tmp->cost + tmp->edges[i].weight;
			    vector<string>::iterator tmp_it = find( v_id.begin(), v_id.end(), tmp->id  );

				
				vertex[k].parent = tmp_id - v_id.begin();
			}
		}

		q.sort(isLessPtr);
	}

	// print 
	//
	
			













