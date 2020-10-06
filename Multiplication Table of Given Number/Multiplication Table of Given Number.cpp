#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please Enter Number ==> ";
    cin>>num;
    for(int i=1;i<11;i++){
        cout<<num<<"*"<<i<<" = "<<num*i<<endl;
    }
    return 0;
}