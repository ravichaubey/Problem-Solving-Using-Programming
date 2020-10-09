#include<iostream>
using namespace std;

int main(){
    
    int r,c;
    cout<<"Enter number of Row and Column ==> ";
    cin>>r>>c;


    for(int i = 0;i<r;i++){
        for(int j = 0;j<c;j++){
            if(i>=j){
                cout<<"*"<<"\t";
            }
        }
        cout<<endl;
    }

    return 0;

}