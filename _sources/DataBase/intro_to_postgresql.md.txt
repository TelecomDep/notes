# PostgreSQL (Основы)

## Установка

Устанивливаем с [официального сайта](https://www.postgresql.org/download/). 

### Ubuntu

**Ubuntu** поддерживает приложение `postgresql` в виде "**установочных**" пакетов. Есть возможность установить разные версии.
```bash
sudo apt-get install postgresql # по умолчанию установится 14 версия
```

**ЕСЛИ** хотим **более новую версию**:

```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
sudo apt update
```

```bash
sudo apt install postgresql-18
```

После установки желательно проверить запущен ли сервис postgresql:

```bash
sudo service postgresql status
```

Должны увидеть:

![1760861601308](image/introduction/1760861601308.png)

Управлять работой сервиса можно при помощи команд:

```bash
sudo service postgresql start       # запуск
sudo service postgresql restart     # перезапуск
sudo service postgresql stop        # остановка
```

**Важно отметить**, что `postgresql` позволяет, так называемый, `peer` - доступ. Это позволяет получать доступ к `СУБД` от Вашего пользователя (под которым приложение было установлено).

При установке на ваш компьютер, приложение, по умолчанию, создаст пользователя `postgres` (без пароля, но имеющего доступ к серверу **СУБД**).

Первым делом, нужно задать пароль для пользователя, чтобы в дальнейшем мы могли работать с `СУБД`.

1. Подключаемся к СУБД под `sudo` с флагом `-u <имя пользователя>`:
```bash
sudo -u postgres psql # postgres - пользователь, который был создан по умолчанию
```
2. Мы увидим новую консоль `psql`:

![1760804468263](image/introduction/1760804468263.png)

Далее меняем пароль для пользователя `postgres` командой:

```bash
\password postgres
```

`Работает!`

<!-- **Из важного** (важно для доступа):

1. Вводим и запоминаем пароль;
![1760719893966](image/introduction/1760719893966.png)

2. Запоминаем номер порта, по которуму будем осуществлять доступ к базе данных;
![1760719963121](image/introduction/1760719963121.png)

3. Остальное - **по умолчанию**.

`Ура, установили!` -->

## Подключение к СУБД

Работать с системой управления базой данных можно при помощи приложений:

![1760722464959](image/introduction/1760722464959.png)

1. `psql` - нативная консоль;
2. `pgAdmin` - [Open-source приложение](https://www.pgadmin.org/) по управлению `PostgreSQl` при помощи графической оболочки;
3. `DBeaver` - аналогично второму варианту, [ссылка](https://dbeaver.io/);
4. `Navicat` - тоже [визуальный интерфейс](https://www.navicat.com/ru/) для управления СУБД.

### psql
`psql` - это нативный метод взаимодействия с **СУБД**. Устанавливается по умолчанию.

При помощи консоли происходит взаимодействие с сервером PostgreSQL.
`-u <user_name> `- это имя пользователя.

```bash
sudo -u postgres psql 
```

### pgAdmin

#### Установка pgAdmin

```bash
# Установка открытого ключа для репозитория
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Создаем файл конфигурации репозитория
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Установка pgAdmin
#

# Install for both desktop and web modes:
sudo apt install pgadmin4

# Install for web mode only: 
sudo apt install pgadmin4-web 

# Настройка, если хотим работать в вебе pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh
```

В результате, после настройки setup-web запуститься сервер pgAdmin по адресу: `https://127.0.0.1/pgadmin4` (вход по `email` + `пароль`, введенный при **установке**):

![1760861338204](image/introduction/1760861338204.png)

