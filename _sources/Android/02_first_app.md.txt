# Создание первого приложения (начало)

## Установка Android Studio

После установки [Androi Studio](https://developer.android.com/studio) создадим свое первое приложение "Hello World". В нем мы ознакомимся со структурой Android-проекта, основными элементами экрана UI (User Interface).

### Первый проект
Создадим первое приложение в виде `Empty Views Activity`:

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_02_new_project.PNG?raw=true)

Рис. 1. Окно создания приложения.

Далее, выберем шаблон для первого приложнеия. Как говорилось выше, выберем `Empty Views Activity`.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_02_empty_activity_views.PNG?raw=true)

Рис. 2. Выбор `Empty Views Activity`.

Нам предоставят возможность выбрать параметры проекта:
- Name - название вашего приложения;
- Language - язык программирвоания (`Java` \ `Kotlin`);
- Minimum SDK - минимальная версия SDK (версия библиотек, используемых в проекте);
- Build language - язык системы сборки проекта.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_02_project_properties.PNG?raw=true)

Рис. 3. Параметры проекта.

В результате мы получим проект со всеми необходимыми элементами для **сборки**, **компиляции** и **запуска** первого приложения.

### Рабочее пространство разработчика
![1759422427188](image/02_first_app/1759422427188.png)

Рис. 4. Рабочее пространство Android Studio.

На рисунке 4 показан пример окна Вашего первого приложения и `Layout Editor`. `Layout Editor` состоит из `Palette`, `Component Tree`, `Design Editor`  и `Attributes`. 

1.  `Project window` - отображает структуру проекта;
2.  `Palette\Политра` - дает доступ к использованию компонентов и слоев (`layouts`) в текущее `Activity`, например:  `TextViews`, `ImageViews`, и `Buttons`.
3.  `Component Tree` - показывает иерархию `виджетов\ views` для вашего **Activity**.
4.  `Design Editor` - визуальное представление вашего **Activity**. 
5.  `Attributes\Окно Атрибутов` - состоит из списка атрибутов выбранного компонента. Можно менять параметра атрибутов. 

**Запуск приложения**

![1759423678960](image/02_first_app/1759423678960.png)

Рис 6. Первый запуск приложения

1. Можно создать и запустить при помощи Эмуляторв (`Tools` -> `Device Manager` -> `Add a new device`);
2. А можно запустить на Вашем смартфоне. Необходимо включить `режим разработчика` и возможность `отладки` (внутри режима разработчика).

![1759423888448](image/02_first_app/1759423888448.png)

Рис. 7. Пример окна создания эмулятора.


