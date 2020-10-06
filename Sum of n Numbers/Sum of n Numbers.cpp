#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Please enter Number ==> ";
    cin>>n;

    int res = 0;
    for(int i=0;i<=n;i++){
        res += i;
    }

    cout<<"Sum is ==> "<<res;
    return 0;
}