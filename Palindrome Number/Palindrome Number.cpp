#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Please Enter Number ==> ";
    cin>>n;
    int temp = n;
    int rev = 0;

    while(n>0){
        int rem = n%10;
        rev = (rev * 10) + rem;
        n /= 10;
    }

    if(temp == rev){
        cout<<"Given Number is Palindrome";
    }else{
        cout<<"Given Number is not Palindrome";
    }

    return 0;
}