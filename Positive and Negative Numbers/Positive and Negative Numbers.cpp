#include<iostream>
using namespace std;

int main(){
    int num;
    cout<<"Please enter number ==> ";
    cin>>num;
    if(num>=0){
        cout<<"Given Number is Positive";
    }else{
        cout<<"Given Number is Negative";
    }
    return 0;
}