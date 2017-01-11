#define my_sizeof(type) (char *)(&type+1)-(char *)(&type)
#include<stdio.h>
int main(){
  double x;
  printf("%d",my_sizeof(x));
  return 0;
  
}
