#include <stdio.h>
#include <cs50.h>

void cough(int n);
void say(string s, int n);

int main(void)
{
  cough(3);
  say("hello!", 4);
}

void cough(int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("cough\n");
  }
}

void say(string s, int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("%s\n", s);
  }
}
