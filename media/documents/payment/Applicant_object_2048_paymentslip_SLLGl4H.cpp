#include<bits/stdc++.h>
using namespace std;
#define f(i,low,up) for(int i=low;i<up;i++)
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
#define mod 1000000007

void sieve()
{
	memset(prime,true,sizeof(prime));
	prime[1]=prime[0]=false;
	f1(i,2,200)
	{
		if(prime[i])
		{
		 prime[i]=true;
		 prime_list.pb(i);
		 
		 for(int j=2*i;j<=200;j=j+i)
		 prime[j]=false;
	    }
	}
	
}


int main()
{
	
	
	return 0;
}
