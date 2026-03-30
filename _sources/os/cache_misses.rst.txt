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

Компилируем и запускаем профайлинг при помощи ``perf`` с флагом ``-e``:

.. code-block:: bash

    gcc -o2 -g cache_miss.c -o cache_miss
    sudo perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations ./cache_miss

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

Подробнее по каждой из команд ``perf -e``:

- ``cache-references`` – количество обращений доступа к памяти в КЭШе. Суммарно имеем ``252,440,135``.
- ``cache-misses`` – количество кэш промахов, т.е. количество доступов к памяти, где небоходимо получить доступ из более памяти высокого уровня (``high-level`` или ``RAM``). ``3,536,534`` или ``1.40%`` от общего количества обращений.
- ``cycles`` – Общее количество циклов процессора (CPU), необходимых для работы программы.  `1,227,589,321` циклов, время, которое процессор был активен.
- ``instructions`` – Количество выполненных инструкций (``1,606,273,789``, ``1.31``  insn per cycle).
- ``branches`` – calculates the number of branch instructions executed. Here, we have 193,719 branches, indicating the number of times the program changed its execution path.
- ``faults`` – adds up the number of page faults, which occur when a process tries to access a page of memory that is not currently mapped in its address space. Here, we have 1,523-page faults.
- ``migrations`` – quantifies the number of times a task is migrated between different ``CPU cores``, with ``2 migrations`` in this example.
- ``time elapsed`` - line shows the total time taken for the ``./cache-miss`` example to execute, which is approximately  ``0.332995043`` seconds.

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


