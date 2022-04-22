#include "array.h"
#include <stdio.h>
#include <stdlib.h>

/*
typedef struct {
    int *array;
    int size;
} Array;

Array array_create(int init_size);
void array_free(Array *a);
int array_size(const Array *a);
int* array_at(const Array *a, int index);
void array_inflate(Array *a, int more_size);
*/


Array array_create(int init_size){
    Array arr;
    arr.array = (int*)malloc(init_size*sizeof(int));;
    arr.size = init_size;
    return arr;
}

void array_free(Array *a){
    free(a->array);
    a->array = NULL;
    a->size = 0;
}

int array_size(const Array *a){
    return a->size;
}

int* array_at(const Array *a, int index){
    return &(a->array[index]);
}

int array_get(const Array *a, int index){
    return a->array[index];
}

void array_set(Array *a, int index, int value){
    a->array[index] = value;
}

void array_inflate(Array *a, int more_size){
    int *p = (int*)malloc(sizeof(int)*(a->size + more_size));
    for (int i=0; i<a->size; i++){
        p[i] = a->array[i];
    }
    free(a->array);
    a->array = p;
    a->size += more_size;
}

int main(){
    Array a;
    a = array_create(5);

    *array_at(&a, 0) = 10;
    array_set(&a, 2, 2);

    for (int i=0; i< a.size; i++){
        printf("%d\n", array_get(&a, i));
    }

    array_free(&a);

    return 0;
}