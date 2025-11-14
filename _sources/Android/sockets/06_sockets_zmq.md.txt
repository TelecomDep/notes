# Работа c сокетами (Sockets).

Короткая выжимка из этих предыдущих лекций:

- У каждого компьютера в сети есть IP-адрес, даже если это просто локальная сеть.
- IP-адрес — это четыре числа от 0 до 255, разделённые точками, например 77.88.55.88 (это адрес сервера Яндекса).
- С помощью этих адресов компьютеры знают, куда направить свои запросы и ответы.
- Когда один компьютер соединяется с другим, они это делают через сетевой порт. Можно сказать, что порт — это номер соединения.
- Сетевые порты в компьютере нумеруются от 1 до 65535, а компьютер сам следит за тем, как распределяются эти номера.
- С помощью портов компьютер понимает, какие данные предназначены какой программе. Некоторые программы и соединения всегда используют один и тот же порт, а другие получают его случайным образом.

**`Сокет`** — это виртуальная конструкция из **`IP-адреса`** и номера `порта`. Её придумали для того, чтобы разработчикам было проще писать код, а программы могли передавать данные друг другу даже в пределах одного компьютера.

Смысл в том, чтобы программист работал не с IP-адресами и портами, разбираясь в тонкостях работы протоколов, а использовал что-то попроще. В итоге получается так:

- программист пишет в программе, что он хочет сделать новый сокет;
- указывает для него IP-адрес, если это необходимо;
- программа собирает это в виртуальную конструкцию, и получается сокет;
- после этого программист может отправлять данные просто в сокет и принимать их оттуда, а компьютер берёт на себя все вопросы по передаче данных.

![28-1920x814.webp](28-1920x814.webp)

## Основные функции сокетов

| **Общие** |   |
| --- | --- |
| Socket | Создать новый сокет и вернуть файловый дескриптор |
| Send | Отправить данные по сети |
| Receive | Получить данные из сети |
| Close | Закрыть соединение |
|   |   |
| **Серверные** |   |
| Bind | Связать сокет с IP-адресом и портом |
| Listen | Объявить о желании принимать соединения. Слушает порт и ждет когда будет установлено соединение |
| Accept | Принять запрос на установку соединения |
|   |   |
| **Клиентские** |   |
| Connect | Установить соединение |



### socket()

Создаёт конечную точку соединения и возвращает файловый дескриптор (с типом файла `S` , Создают прямую связь между процессами в системе. Передают данные между процессами, которые запущены в различных средах либо даже на различных машинах.). Принимает три аргумента:

1. **domain** указывающий семейство протоколов создаваемого сокета
    - **AF_INET** для сетевого протокола IPv4
    - **AF_INET6** для IPv6
    - **AF_UNIX** для локальных сокетов (используя файл)
    - и т.д. (порядка **29-ти разновидностей** протоколов в Unix-like системах [1])
2. **type**
    - **SOCK_STREAM** (надёжная потокоориентированная служба (сервис) или потоковый сокет)
    - **SOCK_DGRAM** (служба датаграмм или датаграммный сокет)
    - **SOCK_RAW** (Сырой сокет — сырой протокол поверх сетевого уровня).
3. **protocol**
    
Протоколы обозначаются символьными константами с префиксом **IPPROTO_*** (например, **IPPROTO_TCP** или **IPPROTO_UDP**). Допускается значение protocol=0 (протокол не указан), в этом случае используется значение по умолчанию для данного вида соединений.

**С**

```cpp
#include <sys/types.h>
#include <sys/socket.h>

int socket(int domain, int type, int protocol);
...
...

int main(){
        struct sockaddr_in serv_addr;
        ...
        ...
        // Создаем сокет
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
    // Указываем тип сокета Интернет
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
}
```

**Python**

```python
import socket

# Создание объекта сокета.
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# AF_INET, SOCK_STREAM и 0 используются по умолчанию при создании сокета.
# Поэтому можно просто писать:
sock_obj = socket.socket()
```

### bind()

Связывает сокет с конкретным адресом. Когда сокет создается при помощи `socket()`, он ассоциируется с некоторым семейством адресов, но не с конкретным адресом. До того как сокет сможет принять входящие соединения, он должен быть связан с адресом. `bind()` принимает три аргумента:

