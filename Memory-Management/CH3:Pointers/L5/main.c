#include <stdio.h>

int main(){
    int meaning_of_life =42;
    int *address_of_the_meaning_life = &meaning_of_life;

    //Dereferencing Pointers (gets the value of pointer) stored value
    int result_of_meaning_of_life = *address_of_the_meaning_life;
    printf("%d\n" , result_of_meaning_of_life);
    return 0;
}
