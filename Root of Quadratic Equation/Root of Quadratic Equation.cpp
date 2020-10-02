#include<iostream>
#include<math.h>
using namespace std;

int main(){
    float a,b,c;
    cout<<"Assuming Quadratic Equation in the form of ax^2+bx+c";
    cout<<"Please enter a,b and c ==> ";
    cin>>a>>c>>c;
    float d = pow(b,2) - (4*(a*c));
    if(d<0){
        cout<<"Root is Imaginary";
    }else if(d==0){
        float r;
        r = -b / (2*a);
        cout<<"Root of Quadratic Equation is ==> "<<r;

    }else{
        float r1,r2;
        r1 = ((-b) + sqrt(d)) / (2*a);
        r2 = ((-b) - sqrt(d)) / (2*a);
        cout<<"Root of Quadratic Equation is ==> "<<r1<<" and "<<r2;
    }
}
