#include <stdio.h>
#include <stdbool.h>

int main() {
  char *str = "Hello";
  int idx = 0;
  while (true) {
    if (str[idx] == '\0'){
        printf("Found");
        break;
    }
    idx++;
  }
  return 0;
}
