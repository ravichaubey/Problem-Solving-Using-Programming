#include<iostream>
using namespace std;

int main(){
    int a,b,c;
    cout<<"Enter Three Numbers == > ";
    cin>>a>>b>>c;
    if(a>b && a>c){
        cout<<"First Number is greater";
    }else
    {
        if(b>c){
            cout<<"Second Number is Greater";
        }else{
            cout<<"Third Number is Greater";
        }
    }
    return 0;
}