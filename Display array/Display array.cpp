#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter Array Size ==> ";
    cin>>n;

    int a[n];
    cout<<"Enter Array Elements :- ";
    
    for(int i=0;i<n;i++){
        cin>>a[i];
    }

    cout<<"Displaying Array Elements ==> ";

    for(auto x:a){
        cout<<x<<" ";
    }

    return 0;
}