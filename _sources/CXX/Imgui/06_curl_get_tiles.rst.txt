Получение тайлов из кода С / С++
===================================


Установка зависимостей и подключение к CMakeLists
---------------------


Устанавливаем пакеты:

.. code-block:: bash

  sudo apt install curl

Добавляем в CmakLists нашего проекта (пример с добавлением проект с ImGUI + PSQL):

.. code-block:: cmake

  add_executable(tile ${EXAMPLES_DIR}/osm_tiles/tile_catcher.cpp)
  target_link_libraries(tile PRIVATE imgui implot curl ${SDL2_LIBRARIES} ${OPENGL_LIBRARIES} ${GLEW_LIBRARIES})
  target_include_directories(tile PRIVATE ${STB_INCLUDE_DIRS})


Отправка запроса на тайл-сервер (``curl``)
---------------------

На данном этапе мы уже знаем как, зная ``zoom`` и координаты ``Lat``, ``Lon``, получить необходмые нам значения ``X``, ``Y``.

Формируем и отправляем запрос:

.. code-block:: c

  ...
  #include <curl/curl.h>
  ...

  // Наш callback при получении данных от libcurl
  size_t onPullResponse(void *data, size_t size, size_t nmemb, void *userp) {
    size_t realsize{size * nmemb};
    auto &blob{*static_cast<std::vector<std::byte> *>(userp)};
    auto const *const dataptr{static_cast<std::byte *>(data)};
    blob.insert(blob.cend(), dataptr, dataptr + realsize);
    std::cout << "Bytes received size = " << realsize << std::endl;
    return realsize;
  }

  bool loaded = false;

  int main()
  {

    // 0. Здесь нам нужно из координат Lat, Lon получить координаты X, Y, Z ()
    int z, int x, int y;
    std::vector<std::byte> &blob

    // 1. Инициализируем структуру curl
    CURL *curl{curl_easy_init()};

    // 2. Формируем строку запроса, зная Z, X, Y
    std::ostringstream urlmaker;
    urlmaker << "https://a.tile.openstreetmap.org";
    urlmaker << '/' << z << '/' << x << '/' << y << ".png";

    // 3. Указываем строку (urlmaker) для структуры curl + немного настроект запроса
    curl_easy_setopt(curl, CURLOPT_URL, urlmaker.c_str());
    curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L);
    curl_easy_setopt(curl, CURLOPT_USERAGENT, "curl");
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 1);
    curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 1);

    // 3.1. Здесь говорим положить результать в массив байтиков blob
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&blob);

    // 3.2. При каждом поступлении данны (chunk'ов) вызывается callback, наша функция onPullResponse (функция определена выше)
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, onPullResponse);
  
    // 4. Собственно, выполнение запроса и проверка на его успешность выполнения.
    const bool ok{curl_easy_perform(curl) == CURLE_OK};
    curl_easy_cleanup(curl);
    loaded = true;

    // 5. Здесь уже получили .PNG-байтики, которые нужно отобразить на гарфике
    return 0;
  }

При выполнении данной программы (если мы захотим еще побайтово вывести информацию в консоль), мы получим след. результат :

.. figure:: ./image/tiles_raw_data.png

   Данные, полученные при помощи библиотеки ``curl``

В текстовом виде это будет выглядеть след. образом, нам здесь важно начало байтового массива:

.. code-block:: 

  0x89 0x50 0x4e 0x47 0xd 0xa 0x1a 0xa 0x0 0x0 0x0 0xd 0x49 0x48 0x44 0x52 0x0 0x0 0x1 0x0 0x0 0x0 0x1 0x0 0x8 0x3 0x0 
  0x0 0x0 0x6b 0xac 0x58 0x54 0x0 0x0 0x3 0x0 0x50 0x4c 0x54 0x45 0xc 0xc 0xc 0x10 0x10 0xc 0x1a 0x1a 0x16 0x23 0x24 
  0x1b 0x25 0x25 0x25 0x2d 0x2d 0x23 0x2d 0x2d 0x2d 0x35 0x35 0x29 0x44 0x4c 0x3 0x33 0x33 0x33 0x3e 0x3f 0x30 0x3f 
  0x40 0x31 0x3c 0x3c 0x3c 0x69 0x2d 0x1e 0x54 0x5b 0x13 0x48 0x49 0x37 0x44 0x44 0x44 0x5b 0x63 0x1b 0x4c 0x4c 0x4c 
  0x5f 0x67 0x20 0x59 0x5a 0x45 0x58 0x58 0x58 0x87 0x49 0x38 0x5f 0x60 0x4a 0x6b 0x72 0x2c 0x63 0x64 0x4d 0x60 0x5f 
  0x5e 0x68 0x69 0x55 0x64 0x64 0x63 0x6e 0x70 0x56 0x69 0x68 0x66 0x6e 0x6e 0x6e 0x76 0x78 0x5c 0x6f 0x70 0x6e 0x71 
  0x71 0x71 0x74 0x74 0x6b 0x77 0x78 0x71 0x78 0x77 0x74 0x7a 0x7a 0x75 0x93 0x9d 0x39 0xac 0x6a 0x58 0x7d .........
  ..................................................................................................................
