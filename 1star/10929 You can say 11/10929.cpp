//21
#include<iostream>

using namespace std;

int main()
{
	string s;
	long long int sum;
	while(cin>>s)
	{
		if(s=="0") break; //記得要用s字串來判斷，不要用數字值0，避免'000000000'也會中止 
		sum=0;
		// {奇數位數字和-偶數位數字和} or {奇數位數字和-偶數位數字和}
		for(int i=0; i<s.length(); i++)
		{
			if(i%2==0) sum+=(int)(s[i]-'0');
			else  sum-=(int)(s[i]-'0');
		}
		//判斷是否為11倍數
		if(sum%11==0)
		{
			cout<<s<<" is a multiple of 11."<<endl;
		}
		else
		{
			cout<<s<<" is not a multiple of 11."<<endl;
		}
	}
}