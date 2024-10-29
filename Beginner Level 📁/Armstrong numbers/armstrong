//armstrong is a number if the sum of cube of each element gives the same number e.g cude of 1,5,3 gives 153. 

#include<iostream>
#include<math.h>
using namespace std;

int main( )
{
    int n;
    cin>>n;
    int original = n;
int sum = 0;

while(n>0){
    int lastdigit = n%10;// returns Remainder 
    sum+= lastdigit*lastdigit*lastdigit;// calculation and Addition of cube from last digit... 
    n=n/10;
}
if(sum==original){
    cout<<"armstrong"<<endl;
}
else{
    cout<<"not-armstrong"<<endl;
}
return 0;
}

