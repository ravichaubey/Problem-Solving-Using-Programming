#include<iostream>
using namespace std;

int main(){
    int start,end;
    cout<<"Please enter Working hour in 24 Hour format.\nStart time and End time ==> ";
    cin>>start>>end;

    if(start >= 9 && end<=18){
        cout<<"Working Hour";
    }else{
        cout<<"Not a Working Hour";
    }
    return 0;   
}