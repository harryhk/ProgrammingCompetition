#include<iostream>
#include<cmath>
using namespace std;

class Laser {

	public:

		Laser( int lt, double r1t, int xt, int ht, int bt  ):l(lt),r1(r1t),x(xt), h(ht), b(bt){};

		int hit(); // return 1 when hit, return 0 if not . 


		int l , x, h,b ;
		double r1;

};


int Laser::hit(){
	
	if( r1 ==0) {
		if( l<= h+b && l>=h-b  ){
			return 1;
		}else{
			return 0;
		}
	}else{
	
		double ab2, ab_n, ab_n2;

		ab_n= x *cos(r1) +(h-l)*sin(r1);
		ab_n2= ab_n * ab_n; 
		
		ab2 = x*x + (h-l)*(h-l);

		if( ab2 - ab_n2 <= b*b  ){
			return 1;
		}else{
			return 0;
		}
	}

}





	

