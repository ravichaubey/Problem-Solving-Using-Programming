#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int i = 0;
    int j = 0;
    int best_record = 0,worst_record = 0,best_score,worst_score;
    while(j<n){
        int score;
        cin>>score;
        if(i == 0){
            best_score = score;
            worst_score = score;
            i += 1;
        }
        if(score>best_score){
                best_record += 1;
                best_score = score;
        }else if(score<worst_score){
                worst_record += 1;
                worst_score = score;
        }
        j+=1;

    }
    cout<<best_record<<" "<<worst_record;
    return 0;
}