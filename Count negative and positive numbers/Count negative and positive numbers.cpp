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

    int negativeCount = 0,posCount = 0;

    for(auto x:arr){
        if(x<0){
            negativeCount += 1;
        }else{
            posCount += 1;
        }
    }

    cout<<"Negative and Positive Number Count are ==> "<<negativeCount<<" and "<<posCount;
    return 0;   

}