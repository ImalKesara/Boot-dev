#include <stdio.h>

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

int main(){
    coordinate_t coord[3] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    printf("points[1].x = %d points[1].y = %d points[1].z = %d\n", coord[1].x , coord[1].y , coord[1].z);
    printf("points[1].x = %d points[1].y = %d points[1].z = %d\n", (coord + 1)->x , (coord + 1) ->y  , (coord + 1)->z);

    return 0;

}
