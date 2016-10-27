#include <stdio.h>
#include <cs50.h>

int main(void)
{
  printf("Minutes: ");
  int minutes = get_int();
  int bottles = minutes*(192/16);
  printf("Your %i minute shower used the equivalent of %i bottles of water!\n", minutes, bottles);
}
