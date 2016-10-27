#include <stdio.h>
#include <cs50.h>

int main(void)
{
  int height;
  do
  {
    printf("Height: ");
    height = get_int();
  }
  while (height < 0 || height > 23);

  for (int row = 0; row < height; row++)
  {
    for (int space = row; space < (height - 1); space++)
    {
      printf(" ");
    }
    for (int hash = 0; hash < (row + 2); hash++)
    {
      printf("#");
    }
    printf("\n");
  }
}
