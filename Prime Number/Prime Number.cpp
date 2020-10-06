#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please enter  number ==> ";
    cin>>num;
    int flag = 1;
    for(int i = 2;i<num;i++){
        if(num % i == 0){
            flag = 0;
        }
    }

    if(flag == 0){
        cout<<"Give number is not a prime number";
    }else{
        cout<<"Give number is prime number";
    }

    return 0;

}