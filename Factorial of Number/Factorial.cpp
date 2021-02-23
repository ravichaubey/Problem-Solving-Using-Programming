#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please Enter Number ==> ";
    cin>>num;

    int fact = 1;
    for(int i=num;i>=1;i--){
        fact *= i;
    }

    cout<<"Factorial of Given Number is ==> "<<fact;
    return 0;
}