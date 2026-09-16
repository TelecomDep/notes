#define _POSIX_C_SOURCE 199309L

#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include <stdalign.h> // Необходим для спецификатора alignas в C11
#include <immintrin.h>

#define SIZE 1024


// Компилируем gcc -std=c11 -O0 -mavx2 scalar_vs_avx_add.c -o scalar_vs_avx
//      флаг -O0 - без оптимизации, работает как есть
//      флаг -O1 - базовая оптимизация (Удаляет мертвый код, Упрощает простые математические выражения, Оптимизирует ветвления (условия if/else).)
//      флаг -O2 - стандартная полная оптимизация (базовый много где). (Встраивание функций (инлайнинг, Перестановка и объединение циклов, Продвинутый анализ указателей и регистров процессора)

void scalar_add_int(const int* a, const int* b, int* result, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        result[i] = a[i] + b[i];
    }
}

// __m256i - переменная (тип данных), соответствующая 256-битному векторному регистру
// _mm256_load_si256 - интринсик загрузки из памяти в 256-битный регистр
// _mm256_add_epi32 - складываем внутри 256 битного регистра значения по 32 бита
// _mm256_store_si256 - сохраняем в массив result
void avx_add_int(const int* a, const int* b, int* result, size_t size) {
    size_t i = 0;
    for (; i <= size - 8; i += 8) {
        __m256i va = _mm256_load_si256((const __m256i*)&a[i]);
        __m256i vb = _mm256_load_si256((const __m256i*)&b[i]);
        __m256i vr = _mm256_add_epi32(va, vb);
        _mm256_store_si256((__m256i*)&result[i], vr);
    }
}

double get_elapsed_ns(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) * 1e9 + (end.tv_nsec - start.tv_nsec);
}

int main() {
    alignas(32) int a[SIZE];
    alignas(32) int b[SIZE];
    alignas(32) int r_scalar[SIZE];
    alignas(32) int r_avx[SIZE];

    for (size_t i = 0; i < SIZE; ++i) {
        a[i] = (int)i;
        b[i] = (int)(i * 2);
    }

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < SIZE; ++i) {
        r_scalar[i] = a[i] + b[i];
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_scalar = get_elapsed_ns(start, end);
    printf("Скалярное сложение: %.0f [ns]\n", time_scalar);

    clock_gettime(CLOCK_MONOTONIC, &start);
    avx_add_int(a, b, r_avx, SIZE);
    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_avx = get_elapsed_ns(start, end);
    printf("AVX-256 сложени-е:   %.0f [ns]\n", time_avx);

    return 0;
}