1. **sockfd** — дескриптор, представляющий сокет при привязке
2. **serv_addr** — указатель на структуру `sockaddr`, представляющую адрес, к которому привязываем.
3. **addrlen** — поле `socklen_t`, представляющее длину структуры `sockaddr`.

**С**

```c
#include <sys/types.h>
#include <sys/socket.h>

int bind(int sockfd, const struct sockaddr *my_addr, socklen_t addrlen);
```

**Python**

```python
server_address = ('localhost', 8080)
sock_obj.bind(server_address)  # Привязка адреса и порта к сокету.
```

### listen()

Подготавливает привязываемый сокет к принятию входящих соединений. Данная функция применима только к типам сокетов `SOCK_STREAM` и `SOCK_SEQPACKET`. Принимает два аргумента:

1. **sockfd** — корректный дескриптор сокета.
2. **backlog** — целое число, означающее число установленных соединений, которые могут быть обработаны в любой момент времени (`размер очереди`). Операционная система обычно ставит его равным максимальному значению.

**C**

```c
#include <sys/socket.h>
int listen(int sockfd, int backlog);
```

**Python**

```c
sock_obj.listen(5)  # Ждем соединение клиента.
```

### accept()

Используется для принятия запроса на установление соединения от удаленного хоста. Принимает следующие аргументы:

1. **sockfd** — дескриптор слушающего сокета на принятие соединения.
2. **cliaddr** — указатель на структуру `sockaddr`, для принятия информации об адресе клиента.
3. **addrlen** — указатель на `socklen_t`, определяющее размер структуры, содержащей клиентский адрес и переданной в `accept()`. Когда `accept()` возвращает некоторое значение, `socklen_t` указывает сколько байт структуры `cliaddr` использовано в данный момент.

**C**

```c
#include <sys/types.h>
#include <sys/socket.h>
int accept(int sockfd, struct sockaddr *cliaddr, socklen_t *addrlen);
```

**Python**

```c
conn, addr = sock_obj.accept()  # Установление соединения с клиентом.
```

### connect()

Устанавливает соединение с сервером.

Некоторые типы сокетов работают без установления соединения, это в основном касается **UDP-сокетов**. Для них соединение приобретает особое значение: цель по умолчанию для посылки и получения данных присваивается переданному адресу, позволяя использовать такие функции как **send()** и **recv()** на сокетах без установления соединения.

Загруженный сервер может отвергнуть попытку соединения, поэтому в некоторых видах программ необходимо предусмотреть повторные попытки соединения.

**C**

```c
#include <sys/types.h>
#include <sys/socket.h>
int connect(int sockfd, const struct sockaddr *serv_addr, socklen_t addrlen);
```

**Python**

```c
server_address = ('192.168.1.100', 8080)
sock_obj.connect(server_address)
```

### Передача\прием данных

Для передачи данных можно пользоваться стандартными функциями **чтения/записи** файлов **read** и **write**, но есть специальные функции для передачи данных через сокеты:

- send
- recv
- sendto
- recvfrom
- sendmsg
- recvmsg

Нужно обратить внимание, что при использовании протокола TCP (сокеты типа SOCK_STREAM) есть вероятность получить меньше данных, чем было передано, так как ещё не все данные были переданы, поэтому нужно либо дождаться, когда функция **recv возвратит 0 байт**, либо выставить флаг **MSG_WAITALL** для функции **recv**, что заставит её дождаться окончания передачи. Для остальных типов сокетов флаг MSG_WAITALL **ничего не меняет** (например, в UDP весь пакет = целое сообщение).

### send()

**send**, **sendto** - отправка данных.

**C**

```c
#include <sys/types.h>
#include <sys/socket.h>

ssize_t send(int s, const void *buf, size_t len, int flags);
ssize_t sendto(int  s, const void *buf, size_t len, int flags, const struct sockaddr *to, socklen_t tolen);
```

**Python**

```c
IP = '192.168.1.100'
PORT = 8080

sock_obj.send('Hello World!')
sock_obj.sendto('Hello World!', (IP, PORT))
```

### resv()

**recv**, **recvfrom** - чтение данных из сокета.

**C**

```c
#include <sys/types.h>
#include <sys/socket.h>

ssize_t recv(int s, void *buf, size_t len, int flags);
ssize_t recvfrom(int s, void *buf, size_t len, int flags, struct sockaddr *from, socklen_t *fromlen);
```

