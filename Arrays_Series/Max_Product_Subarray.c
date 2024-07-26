
#include <stdio.h>

int main() {
   int a[]={-2,3,-4};
   int result=a[0];
   int min=a[0];
   int max=a[0];
   
   for(int i=1;i<3;i++)
   {
       if(a[i]<0)
       {
           int temp;
           temp=max;
           max=min;
           min=temp;
       }
       max=a[i]>(max*a[i])?a[i]:(max*a[i]);
       min=a[i]>(min*a[i])?(min*a[i]):a[i];
       result=result>max?result:max;
   }
   printf("%d",result);
}