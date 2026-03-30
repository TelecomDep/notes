Промахи кэша (L1, L2, L3)
===================================

Пример кода с промахами кэш ``/src/examples/cache_miss.c``:
.. code-block:: c
    #include <stdio.h>
    #define SIZE 10000

    int arr[SIZE][SIZE]; 

    int main() {
        long long sum = 0;

        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                sum += arr[j][i]; 
            }
        }
        return 0;
    }

Компилируем и запускаем профайлинг при помощи ``perf``:

.. code-block:: bash
    ~/../src/examples$ gcc -o2 -g cache_miss.c -o cache_miss
    ~/../src/examples$ sudo perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations ./cache_miss

Видим следующий вывод:

.. code-block:: bash
    Performance counter stats for './cache_miss':

       252,440,135      cache-references                                                      
         3,536,534      cache-misses                     #    1.40% of all cache refs         
     1,227,589,321      cycles                                                                
     1,606,273,789      instructions                     #    1.31  insn per cycle            
       145,190,445      branches                                                              
            97,709      faults                                                                
                 2      migrations                                                            

       0.332995043 seconds time elapsed

       0.280862000 seconds user
       0.051974000 seconds sys

Подробнее по каждой из команд:

- ``cache-references`` – counts the total number of cache references, which are memory accesses to the cache. In this sample, we have 2,315 cache references.
- ``cache-misses`` – sums up the number of cache misses, which are memory accesses that require fetching data from a higher-level cache or main memory. There were 513 cache misses in this sample, accounting for 22.15% of all cache references.
- ``cycles`` – computes the total number of CPU cycles executed. Here, we have 1,004,927 cycles, indicating the time that the CPU was active.
- ``instructions`` – enumerates the total number of instructions executed. Here, we have 1,002,550 instructions, with an average of 0.99 per cycle, to indicate how efficiently the instructions execute.
- ``branches`` – calculates the number of branch instructions executed. Here, we have 193,719 branches, indicating the number of times the program changed its execution path.
- ``faults`` – adds up the number of page faults, which occur when a process tries to access a page of memory that is not currently mapped in its address space. Here, we have 1,523-page faults.
- ``migrations`` – quantifies the number of times a task is migrated between different CPU cores, with 2 migrations in this example.
- ``time elapsed`` line shows the total time taken for the sleep 5 command to execute, which is approximately 0.1009 seconds.

Пример вывода с последовательным доступом к памяти (в строке):

.. code-block:: c
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            sum += arr[i][j]; // Сначала суммируем строку, потом уже меняем столбец
        }
    }

Вывод perf:

.. code-block:: bash
     Performance counter stats for './cache_miss':

        14,890,250      cache-references                                                      
            72,399      cache-misses                     #    0.49% of all cache refs         
       706,258,358      cycles                                                                
     1,603,989,429      instructions                     #    2.27  insn per cycle            
       144,702,850      branches                                                              
            97,711      faults                                                                
                23      migrations                                                            

    0.193752798 seconds time elapsed

    0.134352000 seconds user
    0.059155000 seconds sys


