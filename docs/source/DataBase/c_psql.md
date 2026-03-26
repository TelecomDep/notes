# Clang + PSQL

Пример взаимодействия приложения на языке `СИ` с базой данных `PSQL`. В этом нам поможет библиотека [libpq](https://postgrespro.ru/docs/postgresql/current/libpq), поддерживаемая разработчикеами `PSQL`.


## Установка и подключение библиотеки в CMake

**Устанавливаем**:
```bash
sudo apt install libpq-dev
```

**Подключаем в Cmake** (пример для простого `main.c`):

```cmake
# Ищем пакет PostgreSQL (в котором есть libpq)
find_package(PostgreSQL REQUIRED)

# Создаем исполняемый файл 
add_executable(main main.c)

# Линкуем к исполняемому файлу `main`
target_link_libraries(main PRIVATE PostgreSQL::PostgreSQL)
```

## Взаимодействие из кода СИ

Имя базы данных и кредиты пользователя сохранились из предыдущей "лекции".

### Пример подключения к БД
```c
#include <iostream>
#include <chrono>
#include <thread>
#include <cmath>

#include <libpq-fe.h>

#define HOST "localhost"
#define PORT "5432"
#define DB_NAME "test_db_from_psql"
#define DB_USER "postgres"               //по умолчанию postgres
#define DB_USER_PASSWORD "postgres1234" //Пароль от DB_USER


int main(int argc, char *argv[]) {

    PGconn *con;            // обьект подключения
    PGresult *res;          // результат запроса к базе

    const char* info = "host=" HOST " port=" PORT " dbname=" DB_NAME " user=" DB_USER " password=" DB_USER_PASSWORD;
    con = PQconnectdb(info);                // подключаемся к бд по данным из info

    if (PQstatus(con) != CONNECTION_OK){                      // если подключение не удалось пишем ошибку
            std::cerr << "\033[31mОШИБКА\033[0m подключения к БД.\n" << PQerrorMessage(con) << "\n";
            PQfinish(con);                                   // рвём подключение перед выходом
            exit(1);
    } else {
        std::cout << "Подключение \033[32mУСПЕШНО!\033[0m\n\n" << std::endl;
    }
    
    return 0;
}
```

**Результат**:

![alt text](image/psql_bd_connect_from_c_success.png)