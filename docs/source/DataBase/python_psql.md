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
cursor = conn.cursor()

cursor.execute("SELECT * FROM user_equipment")
print(cursor.fetchall())

cursor.close()

conn.close()
```

<!-- 
# извлекаем первые N строк в полученном наборе
# print(cursor.fetchmany(1)) # здесь N = 1

# print(cursor.fetchone())

# cursor.execute("INSERT INTO user_equipment (Imei, Lat, Lon, Alt, Timestamp) values (333, 84.5559, 51.433332, 225.0, 1233408283)")
# conn.commit()

# print(cursor.fetchall()) -->
