#include<iostream>
using namespace std;

int main(){
    int year;
    cout<<"Please Enter Year ==> ";
    cin>>year;

    if((year % 4 == 0) || (year % 100 == 0 && year % 400 == 0)){
        cout<<"Given Year is Leap Year";
    }else{
        cout<<"Given year is not Leap Year";
    }
    return 0;
}