#include<bits/stdc++.h>
using namespace std;

vector<int>input;

void generate()
{
	srand(time(0));
	int n;
	n=rand()%15+15;
	cout<<"number of values are "<<n<<"\n";
	

	
	for(int i=0;i<n;i++)
	{
		int val=rand()%100+9;
		input.push_back(val);
	}
	
	sort(input.begin(),input.end());
	
	
	
}

int  main()
{
	generate();
	
	int bincnt;
	srand(time(0));
	bincnt=rand()%4+3;
	cout<<"No of bins divided "<<bincnt<<"\n";
	
	vector<int>smtmean(input);
	int sz=input.size();
	
	ofstream fout("binout.txt");
	
	for(int i=0;i<sz;i++)
	{
		fout<<input[i]<<" ";
	}
	fout<<"\n\n\n\n";
	
	for(int i=0;i<bincnt;i++)
	{
		int low=(i*(sz/bincnt));
		int high=((i+1)*(sz/bincnt));
		if(i==bincnt-1)
		 high=sz;
		float mean=0; 
		for(int j=low;j<high;j++)
		{
		   	mean+=smtmean[j];
		} 
		
		mean=mean/(float)(high-low);
		
		for(int j=low;j<high;j++)
		{
			fout<<mean<<" ";
		}
		fout<<"\n";
		
	}
	
	fout<<"\n";
	smtmean=input;
	
	for(int i=0;i<bincnt;i++)
	{
		int low=(i*(sz/bincnt));
		int high=((i+1)*(sz/bincnt));
		if(i==bincnt-1)
		 high=sz;
	
		for(int j=low;j<high;j++)
		{
		   	if(high-1-j<j-low)
		   	fout<<smtmean[high-1]<<" ";
		   	else if(j-low<high-j-1)
		   	fout<<smtmean[low]<<" ";
		   	else
		   	fout<<smtmean[j]<<" ";
		   	
		} 
		
		fout<<"\n";
		
	}
	
	
	fout.close();
	
	return 0;
}
