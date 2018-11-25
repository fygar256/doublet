/*
	doublet.cpp
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

#define REP(i,x,n) for(int i = (int)(x); i < (int)(n); i++)
#define rep(i,n) REP(i,0,n)

static const int INF = (1 << 29);

long N;
int      minCost[3000002];
int          pre[3000002];
string start,goal;
string      word[3000002];
vector<int> edge[3000002];
vector<string> path;

static	char	defaultdic[]="/home/gar/dic/ejdic-hand-utf8.txt";
static	FILE	*so;
static	FILE	*fp;
static	int		len;

void get_path(){
  for(int i = N + 1; i != -1; i = pre[i]) path.push_back(word[i]);
  reverse(path.begin(), path.end());
}

bool diff(string s, string t){
  int sz = s.size();
  int count = 0;
  rep(i,sz) if(s[i] != t[i]) count++;
  
  return count == 1;
}

int solve(){
  rep(i,N+2) REP(j,i+1,N+2) {
    diff(word[i], word[j]);
  }

  rep(i,N+2){
    minCost[i] = INF;
    pre[i] = -1;
  }
  minCost[0] = 0;
  
  queue<int> q;
  q.push(0);
  
  while(!q.empty()){
    int now = q.front();
    q.pop();
    
    rep(k,edge[now].size()){
      int next = edge[now][k];
      if(minCost[next] <= minCost[now] + 1) continue;
      q.push(next);
      minCost[next] = minCost[now] + 1;
      pre[next] = now;
      if(next == N + 1) return minCost[next] - 1;
    }
  }

  return -1;
}

int doublet(){
  if(start == goal){
    cout << '0' << endl;
    cout << start << endl;
    cout << goal << endl;
  }
  else{
    word[0] = start;
    word[N + 1] = goal;
      
    rep(i,N+2) REP(j,i+1,N+2) {
      if(diff(word[i], word[j])){
        edge[i].push_back(j);
        edge[j].push_back(i);
      }
    }

    int ans = solve();
    if(ans != -1){
      cout << "number of links : ";
	  cout << ans << endl;
      get_path();
      rep(i,path.size()) cout << path[i] << endl;
      }
	else {
	  cout << "Target can not be reached!" << endl;
	  }
  }
  return 0;
}

char *strtolower(char *s) {
	char	*t=s;
	while(*s!='\0')
		*s++=tolower(*s);
	return(t);
}

char *getword(FILE *fp) {
static	char aword[1024];
	int idx=0,c;

	c=fgetc(fp);
	if (c==EOF) return(NULL);
	if (c==0x81) fgetc(fp);
		else ungetc(c,fp);

	while(1) {
		c=fgetc(fp);
		if (!isalpha(c)) break;
		aword[idx++]=c;
		}
		aword[idx]='\0';
		ungetc(c,fp);
		while(fgetc(fp)!='\n');
		strtolower(aword);
		return(aword);
}

int	main(int argc,char *argv[])
{
	char *dicword,word1[256],word2[256];
	char *dicfile=defaultdic;
	int	ai,i;
	long	n;

	ai=1;
	if ((argc==4)&&(strncmp(*(argv+1),"-d=",3)==0))
			ai=2,--argc,dicfile=&((*(argv+1))[3]);

	if (argc!=3) {
		fprintf(stderr,"two words required.\n");
		exit(1);
		}

	start=argv[ai];
	goal=argv[ai+1];

	sscanf(argv[ai],"%s",word1);
	sscanf(argv[ai+1],"%s",word2);
	strtolower(word1);
	strtolower(word2);
	if (strlen(word1)!=strlen(word2)) {
		fprintf(stderr,"word length mismatch.\n");
		exit(1);
		}

	/* get unique dictionary of given length */
	fp=fopen(dicfile,"r");
	so=fopen("ol.tmp","w");
	if ((fp==NULL)||(so==NULL)) {
		fprintf(stderr,"File open error!\n");
		exit(1);
		}

	len=strlen(word1);
	n=0;
	while((dicword=getword(fp))!=NULL) {
		if (strlen(dicword)==len) {
			fprintf(so,"%s\n",dicword);
			n++;
			}
	}
	fclose(fp),fclose(so);
	system("sort ol.tmp |uniq >dic.tmp");
	system("rm ol.tmp");
	N=n;

	/* read dictionary to array 'word' */
    std::ifstream rf;
	rf.open("dic.tmp",std::ios::in);

	std::string rlb;

	i=1;
    while(!rf.eof()) {
		std::getline(rf,word[i]);
		i++;
		}
	system("rm dic.tmp");
	/* doublet */
	doublet();
	exit(0);
}
