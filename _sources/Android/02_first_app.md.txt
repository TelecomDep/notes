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

## Структура проекта
В открывшемся проекте мы увидмим структуру:

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_02_project_structure.PNG?raw=true)

Рис. 4. Стркутура проекта.

Вкратце, проект состоит из нескольких важный директорий:
-  `/app` включает в себя еще 3 директории:
    - `/manifest` - содержит файлы конфигурации\\манифеста приложения (ключевой файл в приложении Android);
    - `/kotlin` + java - содержит исходный код приложения;
    - `/res` - включает в себя файлы, используемые приложением Android (картинки, иконки, стили, музыка и т.д.);
- `/Gradle Scripts`. 

### AndroidManifests.xml

Файл `AndroidManifest.xml` является одним из самых важных в Android проекте. В нем содержится информация о пакетах приложения, компонентах типа `Activity`, `Service` и т.д..
Файл `AndroidManifest.xml` выполняет следующие задачи:

- Предоставляет разрешения приложению на использование или доступ к другим компонентам системы.
- Определяет как будут запускаться, например, Activity (какие фильтры использовать).

### /res 

В папке `/res` расположены все используемые приложением ресурсы, включая изображения, различные xml файлы, анимации, звуковые файлы и многие другие. Внутри папки **res** эти все ресурсы распределены по своим папкам:

- Папка  `/drawable` содержит файлы с изображениями, которые будет использоваться в приложении;
- Папка `/layout` располагает xml файлами, которые используются для построения пользовательского интерфейса Android приложения;
- В папке `/menu` находятся xml файлы, используемые только для создания меню;
- В  `/mipmap` папке хранят только значки приложения. Любые другие drawable элементы должны быть размещены в своей папке;
- `/values` хранит те xml файлы, в которых определяются простые значения типа строк, массивов, целых чисел, размерностей, цветов и стилей.

### Gradle  

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

### View
Android SDK включает множество виджетов, которые являются дочерним классом класса `View`. Таким образом, каждый виджет является экземпляром класса `View`, как и отражено на рисунке ниже. 

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/android_class_hierarchy_view.svg?raw=true )

Рис. 6. Иерархия класса `View`. [Источник изображения](https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/media/vectorart/android_class_hierarchy_view.svg).

В нашем примере, на рис. 5 показан экран с виджетами `ConstraintLayout`, `TextView` и `Button`, которые мы можем увидеть в иерархии родительского класса.

#### Атрибуты View

Атрибуты View помогают изменять вид элементов на экране. В качестве базовых атрибутов можно перечислить следующие:
- `id` - id объекта
- `text` - текст
- `visibility` - видимость объекта
- `textSize` - размер текста
- `paddingTop` - отступ контента от верхнего края прямоугольника
- `layout_height/layout_width` - высота/ширина виджета
- `layout_marginTop/layout_marginBottom/…` - отступы для различных сторон виджета

#### Иерархия представлений виджетов
В качестве примера возьмем **Листинг 1**. Все виджеты в `Activity` входят в **иерархию представлений**. 


```{mermaid}

flowchart TD 
    ConstraintLayout["`**ConstraintLayout**
    xmlns:android=http..//schemas.android.com/apk/res/android
    android:id=@+id/main
    android:layout_width=match_parent
    android:layout_height=match_parent
    tools:context=.MainActivity`"]
    TextView["`**TextView**
    android:id=@+id/textView2
    android:layout_width=wrap_content
    android:layout_height=wrap_content
    android:text=Hello World!
    ...`"]
    Button["`**Button**
    android:id=@+id/go_to_second_activity
    android:layout_width=wrap_content
    android:layout_height=wrap_content
    android:text=SecondActivity
    ...`"]

    style ConstraintLayout text-align:left
    style TextView text-align:left
    style Button text-align:left

    ConstraintLayout --> TextView
    ConstraintLayout --> Button
```
Рис. 3. Иерархия представлений виджетов и атрибутов `Activity`.

Корневым элементом иерархии представлений в этом макете является элемент `ConstraintLayout`. В нем должно быть указано пространство имен XML ресурсов Android http://schemas.android.com/apk/res/android. `ConstraintLayout` наследует от дочернего класса `View` с именем `ViewGroup`. Виджет `ViewGroup` предназначен для хранения и размещения других виджетов. LinearLayout используется в тех случаях, когда вы хотите выстроить виджеты в один столбец или строку. Другие дочерние классы `ViewGroup` — `FrameLayout`, `TableLayout` и `RelativeLayout`.

Если виджет содержится в `ViewGroup`, он называется потомком (child) `ViewGroup`. Корневой элемент `ConstraintLayout` имеет двух потомков: `TextView` и другой элемент `Button`. 

## Управление виджетами из кода Kotlin (один из способов)

По умолчанию, при создании проекта, мы получаем от Android Studio файлы `activity_main.xml` и `MainActivity.kt` (при создании проекта можно изменить название). В `.xml` файле мы уже определили элементы экрана: `TextView`, `Button`. Далее, нам нужно научиться взаимодействовать с ними. 

При создании первого приложения в `Android Studio` мы получаем код из **листинга №2**.
Взаимодействие нашего кода и объектов интерфейса (определенных в файле `.xml`, далее компилируемые в объекты `View`). 

Для начала, `Activity` необходимо подружить с элементами в файле `.xml`. При создании проекта, по умолчанию в `Empty Views Acitvity`, ресурсы .xml загружаются автоматически:

```kotlin
setContentView(R.layout.activity_main) // activity_main.xml
```

Именно в этом моменте решается какой именно визуальный интерфейс будет иметь пользовательский интерфейс. В данном случае предоставляется **ресурс** `R.layout.activity_main`, что является файлом в папке `res/layout/activity_main.xml`.

Из **листинга №1** можно заметить один важнй параметр элементов экрана -`"@+id`, идентификатор элемента. Данный идентификатор позволяет обращаться к элементу экрана, который определен в файле `.xml`. 

Для получения элементов класса по `id` класс Activity имеет метод [`findViewById()`](https://developer.android.com/reference/android/view/View#findViewById(int)). 
```
Finds the first descendant view with the given ID, the view itself if the ID matches getId(), or null if the ID is invalid (< 0) or there is no matching view in the hierarchy.
```
В этот метод передается идентификатор ресурса в виде `R.id` - идентификатор элемента, который был создан с файле `.xml`. Также, необходимо привести возвращаемый тип данных (View) к нужному нам классу (`TextView`, `Button` или др.). 

Листинг 3. MainActivity.kt (с добавлением виджетов)
```kotlin
class MainActivity : AppCompatActivity() {

    // onCreate() – вызывается при первом создании Activity
    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Инициализация переменных для элементов экрана.
        var mTextView = findViewById<TextView>(R.id.textView2)
        var bGoToSecondActivity = findViewById<Button>(R.id.go_to_second_activity)

    }
}
```
Таким образом, появляется возможность управлять элементами экрана из кода приложения.
Например, можем поменять содержание текстового элемента (`TextView`):
```kotlin
mTextView.setText("Hello from code Kotlin!");
```
Аналогично, можно возпользоваться методом обработки нажатия на элемент `View`, используя метод `setOnClickListener`:

```
bGoToSecondActivity.setOnClickListener({
            mTextView.setText("Hello from clicked Button!");
        });
```