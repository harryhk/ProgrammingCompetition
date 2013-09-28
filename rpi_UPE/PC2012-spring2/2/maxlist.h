#include<vector>
using namespace std;

class MaxList{
	
	public:
		
		MaxList(int n, vector<int> q  ):num(n), l(q){}

		int maxsum();

		int num;
		vector<int> l;
};

int MaxList::maxsum(){
	
	int b_idx, e_idx ;
	vector< int  > l_store;

	for(int i=0 ;i!= l.size(); i++){
		
		if( i==0  ){
			l_store.push_back( l[i] );
		}else{

			if( l[i] < l_store.back()  ){
				l_store.push_back(l[i]);
			}else if( l[i] == l_store.back()  ){
				continue;
			}else if(  l[i] > l_store.back() ){
				e_idx= l_store.size();
				int tmp_sum=0;
				int k=0;
				for( k= e_idx -1 ; k>=0  ; k--   ){
					if( l_store[k] < l[i] ){
						tmp_sum += l_store[k];
					}else{
						break;
					}
				}
				vector<int >::iterator iter = l_store.begin();
				if(tmp_sum < l[i]){
					//for(int jj=k+1; jj!=l_store.size(); jj++)
					l_store.erase( iter+ k+1, l_store.end() );
					l_store.push_back(l[i]);
				}
			}
		}
	}

	int s=0;
	for(int i=0; i!=l_store.size(); i++){
		s+=l_store[i];
	}

	
	return s;
}
