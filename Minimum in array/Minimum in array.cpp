#include<iostream>
using namespace std;

int main(){

    int n;
    cout<<"Enter Size of Array ==> ";
    cin>>n;
    int arr[n];
    cout<<"Enter Array Elements ==> ";

    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int min = INT32_MAX;

    for(auto x:arr){
        if(x<min){
            min = x;
        }
    }

    cout<<"Minimum is ==> "<<min;

    return 0;

}