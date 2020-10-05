#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please Enter Number ==> ";
    cin>>num;

    if(num%2 == 0){
        cout<<"Given Number is Even";
    }else{
        cout<<"Given Number is Odd";
    }
    return 0;

}