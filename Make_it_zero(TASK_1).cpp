#include<iostream>
#include<vector>


void make_it_zero(){
int n;
std::cin >> n;
std::vector<int> v(n);
for(int i = 0; i < n; i++){
    std::cin >> v[i];
}

if(n % 2 == 0){
    // Even length takes 2 Operations
    std::cout << 2 << "\n";
    std::cout << 1 << " " << n << "\n";
    std::cout << 1 << " " << n << "\n";
} else {
    // Odd length takes 4 opeartions
    std::cout << 4 << "\n";
    std:: cout << 2 << " " << n << "\n";
    std:: cout << 2 << " " << n << "\n";
    std:: cout << 1 << " " << 2 << "\n";
    std:: cout << 1 << " " << 2 << "\n";
}

}

int main(){
std::ios_base::sync_with_stdio(false);   // Turns off the synchronization between C++ streams and  C streams , for better speed 
std::cin.tie(nullptr);                   // Unties cin from cout , for better speed
int t;
std::cin>>t;
while(t>0){
make_it_zero();
    t--;
}
    return 0;
}


