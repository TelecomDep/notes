# Структура проекта
В открывшемся проекте мы увидмим структуру:

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_02_project_structure.PNG?raw=true)

Рис. 4. Стркутура проекта.

Вкратце, проект состоит из нескольких важный директорий:
-  `/app` включает в себя еще 3 директории:
    - `/manifest` - содержит файлы конфигурации\\манифеста приложения (ключевой файл в приложении Android);
    - `/kotlin` + java - содержит исходный код приложения;
    - `/res` - включает в себя файлы, используемые приложением Android (картинки, иконки, стили, музыка и т.д.);
- `/Gradle Scripts`. 

## AndroidManifests.xml

Файл `AndroidManifest.xml` является одним из самых важных в Android проекте. В нем содержится информация о пакетах приложения, компонентах типа `Activity`, `Service` и т.д..
Файл `AndroidManifest.xml` выполняет следующие задачи:

- Предоставляет разрешения приложению на использование или доступ к другим компонентам системы.
- Определяет как будут запускаться, например, Activity (какие фильтры использовать).

## /res 

В папке `/res` расположены все используемые приложением ресурсы, включая изображения, различные xml файлы, анимации, звуковые файлы и многие другие. Внутри папки **res** эти все ресурсы распределены по своим папкам:

- Папка  `/drawable` содержит файлы с изображениями, которые будет использоваться в приложении;
- Папка `/layout` располагает xml файлами, которые используются для построения пользовательского интерфейса Android приложения;
- В папке `/menu` находятся xml файлы, используемые только для создания меню;
- В  `/mipmap` папке хранят только значки приложения. Любые другие drawable элементы должны быть размещены в своей папке;
- `/values` хранит те xml файлы, в которых определяются простые значения типа строк, массивов, целых чисел, размерностей, цветов и стилей.

## Gradle  

 Скрипты Gradle используются для автоматизации сборки проекта. Android Studio выполняет сборку приложения в фоновом режиме без какого-либо вмешательства со стороны разработчика. Этот процесс сборки осуществляется с использованием системы Gradle — инструментария для автоматической сборки с помощью набора конфигурационных файлов. Gradle скрипты написаны на языке `groove`.  

## Ползовательский интерфейс (первое Activity)
При создании первого приложения, вы могли увидеть интерфейс работы с **"внешним видом"** вашего Android-приложения. 

По умолчанию, файл `/layout/activity_main.xml` определяет разметку первой `"страницы" (activity)`, которую видит, с которой взаимодействует пользователь.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_01_main_xml.PNG?raw=true)
Рис. 5. Окно макета `Activity`.

Листинг 1. `activity_main.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.541"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.398" />

    <Button
        android:id="@+id/go_to_second_activity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="36dp"
        android:layout_marginEnd="120dp"
        android:text="SecondActivity"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView2" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

Макет `Activity`, по умолчанию, определяет два виджета (`widgets`): 
- ConstraintLayout;
- TextView;
- p.s. Button (из примера выше) мы добавили **после** создания первого приложения.

Виджеты представляют собой структурные элементы пользовательского интерфейса. Существую различные виджеты по своим функциям\свойствам: вывод текста на экран, ввод текста, нажатие кнопки и другие взаимодействия с пользователем. В примере выше `Button`, `TextView` - это лишь разновидности виджетов.