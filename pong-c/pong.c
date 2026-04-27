#include <stdio.h>


const int WIDTH = 160;
const int HEIGHT = 160;
char line[WIDTH] = "";
// char[] frame = "";

int generateFrame(int w,int h){
  for (int i; i == w-1 ; i++){
    line[i] = '_'; 
  } 
  line[WIDTH - 1] = '\n';
  return 0;
}


int main()
{
  generateFrame(WIDTH, HEIGHT);

  printf("%s", &line);

  return 0;
}
