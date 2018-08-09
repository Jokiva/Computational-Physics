#include <stdlib.h>   
#include <stdio.h>   
  
long a=10000,b,c=2800,d,e,f[2801],g;   
  
int main()   
{   
    for(;b-c;)   
        f[b++]=a/5;   
    for(;d=0,g=c*2;c-=14,printf("%.4ld",e+d/a),e=d%a) //原代码为%.4d,GCC给出警告.已改为%.4ld  
        for(b=c;d+=f[b]*a,f[b]=d%--g,d/=g--,--b;d*=b);
    return 0;  
} 