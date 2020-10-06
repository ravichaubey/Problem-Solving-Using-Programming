#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int n;
    cout<<"Please Enter Number ==> ";
    cin>>n;
    int temp = n;
    int sumOFDigit = 0;

    while(n>0){
        sumOFDigit += pow(n%10,3);
        n /= 10;
    }

    if(temp==sumOFDigit){
        cout<<"Yes, Given Number is Armstrong Number";
    }else{
        cout<<"Given Number is not Armstrong Number";
    }

    return 0;
}