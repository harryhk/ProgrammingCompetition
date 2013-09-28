#include<string>

using namespace std;


class Ship{
	
	public:

		Ship(int s1, int  n1,  int x1, string  info1):s(s1), n(n1), x(x1), info(info1){};
		
		double prob();

		int s, n, x;
		string info;
};

double Ship::prob(){
	
	int pos_h=-1;
	int pos_m=-1;
	for(int i=0; i!=info.size(); i++){
		if( info[i] == 'h' ){
			pos_h= i ; 
			break;
		}
	}
	for(int i=0; i!=info.size(); i++){
		if( info[i] == 'm' ){
			pos_m= i ; 
			break;
		}
	}

	int hit_b = pos_h - n +1  > 0 ? pos_h - n +1  : 0 ; 

	int hit_e = pos_h ; 
 

	if( info[x] == 'h'  ){
		return 100; 
	}
	if( info[x] =='m' ){
		return 0; 
	}
	if( info[x] == '*' ){
		if( pos_m == -1  ){
			if( x - pos_h < n && x > pos_h ){
				x = x-n+1;
			}
			return 100.0 *  (x - hit_b +1) /   (hit_e - hit_b +1);
		}else{
			return -1;
		}
	}
}




	



