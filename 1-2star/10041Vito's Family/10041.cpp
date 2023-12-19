//19
#include<iostream>
#include<vector>
#include <algorithm> 
#include <cmath>
using namespace std;

int main(){
    int n, r, s;

    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>r;
        vector<int> vs;
        for(int j=0; j<r; j++)
        {
            cin>>s;
            vs.push_back(s);
        }
        sort(vs.begin(), vs.end());
        int m = vs[r/2];
        int sum = 0;
        for(int j=0; j<r; j++)
        {
            int d = abs(m-vs[j]);
            sum += d;
        }
        cout<<sum<<endl;
    }
}
