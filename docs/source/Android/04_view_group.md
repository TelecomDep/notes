# 4. Работа ViewGroup
Снова про `root` класс для всех виджетов. 
## View
Android SDK включает множество виджетов, которые являются дочерним классом класса `View`. Таким образом, каждый виджет является экземпляром класса `View`, как и отражено на рисунке ниже. 

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/android_class_hierarchy_view.svg?raw=true )

Рис. 1. Иерархия класса `View`. [Источник изображения](https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/media/vectorart/android_class_hierarchy_view.svg).


## ViewGroup

Макет определяет структуру пользовательского интерфейса в вашем приложении, например в [действии](https://developer.android.com/guide/components/activities?hl=ru) . Все элементы макета построены с использованием иерархии объектов [View](https://developer.android.com/reference/android/view/View?hl=ru) и [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup?hl=ru) . `View` обычно рисует то, что пользователь может видеть и с чем может взаимодействовать. `ViewGroup` — это невидимый контейнер, определяющий структуру макета для `View` и других объектов `ViewGroup` , как показано на рисунке 1.

![](https://developer.android.com/static/images/viewgroup_2x.png?hl=ru)

**Рисунок 1.** Иллюстрация иерархии представлений, определяющей макет пользовательского интерфейса.

Объекты `View` часто называются **_виджетами_** и могут быть одним из многих подклассов, таких как [Button](https://developer.android.com/reference/android/widget/Button?hl=ru) или [TextView](https://developer.android.com/reference/android/widget/TextView?hl=ru) . Объекты `ViewGroup` обычно называются **_макетами_** и могут относиться к одному из многих типов, предоставляющих другую структуру макета, например [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout?hl=ru) или [`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout?hl=ru) .

Объявить макет можно двумя способами:

-   **Объявляйте элементы пользовательского интерфейса в XML.** Android предоставляет простой словарь XML, соответствующий классам и подклассам `View` , например, для виджетов и макетов. Вы также можете использовать [редактор макетов](https://developer.android.com/studio/write/layout-editor?hl=ru) Android Studio для создания макета XML с помощью интерфейса перетаскивания.
    
-   **Создание экземпляров элементов макета во время выполнения.** Ваше приложение может создавать объекты `View` и `ViewGroup` и программно управлять их свойствами.

**Совет:** Для отладки макета во время выполнения используйте инструмент [«Инспектор макета»](https://developer.android.com/studio/debug/layout-inspector?hl=ru) .

## XML

Используя словарь XML Android, вы можете быстро разрабатывать макеты пользовательского интерфейса и элементы экрана, которые они содержат, точно так же, как вы создаете веб-страницы в HTML с рядом вложенных элементов.

Каждый файл макета должен содержать ровно один корневой элемент, который должен быть объектом `View` или `ViewGroup` . После определения корневого элемента вы можете добавить дополнительные объекты или виджеты макета в качестве дочерних элементов, чтобы постепенно построить иерархию `View` , определяющую ваш макет. Например, вот макет XML, в котором используется вертикальный `LinearLayout` для хранения `TextView` и `Button` :
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout\_width="match\_parent"
              android:layout\_height="match\_parent"
              android:orientation="vertical" \>
    <TextView android:id="@+id/text"
              android:layout\_width="wrap\_content"
              android:layout\_height="wrap\_content"
              android:text="Hello, I am a TextView" />
    <Button android:id="@+id/button"
            android:layout\_width="wrap\_content"
            android:layout\_height="wrap\_content"
            android:text="Hello, I am a Button" />
</LinearLayout>
```
После объявления макета в XML сохраните файл с расширением `.xml` в каталоге `res/layout/` вашего проекта Android, чтобы он правильно скомпилировался.

Дополнительные сведения о синтаксисе XML-файла макета см. в [разделе layout-resource](https://developer.android.com/guide/topics/resources/layout-resource?hl=ru) .

### Подключение XML-res

При компиляции приложения каждый файл макета XML компилируется в ресурс `View` . Загрузите ресурс макета в реализацию обратного вызова [Activity.onCreate()](https://developer.android.com/reference/android/app/Activity?hl=ru#onCreate(android.os.Bundle)) вашего приложения. Сделайте это, вызвав [setContentView()](https://developer.android.com/reference/android/app/Activity?hl=ru#setContentView(int)) , передав ему ссылку на ваш ресурс макета в форме: `R.layout. _layout_file_name_` . Например, если ваш XML-макет сохранен как `main_layout.xml` , загрузите его для своей `Activity` следующим образом:
```Kotlin
fun onCreate(savedInstanceState: Bundle) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main_layout)
}
```
Платформа Android вызывает метод обратного вызова `onCreate()` в вашем `Activity` при запуске `Activity` . Дополнительные сведения о жизненных циклах действий см. в [разделе Введение в действия](https://developer.android.com/guide/components/activities?hl=ru#Lifecycle) .

### Атрибуты

Каждый объект `View` и `ViewGroup` поддерживает собственный набор атрибутов XML. Некоторые атрибуты специфичны для объекта `View` . Например, `TextView` поддерживает атрибут `textSize` . Однако эти атрибуты также наследуются любыми объектами `View` , расширяющими этот класс. Некоторые из них являются общими для всех объектов `View` , поскольку они наследуются от корневого класса `View` , например атрибут `id` . Другие атрибуты считаются _параметрами макета_ , которые являются атрибутами, описывающими определенные ориентации макета объекта `View` , как определено родительским объектом `ViewGroup` этого объекта.

### ИДЕНТИФИКАТОР

Любой объект `View` может иметь связанный с ним целочисленный идентификатор, позволяющий однозначно идентифицировать `View` в дереве. При компиляции приложения этот идентификатор упоминается как целое число, но идентификатор обычно назначается в XML-файле макета в виде строки в атрибуте `id` . Это атрибут XML, общий для всех объектов `View` , и он определяется классом `View` . Вы используете его очень часто. Синтаксис идентификатора внутри тега XML следующий:
```xml
android:id="@+id/my\_button"
```
_Символ_ (@) в начале строки указывает, что синтаксический анализатор XML анализирует и расширяет остальную часть строки идентификатора и идентифицирует ее как ресурс идентификатора. Символ _плюса_ (`+`) означает, что это новое имя ресурса, которое необходимо создать и добавить к вашим ресурсам в файле `R.java` .

Платформа Android предлагает множество других ресурсов для идентификации. При ссылке на идентификатор ресурса Android вам не нужен символ _плюса_ , но вы должны добавить пространство имен пакета `android` следующим образом:

```xml
android:id="@android:id/empty"
```

Пространство имен пакета `android` указывает, что вы ссылаетесь на идентификатор из класса ресурсов `android.R` , а не из класса локальных ресурсов.

Чтобы создавать `View` и ссылаться на них из вашего приложения, вы можете использовать следующий общий шаблон:

1.  Определите представление в файле макета и присвойте ему уникальный идентификатор, как в следующем примере:
```xml
    <Button android:id="@+id/my\_button"
            android:layout\_width="wrap\_content"
            android:layout\_height="wrap\_content"
            android:text="@string/my\_button\_text"/>
```  
2.  Создайте экземпляр объекта представления и запишите его из макета, обычно с помощью метода [onCreate()](https://developer.android.com/reference/android/app/Activity?hl=ru#onCreate(android.os.Bundle)) , как показано в следующем примере:

```Kotlin
val myButton: Button = findViewById(R.id.my_button)
```
Определение идентификаторов для объектов представления важно при создании [RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout?hl=ru) . В относительном макете родственные представления могут определять свой макет относительно другого родственного представления, на которое ссылается уникальный идентификатор.

Идентификатор не обязательно должен быть уникальным во всем дереве, но он должен быть уникальным в той части дерева, в которой вы ищете. Часто это может быть все дерево, поэтому лучше сделать его уникальным, если это возможно.

### Параметры макета

Атрибуты макета XML с именем `layout_ _something_` определяют параметры макета для `View` , соответствующие `ViewGroup` , в которой оно находится.

Каждый класс `ViewGroup` реализует вложенный класс, расширяющий [ViewGroup.LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams?hl=ru) . Этот подкласс содержит типы свойств, которые определяют размер и положение каждого дочернего `View` в зависимости от `ViewGroup`. Как показано на рисунке 2, родительская `ViewGroup`й определяет параметры макета для каждого дочернего `View`, включая дочернюю `ViewGroup`.

![](https://developer.android.com/static/images/layoutparams.png?hl=ru)

**Рисунок 2.** Визуализация иерархии `View` с параметрами макета, связанными с каждым `View`.

Каждый подкласс `LayoutParams` имеет свой собственный синтаксис для установки значений. Каждый дочерний элемент должен определять `LayoutParams` , соответствующий его родительскому элементу, хотя он также может определять разные `LayoutParams` для своих собственных дочерних элементов.

Вы можете указать ширину и высоту с точными измерениями, но, возможно, вам не захочется делать это часто. Чаще всего вы используете одну из этих констант для установки ширины или высоты:

-   `wrap_content` : сообщает вашему `View`, что его размер соответствует размерам, требуемым его содержимым.
-   `match_parent` : сообщает вашему `View`, что оно должно стать настолько большим, насколько позволяет его родительская `ViewGroup`.

Как правило, мы не рекомендуем указывать ширину и высоту макета в абсолютных единицах, таких как пиксели. Лучшим подходом является использование относительных измерений, таких как независимые от плотности пиксельные единицы (dp), `wrap_content` или `match_parent` , поскольку это помогает вашему приложению правильно отображаться на экранах различных размеров. Принятые типы измерений определены в [ресурсе макета](https://developer.android.com/guide/topics/resources/layout-resource?hl=ru) .

## Положение макета

`View` имеет прямоугольную геометрию. Он имеет местоположение, выраженное как пара **_левой_** и **_верхней_** координат, и два измерения, выраженные как ширина и высота. Единицей местоположения и размеров является пиксель.

Вы можете получить местоположение представления, вызвав методы [getLeft()](https://developer.android.com/reference/android/view/View?hl=ru#getLeft()) и [getTop()](https://developer.android.com/reference/android/view/View?hl=ru#getTop()) . Первый возвращает левую координату ( _x_ ) прямоугольника, представляющего `View`. Последний возвращает верхнюю координату ( _y_ ) прямоугольника, представляющего `View`. Эти методы возвращают расположение `View` относительно его родителя. Например, когда `getLeft()` возвращает 20, это означает, что представление расположено на 20 пикселей правее левого края его прямого родительского элемента.

Кроме того, существуют удобные методы, позволяющие избежать ненужных вычислений: а именно [getRight()](https://developer.android.com/reference/android/view/View?hl=ru#getRight()) и [getBottom()](https://developer.android.com/reference/android/view/View?hl=ru#getBottom()). Эти методы возвращают координаты правого и нижнего краев прямоугольника, представляющего `View`. Например, вызов `getRight()` аналогичен следующему вычислению: `getLeft() + getWidth()` .

<!-- ## Размер, отступы и поля

Размер представления выражается шириной и высотой. Представление имеет две пары значений ширины и высоты.

Первая пара известна как _измеренная ширина_ и _измеренная высота_ . Эти размеры определяют, насколько большим должно быть представление внутри своего родителя. Вы можете получить измеренные размеры, вызвав методы [getMeasuredWidth()](https://developer.android.com/reference/android/view/View?hl=ru#getMeasuredWidth()) и [getMeasuredHeight()](https://developer.android.com/reference/android/view/View?hl=ru#getMeasuredHeight()).

Вторая пара известна как _ширина_ и _высота_ или иногда _ширина_ и _высота_ рисунка. Эти размеры определяют фактический размер представления на экране, во время рисования и после компоновки. Эти значения могут, но не обязательно, отличаться от измеренных ширины и высоты. Вы можете получить ширину и высоту, вызвав [getWidth()](https://developer.android.com/reference/android/view/View?hl=ru#getWidth()) и [getHeight()](https://developer.android.com/reference/android/view/View?hl=ru#getHeight()).

Чтобы измерить свои размеры, представление учитывает его отступы. Заполнение выражается в пикселях для левой, верхней, правой и нижней частей представления. Вы можете использовать отступы, чтобы сместить содержимое представления на определенное количество пикселей. Например, левое заполнение, равное двум, смещает содержимое представления на два пикселя вправо от левого края. Вы можете установить заполнение с помощью метода [setPadding(int, int, int, int)](https://developer.android.com/reference/android/view/View?hl=ru#setPadding(int,%20int,%20int,%20int)) и запросить его, вызвав [getPaddingLeft()](https://developer.android.com/reference/android/view/View?hl=ru#getPaddingLeft()) , [getPaddingTop()](https://developer.android.com/reference/android/view/View?hl=ru#getPaddingTop()), [getPaddingRight()](https://developer.android.com/reference/android/view/View?hl=ru#getPaddingRight()) и [getPaddingBottom()](https://developer.android.com/reference/android/view/View?hl=ru#getPaddingBottom()).

Хотя представление может определять отступы, оно не поддерживает поля. Однако группы представлений поддерживают поля. Дополнительные сведения см. [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup?hl=ru) и [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams?hl=ru)` .

Дополнительные сведения о размерах см. в разделе [Размер](https://developer.android.com/guide/topics/resources/more-resources?hl=ru#Dimension) .

Помимо программной настройки полей и отступов, вы также можете установить их в макетах XML, как показано в следующем примере:
```xml
  <?xml version\="1.0" encoding\="utf-8"?>  
<LinearLayout xmlns:android\="http://schemas.android.com/apk/res/android"                   android:layout\_width\="match\_parent"                
android:layout\_height\="match\_parent"                
android:orientation\="vertical" \>      
    <TextView android:id\="@+id/text"                
            android:layout\_width\="wrap\_content"                
            android:layout\_height\="wrap\_content"               
            **android:layout\_margin\="16dp"                
            android:padding\="8dp"**                
            android:text\="Hello, I am a TextView" />      
    <Button android:id\="@+id/button"              
            android:layout\_width\="wrap\_content"              
            android:layout\_height\="wrap\_content"              
            **android:layout\_marginTop\="16dp"              
            android:paddingBottom\="4dp"              
            android:paddingEnd\="8dp"              
            android:paddingStart\="8dp"              
            android:paddingTop\="4dp"**              
            android:text\="Hello, I am a Button" />  
 </LinearLayout>  
```
В предыдущем примере показано применение полей и отступов. `TextView` имеет одинаковые поля и отступы, а `Button` показывает, как можно применять их независимо к разным краям.

**Примечание.** Рекомендуется использовать `paddingStart` , `paddingEnd` , `layout_marginStart` и `layout_marginEnd` вместо `paddingLeft` , `paddingRight` , `layout_marginLeft` и `layout_marginRight` , поскольку они лучше работают как с языковыми скриптами с письмом слева направо, так и с письмом справа налево.

## Общие макеты

Каждый подкласс класса `ViewGroup` предоставляет уникальный способ отображения вложенных в него представлений. Самый гибкий тип макета и тот, который предоставляет лучшие инструменты для поддержания мелкой иерархии макетов, — это [ConstraintLayout](https://developer.android.com/develop/ui/views/layout/constraint-layout?hl=ru) .

Ниже приведены некоторые распространенные типы макетов, встроенные в платформу Android.

**Примечание.** Хотя вы можете вложить один или несколько макетов в другой макет для достижения желаемого дизайна пользовательского интерфейса, сохраняйте иерархию макетов как можно более мелкой. Ваш макет прорисовывается быстрее, если в нем меньше вложенных макетов. Иерархия широкого представления лучше, чем иерархия глубокого представления.

**[Линейный макет](https://developer.android.com/develop/ui/views/layout/linear?hl=ru)**

[![](https://developer.android.com/static/images/ui/linearlayout-small.png?hl=ru)](https://developer.android.com/develop/ui/views/layout/linear?hl=ru)

Организует дочерние элементы в одну горизонтальную или вертикальную строку и создает полосу прокрутки, если длина окна превышает длину экрана.

**[Создание веб-приложений в WebView](https://developer.android.com/guide/webapps/webview?hl=ru)**

[![](https://developer.android.com/static/images/ui/webview-small.png?hl=ru)](https://developer.android.com/guide/webapps/webview?hl=ru)

Отображает веб-страницы.

## Динамические списки

Если содержимое вашего макета является динамическим или не определено заранее, вы можете использовать [RecyclerView](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru) или подкласс [AdapterView](https://developer.android.com/develop/ui/views/layout/binding?hl=ru). `RecyclerView` обычно является лучшим вариантом, поскольку он использует память более эффективно, чем `AdapterView` .

Общие макеты, возможные с помощью `RecyclerView` и `AdapterView` включают следующее:

**[Список](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru)**

[![](https://developer.android.com/static/images/ui/listview-small.png?hl=ru)](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru)

Отображает прокручиваемый список из одного столбца.

**[Сетка](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru)**

[![](https://developer.android.com/static/images/ui/gridview-small.png?hl=ru)](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru)

Отображает прокручиваемую сетку столбцов и строк.

`RecyclerView` предлагает больше возможностей и возможность [создать собственный менеджер макетов](https://developer.android.com/develop/ui/views/layout/recyclerview?hl=ru#plan-your-layout) .

### Заполнение представления адаптера данными

Вы можете заполнить [AdapterView](https://developer.android.com/reference/android/widget/AdapterView?hl=ru) , такой как [ListView](https://developer.android.com/reference/android/widget/ListView?hl=ru) или [GridView](https://developer.android.com/reference/android/widget/GridView?hl=ru) путем привязки экземпляра `AdapterView` к [Adapter](https://developer.android.com/reference/android/widget/Adapter?hl=ru), который извлекает данные из внешнего источника и создает `View` , представляющее каждую запись данных.

Android предоставляет несколько подклассов `Adapter` , которые полезны для получения различных типов данных и построения представлений для `AdapterView` . Два наиболее распространенных адаптера:

[ArrayAdapter](https://developer.android.com/reference/android/widget/ArrayAdapter?hl=ru)

Используйте этот адаптер, если источником данных является массив. По умолчанию `ArrayAdapter` создает представление для каждого элемента массива, вызывая [toString()](https://developer.android.com/reference/java/lang/Object?hl=ru#toString()) для каждого элемента и помещая содержимое в `TextView` .

Например, если у вас есть массив строк, который вы хотите отобразить в `ListView` , инициализируйте новый `ArrayAdapter` , используя конструктор, чтобы указать макет для каждой строки и массива строк:


```Kotlin
val adapter = ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, myStringArray)
```
    

Аргументы этого конструктора следующие:

-   [Context](https://developer.android.com/reference/android/content/Context?hl=ru) вашего приложения
-   Макет, содержащий `TextView` для каждой строки в массиве.
-   Строковый массив

Затем вызовите [setAdapter()](https://developer.android.com/reference/android/widget/AdapterView?hl=ru#setAdapter(T)) в вашем `ListView` :

```Kotlin
val listView: ListView = findViewById(R.id.listview)
listView.adapter = adapter
```
    

Чтобы настроить внешний вид каждого элемента, вы можете переопределить метод `toString()` для объектов вашего массива. Или, чтобы создать представление для каждого элемента, отличное от `TextView` (например, если вам нужен [ImageView](https://developer.android.com/reference/android/widget/ImageView?hl=ru) для каждого элемента массива), расширьте класс `ArrayAdapter` и переопределите [getView()](https://developer.android.com/reference/android/widget/ArrayAdapter?hl=ru#getView(int,%20android.view.View,%20android.view.ViewGroup)) , чтобы он возвращал тип представления, который вы хотите для каждого элемента.

[SimpleCursorAdapter](https://developer.android.com/reference/android/widget/SimpleCursorAdapter?hl=ru)

Используйте этот адаптер, если ваши данные поступают из [Cursor](https://developer.android.com/reference/android/database/Cursor?hl=ru) . При использовании `SimpleCursorAdapter` укажите макет, который будет использоваться для каждой строки `Cursor` , и какие столбцы `Cursor` вы хотите вставить в представления нужного макета. Например, если вы хотите создать список имен и номеров телефонов людей, вы можете выполнить запрос, который возвращает `Cursor` , содержащий строку для каждого человека и столбцы для имен и номеров. Затем вы создаете массив строк, указывающий, какие столбцы из `Cursor` вы хотите разместить в макете для каждого результата, и целочисленный массив, указывающий соответствующие представления, в которых необходимо разместить каждый столбец:
```Kotlin
    val fromColumns \= arrayOf(ContactsContract.Data.DISPLAY\_NAME,
                              ContactsContract.CommonDataKinds.Phone.NUMBER)
    val toViews \= intArrayOf(R.id.display\_name, R.id.phone\_number)
  ```  
    

Когда вы создаете экземпляр `SimpleCursorAdapter` , передайте макет, который будет использоваться для каждого результата, `Cursor` , содержащий результаты, и эти два массива:

```Kotlin
val adapter \= SimpleCursorAdapter(this,
        R.layout.person\_name\_and\_number, cursor, fromColumns, toViews, 0)
val listView \= getListView()
listView.adapter \= adapter
```
    

Затем `SimpleCursorAdapter` создает представление для каждой строки в `Cursor` , используя предоставленный макет, вставляя каждый элемент `fromColumns` в соответствующее представление `toViews` .

Если в течение жизни вашего приложения вы измените базовые данные, считываемые вашим адаптером, вызовите [notifyDataSetChanged()](https://developer.android.com/reference/android/widget/ArrayAdapter?hl=ru#notifyDataSetChanged()) . Это уведомляет присоединенное представление о том, что данные были изменены, и оно обновляется.

### Обработка событий кликов

Вы можете реагировать на события щелчка по каждому элементу в `AdapterView` , реализуя интерфейс [AdapterView.OnItemClickListener](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener?hl=ru) . Например:

```Kotlin
listView.onItemClickListener \= AdapterView.OnItemClickListener { parent, view, position, id \-\>
    // Do something in response to the click.
}

``` -->