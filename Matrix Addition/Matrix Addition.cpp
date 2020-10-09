#include<iostream>
using namespace std;

int main(){
    
    int r,c;
    cout<<"Enter number of row and column ==> ";
    cin>>r>>c;

    int mat1[r][r],mat2[r][c],res[r][c];

    cout<<"Enter Element of Matrix 1 ==> ";
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>mat1[i][j];
        }
    }

    cout<<"Enter Element of Matrix 2 ==> ";
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>mat2[i][j];
        }
    }

    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            res[i][j] = mat1[i][j] + mat2[i][j];
        }
    }

    cout<<"Resulting matrix is ==>\n";

    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<res[i][j]<<"\t";
        }
        cout<<endl;
    }

    return 0;    

}