#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please enter  number ==> ";
    cin>>num;

    int sumOfFactors = 0;
    for(int i=1;i<=num;i++){
        if(num % i == 0){
            sumOfFactors += i;
        }
    }

    if((2*num) == sumOfFactors){
        cout<<"Yes!! Given Number is Perfect Number";
    }else{
        cout<<"OOPS!! Given Number is not a Perfect Number";
    }

    return 0;

}