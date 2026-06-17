#include<vector>
#include<iostream>
#include<tuple>

// Function to calculate the modular inverse  
std::tuple<int,int,int> extended_gcd(int a, int b){
    if( a==0){
        return {b,0,1};
    }
    auto [gcd,x1,y1]=extended_gcd(b%a,a);

    int x,y;
    x = y1 - x1*(b/a);
    y=x1;
    return {gcd,x,y};

}


int main(){
std::ios_base::sync_with_stdio(false);

int n;
std::cin>>n;
std::vector<int> v(n);
for(int i=0;i<n;i++){
    std::cin>>v[i];
}

// Take mod 41 with every number 
for(int i=0;i<n;i++){
v[i]=v[i]%41;
}

// To calculate the modular inverse for all v[i]
for(int i=0;i<n;i++){
  auto [gcd,x,y]=extended_gcd(v[i],41);
  v[i]=(x+41)%41;                            // If x is negative then this line takes care of it
}

// vector string to store the respective char 
std::vector<char> s(n);
for(int i=0;i<n;i++){
    if(v[i]>=1 && v[i]<=26){
        s[i]= 'a'+v[i]-1;
        }
    else if(v[i]>=27 && v[i]<=36){
             s[i]='0'+v[i]-27;
                }
    else if(v[i]==37)
        s[i]= '_';
        }

for(int i=0;i<n;i++){
    std::cout<<s[i];
}

std::cout<<"\n";
    return 0;
}