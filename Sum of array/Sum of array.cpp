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

    int sum = 0;

    for(auto x:a){
        sum += x;
    }

    cout<<"Sum of Elements of Array is ==> "<<sum;

}