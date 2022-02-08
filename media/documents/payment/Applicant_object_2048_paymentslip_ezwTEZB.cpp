#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define f(i,low,up) for(int i=low;i<up;i++)
#define F first
#define S second
#define mk make_pair

typedef struct dnode{
	string label;
	int level;
	vector<pair<string,struct dnode*> >child;
	
	
}*dptr;

map<string,set<string> >attr;

int num_attr;

void get_data(vector<vector<string> >&v)
{
	ifstream fin("decision.txt");
	
	if(!fin)
	{
		cout<<"Error opening file\n";
		return;
	}
	
	string str;
	while(getline(fin,str))
	{
		stringstream ss(str);
		string sp;
		vector<string>vec;
		while(ss>>sp)
		{
			vec.pb(sp);
			////cout<<"& "<<sp<<" ";
		}
		//cout<<"\n";
		
		v.pb(vec);
	}
	
}

//--------------------------------------------------------------------------
set<int>taken;

/*float get_info()
{
	map<string,float>mp;
	
	f(i,0,v.size())
	{
		mp[v[i][v[0].size()-1]]++;
	}
	
	float info=0;
	
	map<string,int>::iterator it;
	
	for(it=mp.begin();it!=mp.end();it++)
	{
		float k=(it->second/v.size());
		k=0-(k*log2(k));
		info+=k;
	}
	
	return info;
}
*/

//FINDS COLUMN WHICH GIVES MAXIMUM GAIN

float get_colinfo(int colnum,vector<vector<string> >v)
{
	map<string,map<string,int> >mp;
	
	int lastcol=v[0].size()-1;
	
	f(i,1,v.size())
	{
	   mp[v[i][colnum]][v[i][lastcol]]++;	
	}
	 
    map<string,map<string,int> >::iterator it;
    
    int sz=v.size();
    
    float infoval=0;
    
    for(it=mp.begin();it!=mp.end();it++)
    {
    	map<string,int>::iterator iter;
    	
    	
    	cout<<it->first<<" * \n";
    	for(iter=it->second.begin();iter!=it->second.end();iter++)
        {
        	cout<<iter->F<<" "<<iter->S<<"\n";
     	}
    }
    
    for(it=mp.begin();it!=mp.end();it++)
    {
    	map<string,int>::iterator iter;
    	
    	int colsize=0;
    	
    	for(iter=it->second.begin();iter!=it->second.end();iter++)
    	{
    		colsize+=iter->second;
		}
		
		//cout<<"colsize is "<<colsize<<"\n";
    	
    	float val=0;
    	
    	for(iter=it->second.begin();iter!=it->second.end();iter++)
    	{
    		float val2=iter->second/(float)colsize;
    		float val1=(colsize/(float)sz)*(val2*log2(val2));
    		val-=val1;
		}
          infoval+=val;	 
    	
	}
	
	return infoval;
}

void print(vector<vector<string> >v)
{
	f(i,0,v.size())
	{
		f(j,0,v[i].size())
		{
			cout<<v[i][j]<<" ";
		}
		cout<<"\n";
	}
}


bool check(vector<vector<string> >v)
{
	int col=v[0].size()-1;
	string val=v[1][col];
    f(i,2,v.size())
	{
	    if(v[i][col]!=val)
		  return false;	
	}	
	
	return true;
}

string get_max(vector<vector<string> >v)
{
	map<string,int>mp;
	int col=v[0].size()-1;
	f(i,1,v.size())
	{
		mp[v[i][col]]++;
	}
	
	map<string,int>::iterator it;
	
	int maxi=-1;
	string str="";
	
	for(it=mp.begin();it!=mp.end();it++)
	{
		if(it->S>maxi)
		{
			str=it->F;
			maxi=it->S;
		}
	}
	
	return str;
	
}



