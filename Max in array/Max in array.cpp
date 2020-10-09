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

    int max = INT32_MIN;

    for(auto x:arr){
        if(x>max){
            max = x;
        }
    }

    cout<<"Maximum is ==> "<<max;

    return 0;

}