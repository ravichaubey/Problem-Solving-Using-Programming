#include<iostream>
using namespace std;

int main(){
    
    int n;
    cout<<"Enter number of Row ==> ";
    cin>>n;

    int count = 1;

    for(int i = 0;i<n;i++){
        for(int j = 0;j<4;j++){
            cout<<count<<"\t";
            count += 1;
        }
        cout<<endl;
    }

    return 0;

}