#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
struct data{
	string ss;
	long long num;
};
bool asc( const data& left, const data& right ) {
	return left.ss == right.ss ? left.num < right.num : left.ss < right.ss;
}
vector<data> d1,d2;
long long search(long long s, long long g, string st){
	if(s == g) {
		if(st == d2[s].ss) {
			return d2[s].num;
		}
		return -1;
	}
	if(s+1 == g) {
		if(st == d2[s].ss) return d2[s].num;
		if(st == d2[g].ss) return d2[g].num;
		return -1;
	}
	long long half = (s+g)/2;
//cout << "half: " << half << endl;
	if(st == d2[half].ss) {
		return d2[half].num;
	}
	if(st.compare(d2[half].ss) < 0) {
		return search(s,half,st);
	}
	return search(half,g,st);
}

int main(void){
	long long n=1000000,i;
	d1.resize(n);
	d2.resize(n);
	i = 0;
	while(true){
		string s;
		long long x;
		cin >> s >> x;
		if(s[0]=='0' && x==0) break;
		d1[i].ss = s;
		d1[i].num = x;
		i++;
	}
	i = 0;
	while(true){
		string s;
		long long x;
		cin >> s >> x;
		if(s[0]=='0' && x==0) break;
		d2[i].ss = s;
		d2[i].num = x;
		i++;
	}
//cout << "input finish\n";
	sort(d2.begin(),d2.end(),asc);
//cout << "sort finish\n";
	for(i=0;i<d1.size();i++) {
		long long p;
//if(i%10000 == 0) cout << i << endl;
		p = search(0,d2.size()-1,d1[i].ss);
		if(p != -1) {
			cout << "key1: " << d1[i].num << ", key2: " << p << endl;
		}
		//break;
	}
	//cout << n << '\n';
}
