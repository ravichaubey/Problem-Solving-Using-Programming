#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter Array Size ==> ";
    cin>>n;

    int l = 0, h = n;

    int arr[n];
    cout<<"Enter Array Elements in Sorted Order ==> ";
    for(int i = 0 ; i<n ; i++){
        cin>>arr[i];
    }

    int key;
    cout<<"Enter Key to Search ==> ";
    cin>>key;

    //Binary Search

    while(l <= h){
        int mid = (l+h) / 2;
        if(key == arr[mid]){
            cout<<"Element is Found at Position "<<(mid+1);
            break;
        }else if(key>arr[mid]){
            l = mid+1;
        }else{
            h = mid-1;
        }
    }
    if(l>h){
        cout<<"Element is not found";
    }
    return 0;
}