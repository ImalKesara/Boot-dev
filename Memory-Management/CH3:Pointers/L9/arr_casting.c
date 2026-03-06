#include <stdio.h>

typedef struct Points {
    int x;
    int y;
    int z;
} points_t;
int main(){
    points_t points[3] = {
        {1,4,5},
        {1,2,3},
        {1,9,5},
    };

    int *points_start = (int *) points;
    for(int i = 0; i < 9; i++){
        printf("%d = \n", points_start[i]);
    };

    return 0;
}
