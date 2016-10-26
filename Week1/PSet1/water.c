#include <stdio.h>
#include <cs50.h>

int main(void)
{
  int min;
  printf("Minutes: ");
  do
  {
    min = get_int();
  }
  while (min != sizeof(int));
  int bottle = (192/16);
  printf("%i", bottle);
}
