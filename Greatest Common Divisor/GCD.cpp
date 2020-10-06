#include<iostream>
using namespace  std;

int main(){
    int m,n;
    cout<<"Please Enter m and n ==> ";
    cin>>m>>n;
    while(1){
        if(m == n){
            cout<<"GCD is ==> "<<m;
            break;
        }else if(m>n){
            m = m-n;
        }else
        {
            n = n-m;
        }
        
    }
    return 0;
}