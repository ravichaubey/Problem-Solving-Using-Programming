#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Please Enter Number ==> ";
    cin>>n;
    int rev = 0;

    while(n>0){
        int rem = n%10;
        rev = (rev * 10) + rem;
        n /= 10;
    }

    cout<<"Reverse of Number is ==> "<<rev;
    return 0;
}