#include <stdio.h>

#define CAPACITY 50000 // Емкость хэш-таблицы


uint64_t calc_hash(char *str){
    uint64_t summ = 0;
    for(int j=0; str[j]; j++){
        summ += str[j];
    }

    return summ % CAPACITY;
}

typedef struct hash_item_s {
    char *key;
    char *value;
} hash_item_t;

typedef struct hash_table_s{
    hash_item_t **items; // Важно, это массив УКАЗАТЕЛЕЙ на каждый элемент структуры hash_item_s;
    int size;
    int count;
} hash_table_t;


hash_item_t *create_item(char* key, char* value) {
    hash_item_t *item = (hash_item_t *)malloc(sizeof(hash_item_t));
    item->key = (char*) malloc (strlen(key) + 1);
    item->value = (char*) malloc (strlen(value) + 1);

    strcpy(item->key, key);
    strcpy(item->value, value);

    return item;
}

void free_item(hash_item_t *item){
    free(item->key);
    free(item->value);
    free(item);
}

hash_table_t *create_table(int size) {
    hash_table_t *table = (hash_table_t *)malloc(sizeof(hash_table_t));
    table->size = size;
    table->items = (hash_item_t **)calloc(table->size, sizeof(hash_item_t *));
    for (int i=0; i<table->size; i++) {
        table->items[i] = NULL;
    }
        
}

void free_table(hash_table_t *table){
    for (int i=0; i<table->size; i++) {
        if(table->items[i] != NULL){
            free_item(table->items[i]);
        }
    }
    free(table->items);
    free(table);
}

int main(){

    return 0;
}