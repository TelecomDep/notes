# Python + PSQL

Если захотели получить данные из внешнего приложения, написанного вами.
Например, возьмем язык Python как основного `бэкэнд-сервера`, как основного клиента по получению и сохранению данных.

## Установка psycopg2

Устанавливаем из репозитирия:
```bash
sudo apt install python3-psycopg2
```

## Подключение к базе данных

```python
import psycopg2

# Таблица, которую мы создали до этого
conn = psycopg2.connect(dbname="test_db_from_psql", host="localhost", user="postgres", password="postgres1234", port="5432")

print("connected to data base")

conn.close()
```

## Получение данных (Cursor)

Взаимодействие с базой данных производтся при помощи объекта класса `cursor`. Получить его можно через метод объекта класса `connection` - `cursor()`. 

Основные методы класса `cursor`:
|Метод | Описание| Пример |
|---|---|---|
|`execute(query, vars=None)`| выполняет одну SQL-инструкцию. Через второй параметр в код SQL можно передать набор параметров в виде списка или словаря|`cursor.execute("SELECT * FROM user_equipment")` |
|`executemany(query, vars_list)`| выполняет параметризованное SQL-инструкцию. Через второй параметр принимает наборы значений, которые передаются в выполняемый код SQL.| |
|`callproc(procname[, parameters])`| выполняет хранимую функцию. Через второй параметр можно передать набор параметров в виде списка или словаря| |
|`mogrify(operation[, parameters])`| возвращает код запроса SQL после привязки параметров| |
|`fetchone()`| возвращает следующую строку из полученного из БД набора строк в виде кортежа. Если строк в наборе нет, то возвращает `None`|`cursor.fetchone()` |
|`fetchmany([size=cursor.arraysize])`| возвращает набор строк в виде списка. количество возвращаемых строк передается через параметр. Если больше строк нет в наборе, то возвращается пустой список.| `cursor.fetchmany(12)`|
|`fetchall()`| возвращает все (оставшиеся) строки в виде списка. При отсутствии строк возвращается пустой список.| `cursor.fetchall()`|
|`scroll(value[, mode='relative'])`| перемещает курсор в наборе на позицию `value` в соответствии с режимом `mode`.| |

Ниже пример получения всех строк из, созданной ранее таблицы:

```python
import psycopg2

# Таблица, которую мы создали до этого
conn = psycopg2.connect(dbname="test_db_from_psql", host="localhost", user="postgres", password="postgres1234", port="5432")

cursor = conn.cursor() # получаем курсор

cursor.execute("SELECT * FROM user_equipment")
print(cursor.fetchall())

cursor.close() # закрываем курсор

conn.close() 
```
## Выполняем запросы в SQL-формате

Выполнение команд `SQL` производится при помощи методов `execute`/`executemany` курсора, но для **подтверждения** их выполнения необходимо вызывать метод `commit()` объекта `connection`. Например:

```python
import psycopg2

# Таблица, которую мы создали до этого
conn = psycopg2.connect(dbname="test_db_from_psql", host="localhost", user="postgres", password="postgres1234", port="5432")

cursor = conn.cursor() # получаем курсор

sql = "CREATE DATABASE new_data_base" # SQL-запрос в виде строки
cursor.execute(sql)
conn.commit()   # здесь команда на самом деле выполнится

cursor.close() # закрываем курсор

conn.close() 
```

<!-- 
# извлекаем первые N строк в полученном наборе
# print(cursor.fetchmany(1)) # здесь N = 1

# print(cursor.fetchone())

# cursor.execute("INSERT INTO user_equipment (Imei, Lat, Lon, Alt, Timestamp) values (333, 84.5559, 51.433332, 225.0, 1233408283)")
# conn.commit()

# print(cursor.fetchall()) -->