**Python**

```c
BUFFER_SIZE = 1024

data = conn.recv(BUFFER_SIZE)
data, sender_addr = conn.recvfrom(BUFFER_SIZE)
```

## **SOCK_STREAM vs SOCK_DGRAM**

| Потоковый (SOCK_STREAM) | Датаграммный(SOCK_DGRAM) |
| --- | --- |
| Устанавливает соединение | Нет |
| Гарантирует доставку данных | Нет в случае UDP |
| Гарантирует порядок доставки пакетов | Нет в случае UDP |
| Гарантирует целостность пакетов | Тоже |
| Разбивает сообщение на пакеты | Нет |
| Контролирует поток данных | Нет |

### Клиент-серверная программа (Python)

**TCP- Server**

```python
import socket
    
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
# Привязываем сокет к IP-адресу и порту
server_socket.bind(('localhost', 12345))
    
# Слушаем входящие соединения
server_socket.listen(1)
    
print("Сервер запущен и ожидает подключений...")
    
# Принимаем входящее соединение
client_socket, client_address = server_socket.accept()
print(f"Подключение установлено с {client_address}")
    
# Получаем данные от клиента
data = client_socket.recv(1024)
print(f"Получены данные: {data}")
    
# Закрываем соединения
client_socket.close()
server_socket.close()
```

**TCP-Client**

```python
import socket
    
# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
# Подключаемся к серверу
client_socket.connect(('localhost', 12345))
    
# Отправляем данные серверу
client_socket.sendall(b'Hello, server!')
    
# Закрываем соединение
client_socket.close()
```

**UDP-Server**

```python
import socket
    
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
# Привязываем сокет к IP-адресу и порту
server_socket.bind(('localhost', 12345))
    
print("Сервер запущен и ожидает входящих данных...")
    
# Получаем данные от клиент
data, client_address = server_socket.recvfrom(1024)
print(f"Получены данные от {client_address}: {data}")
    
# Закрываем сокет
server_socket.close()
```

**UDP-client** 

```python
import socket
    
# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
# Отправляем данные серверу
client_socket.sendto(b'Hello, server!', ('localhost', 12345))
    
# Закрываем сокет
client_socket.close()
```
### Клиент-серверная программа на СИ
**Сервер**
```c
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
int main(int argc, char const* argv[])
{
    int server_fd, new_socket;
    ssize_t valread;
    struct sockaddr_in address;
    int opt = 1;
    socklen_t addrlen = sizeof(address);
    char buffer[1024] = { 0 };
    char* hello = "Hello from server";

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET,
                   SO_REUSEADDR | SO_REUSEPORT, &opt,
                   sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr*)&address,
             sizeof(address))
        < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket
         = accept(server_fd, (struct sockaddr*)&address,
                  &addrlen))
        < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }
  
    // subtract 1 for the null
    // terminator at the end
    valread = read(new_socket, buffer,
                   1024 - 1); 
    printf("%s\n", buffer);
    send(new_socket, hello, strlen(hello), 0);
    printf("Hello message sent\n");

    // closing the connected socket
    close(new_socket);
  
    // closing the listening socket
    close(server_fd);
    return 0;
}
```

**Клиент**

```c
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080

int main(int argc, char const* argv[])
{
    int status, valread, client_fd;
    struct sockaddr_in serv_addr;
    char* hello = "Hello from client";
    char buffer[1024] = { 0 };
    if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary
    // form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)
        <= 0) {
        printf(
            "\nInvalid address/ Address not supported \n");
        return -1;
    }

    if ((status
         = connect(client_fd, (struct sockaddr*)&serv_addr,
                   sizeof(serv_addr)))
        < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
  
    // subtract 1 for the null
    // terminator at the end
    send(client_fd, hello, strlen(hello), 0);
    printf("Hello message sent\n");
    valread = read(client_fd, buffer,
                   1024 - 1); 
    printf("%s\n", buffer);

    // closing the connected socket
    close(client_fd);
    return 0;
}
```
**Компиляция**
```bash
gcc client.c -o clientgcc server.c -o server
```



### Список литературы

1. **Linux manual - page address_families(7) (**[https://man7.org/linux/man-pages/man7/address_families.7.html](https://man7.org/linux/man-pages/man7/address_families.7.html)**)**
2.