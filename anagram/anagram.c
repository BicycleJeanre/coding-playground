#include <stdio.h>
#include <string.h>
int main() {

  char outputWords[1000][10];
  int currentPosition;
  char currentChar;

  // get input word
  char word[10];
  printf("Enter your Anagram word: ");
  scanf("%9s", word);

  strcpy(outputWords[0], word);

  printf("The output is: %s", word);
  return 0;
}
