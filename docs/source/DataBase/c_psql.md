# Clang + PSQL

Пример взаимодействия приложения на языке `СИ` с базой данных `PSQL`. В этом нам поможет библиотека [libpq](https://postgrespro.ru/docs/postgresql/current/libpq), поддерживаемая разработчикеами `PSQL`.


## Установка и подключение библиотеки

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

