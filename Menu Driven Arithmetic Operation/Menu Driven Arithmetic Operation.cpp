#include<iostream>
using namespace std;

int main(){
    int option,a,b;

    while(1){

    cout<<"<==========Menu===========>";
    cout<<"\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n";

    cin>>option;
    switch (option)
    {
        case 1:
            cin>>a>>b;
            cout<<"Addition ==> "<<a+b;
            break;
        case 2:
            cin>>a>>b;
            cout<<"Subtraction ==> "<<a-b<<endl;
            break;
        case 3:
            cin>>a>>b;
            cout<<"Multiplication ==> "<<a*b<<endl;
            break;
        case 4:
            cin>>a>>b;
            cout<<"Division ==> "<<a/b<<endl;
        case 5:
            return 0;
        default:
            cout<<"Invalid Choice<<"<<endl;
    }

    }

}