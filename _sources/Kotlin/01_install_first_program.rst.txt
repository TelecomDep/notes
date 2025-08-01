Установка средств разработки
===================================


Установка IntelliJ IDEA
---------------------

Компилировать и запускать программы на базе языка Kotlin можно в консоли (в терминале), однако, если есть желание разрабатывать  
приложения более сложно порядка, чем ``println('Hello World')``, рекомендуется использовать IDE. Можно выбрать одно из 
наиболее популярных в сфере разработки:  ``IntelliJ IDEA``, ``Android Studio``, ``Eclipce`` и др.

Начнем мы с работы в ``IntelliJ IDEA``. Пройдя по ссылке_, устанавливаем *Community Edition* (бесплатную) версию.

.. _ссылке: https://www.jetbrains.com/idea/download/


.. figure:: ../_static/images/kotlin/00_intellij_idea_install.png
    :name: Canti_15
    :width: 50%

    IntelliJ IDEA Community Edition (free).

Можно установить под Windows, Linux, MasOS.

После установки запускаем IntelliJ IDEA Community Edition и создаем новый проект (настройки среды уже сделаете сами под себя).

.. figure:: ../_static/images/kotlin/00_new_project.png
    :name: Canti_15
    :width: 50%

    Создать новый проект.

Далее, настраиваем параметры проекта. 


.. figure:: ../_static/images/kotlin/00_new_project_initialization.png
    :name: Canti_15
    :width: 50%

    Настройка проекта.

#. **Name** - имя вашего проекта;
#. **Location** можно указать путь к проекту, если не устраивает путь по умолчанию;
#. В левом столбце выбираем Kotlin;
#. **JDK**  - можно указать путь к Java SDK, если он уже установлен на компьютере локально.  Заметьте, если у вас не установлен ``JDK``, среда предложит версию для установки;
#. **Add sample code** - убираем галочку, чтобы начать проект ``с нуля``.

