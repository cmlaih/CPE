// 11
#include <iostream>
using namespace std;

int main()
{
	int n1, n2;	//數字1，數字2
	while(cin>>n1>>n2)
	{
		int carry=0;	//記錄進位
		int cnt=0;
		if(n1==0&&n2==0) break;
		while(n2>0 || n1>0)
		{
			
			if((n1%10+n2%10+carry)>=10)
			{
				cnt++;
				carry=1;
			}
			else 
                carry=0;
			n1/=10;
			n2/=10;
        }
	
		if(cnt==0) cout<<"No carry operation."<<endl;
		else if(cnt==1) cout<<"1 carry operation."<<endl;
		else cout<<cnt<<" carry operations."<<endl;
    }
	return 0;
} 