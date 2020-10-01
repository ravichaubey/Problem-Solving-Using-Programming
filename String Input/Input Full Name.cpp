#include<iostream>
using namespace std;

int main(){
    string name;
    cout<<"May I Know Your Name? ";
    getline(cin,name);
    cout<<"Hello Mr. "<<name;
    return 0;
}