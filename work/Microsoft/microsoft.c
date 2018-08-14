// Definition for arrays:
// typedef struct arr_##name {
//   int size;
//   type *arr;
// } arr_##name;
//
// arr_##name alloc_arr_##name(int len) {
//   arr_##name a = {len, len > 0 ? malloc(sizeof(type) * len) : NULL};
//   return a;
// }
//

void turn_right(int *dir){
    int tmp = dir[0];
    dir[0] = -dir[1];
    dir[1] = tmp;
}

arr_arr_integer spiralNumbers(int n) {
    int *matrix = malloc(n * n * sizeof(int));
    arr_arr_integer a = alloc_arr_arr_integer(n);

    for(int i = 0; i < n; i++) {
        a.arr[i].arr = matrix + i * n;
        a.arr[i].size = n;
    }

    int dir[2] = { 1, 0 };
    int pos[2] = { 0, 0 };
    int min[2] = { 0, 0 };
    int max[2] = { n, n };

    int counter = 1;

    while(max[0] > min[0] && max[1] > min[1]) {
        int turn = 0;
        if(pos[0] + dir[0] >= max[0]) {
            min[1]++;
            turn_right(dir);
        } else if(pos[1] + dir[1] >= max[1]) {
            max[0]--;
            turn_right(dir);
        } else if(pos[0] + dir[0] < min[0]) {
            max[1]--;
            turn_right(dir);
        } else if(pos[1] + dir[1] < min[1]) {
            min[0]++;
            turn_right(dir);
        }

        a.arr[pos[1]].arr[pos[0]] = counter++;
        pos[0] += dir[0];
        pos[1] += dir[1];
    }

    return a;
}