void create_tree(dptr &root,vector<vector<string> >v)
{
        if(root->level==num_attr||check(v))
		{
			string n = get_max(v);
			root->label=n;
			root->level=root->level+1;
			
			cout<<"making leaf val "<<root->label<<"\n";
			
			return;
		}
    
    float maxi=1000000;
    int minind=-1;
    
    f(i,0,v[0].size()-1)
    {
    	
		float val=get_colinfo(i,v);
		//cout<<fixed<<setprecision(4)<<val<<"\n";
    	if(val<maxi)
    	{
    	   maxi=val;
		   minind=i;	
		}
    	
	}
	
	//cout<<"Maximum gain found for "<<v[0][minind]<<"\n";
	
	//cout<<fixed<<setprecision(4)<<"maxi "<<maxi<<" "<<minind;
	
   
    
//    
//   
//	
//	//find gain index
//	
//	vector<vector<int> >vec;
//	map<string,vector<int> >iterator::it;
//	

	
	
    	
    
		root->label=v[0][minind];
	
		
		
    	
    	set<string>::iterator it;
    	
    	vector<vector<string> >vec(v);
    	
    	
      //REMOVING COLUMN	
       f(i,0,v.size())
	   {
		v[i].erase(v[i].begin()+minind);
	   }
	   
	    map<string,vector<int> >cmap;
    		
    	f(i,1,vec.size())
    	{
    	  cmap[vec[i][minind]].pb(i); 	
		}
    	
    	for(it=attr[root->label].begin();it!=attr[root->label].end();it++)
    	{
    		vector<vector<string> >vect;
    		vect.pb(v[0]);
    		
    		
    		if(cmap.find(*it)==cmap.end())
    		{
    			//making leaf node
    			
    			dptr leaf=new dnode();
    			leaf->level=root->level+1;
    			leaf->label=get_max(v);
    			root->child.pb(mk(*it,leaf));
			}
			else
			{
				dptr r=new dnode();
				r->level=root->level+1;
				root->child.pb(mk(*it,r));
				
				 f(i,0,cmap[*it].size())
				 {
				    vect.pb(v[cmap[*it][i]]);	
				 }
				 
//				 cout<<*it<<" After trimming vector becomes \n";
//				 
//				 print(vect);
//				cout<<"Sendiing lala\n";
				create_tree(r,vect);
			}
		}
}


void level_order(dptr root)
{
	queue<dptr>q;
	q.push(root);
	
	while(!q.empty())
	{
		dptr node=q.front();
		q.pop();
		cout<<node->label<<" "<<node->level;
		if(node->child.size()==0)
		 cout<<" leaf ";
		
		//prev=node->level;
		
		f(i,0,node->child.size())
		{
		 cout<<node->child[i].F<<"  ";	
		 q.push(node->child[i].S);
	    }
	    
	    cout<<"\n";
		
	}
}

void dfs(dptr root)
{
	cout<<root->label<<" "<<root->level<<" ";
	
	if(root->child.size()==0)
	{
		cout<<"leaf\n";
	}
	
	f(i,0,root->child.size())
	{
		cout<<root->child[i].F<<"\n";
		dfs(root->child[i].S);
	}
	
}

void  mine(dptr root,map<string,string>mp)
{
	while(root->child.size()>0)
	{
		f(i,0,root->child.size())
		{
			if(root->child[i].F==mp[root->label])
			{
				root=root->child[i].S;
				break;
			}
		}
	}
	
	cout<<"label is "<<root->label<<"\n";
}


int main()
{
	vector<vector<string> >v;
	get_data(v);
	
    num_attr=v[0].size()-1;
	
    f(i,0,v[0].size())
    {
    	f(j,1,v.size())
    	{
    		attr[v[0][i]].insert(v[j][i]);
		}
	}
	
	map<string,set<string> >::iterator it;
	
//	for(it=attr.begin();it!=attr.end();it++)
//	{
//		set<string>::iterator itr;
//		
//		cout<<it->F<<" ";
//		for(itr=it->S.begin();itr!=it->S.end();itr++)
//		{
//			cout<<*itr<<" ";
//		}
//		
//		cout<<"\n\n";
//		
//	}
    
    
	
	
	//float infod=getinfod();
    
   
	
	
	
	dptr root=new dnode();
	root->level=0;
	create_tree(root,v);
	
	
	cout<<"level order \n\n";
	level_order(root);
	
	
	cout<<"\n\n";
	
	dfs(root);
	
	map<string,string>mp;
	
	mp["age"]="middle_aged";
	mp["income"]="high";
	mp["student"]="yes";
	mp["credit_rating"]="fair";
	
	mine(root,mp);
	
	
	
	return 0;
}
