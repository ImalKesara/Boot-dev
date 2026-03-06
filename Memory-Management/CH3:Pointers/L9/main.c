#include <stdio.h>

int main() {
  int numbers[5] = {1, 2, 3, 4, 5};

  printf("number[2] = %d\n", numbers[2]);
  printf("number[2] = %d\n", *(numbers + 2));

  int *ptr = numbers;
  int *ptrr = &numbers[0];
  printf("%p\n", ptr);
  printf("%p\n", ptrr);

  return 0;
}
