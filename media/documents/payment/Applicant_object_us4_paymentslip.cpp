#include<bits/stdc++.h>
using namespace std;
#define f(i,low,up) for(int i=low;i<up;i++)
#define f1(i,low,up) for(int i=low;i<=up;i++)
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
#define mod 1000000007
int n;
int get(int r,int l,int h,vector<int>*v)
{
	int cnt=0;
	queue<pair<int,int> >q;
	int visit[n];
	memset(visit,0,sizeof(visit));
	visit[r]=1;
	
	if(l==0)
	cnt++;
	
	q.push(mk(r,0));
	
	while(!q.empty())
	{
		int t=q.front().F;
		int lev=q.front().S;
		q.pop();
		
		f(i,0,v[t].size())
		{
		   	if(visit[v[t][i]]==0)
		   	{
		   	   visit[v[t][i]]=1;
		   	   
		   	   if(lev+1>=l&&lev+1<=h)
		   	   cnt++;
		   	   
			   if(lev<h-1)
			   {
			       q.push(mk(v[t][i],lev+1));	
			   }	  	
		    }
		}
	}
	
	return cnt;
	
}

int main()
{
     int q;
	 
	 cin>>n>>q;
	 vector<int>v[n+1];
	 f(i,0,n-1)
	 {
	 	int x,y;
	 	cin>>x>>y;
	 	v[x].pb(y);
	 	v[y].pb(x);
	 }
	 
	 while(q--)
	 {
	 	int r,l,h;
	 	cin>>r>>l>>h;
	 	cout<<get(r,l,h,v)<<"\n";
	 	
	 	
	 }
	   
    

    return 0;
}

