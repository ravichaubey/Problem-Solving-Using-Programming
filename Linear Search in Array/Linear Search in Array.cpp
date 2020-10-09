#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter Array Size ==> ";
    cin>>n;

    int arr[n];
    cout<<"Enter Array Elements ==> ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int num;
    cout<<"Enter Number to Search ==> ";
    cin>>num;

    int flag = 0;
    int i = 0;
    for(i=0;i<n;i++){
        if(arr[i] == num){
            flag = 1;
            break;
        }
    }

    if(flag){
        cout<<"Element is found at position "<<i+1;
    }else{
        cout<<"Element is not found in array";
    }

    return 0;


}