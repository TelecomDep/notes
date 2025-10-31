# Работа виджетами из Activity
Снова про `root` класс для всех виджетов. 
## View
Android SDK включает множество виджетов, которые являются дочерним классом класса `View`. Таким образом, каждый виджет является экземпляром класса `View`, как и отражено на рисунке ниже. 

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/android_class_hierarchy_view.svg?raw=true )

Рис. 1. Иерархия класса `View`. [Источник изображения](https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/media/vectorart/android_class_hierarchy_view.svg).


**Основные Операции с View**

1. **Set Properties** - можем задать свойства для каждого объекта класса View и его наследников;
2. **Set focus** - "фокусировка" объекта, например, если нужно ввести текст в нужное вам `TextView`;
3. **Set up Listeners** - "навесить" слушателя (`интерфейс`) для выполнения необходимых функций\действий при взаимодействии с объектом;
4. **Set Visibility** - спрятать или показать объект.

<!-- ## Создание нового Activity

Для начала, создадим новое `Activity`, в котором будем создавать виджеты и работать из `Activity`.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_05_create_new_activity.png?raw=true )

Рис. 2. Создание нового `Activity`.

Далее, вам откроется окно с настройками нового `Activity`. Необходимо ввести имя и поставить галочку на автоматическое создание файла `layout` для `Activity`.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/basic_05_create_new_activity_naming.PNG?raw=true )

Рис. 3. Настройка нового `Activity`.

Замем вы увидите изменения в структуре проекта: добавится файл с кодом `имя_класса.kt`, появится к нему файл `имя_layout.xml`. Также, не мало важным является добавление `Activity` в файл `AndroidManifest.xml`, который является **основой** вашего проекта.

Содержание файла `AndroidManifest.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.Android_notes"
        tools:targetApi="31">
        <activity
            android:name=".activities.ViewExamples"
            android:exported="false" />
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
``` -->

### Атрибуты (Properties)

Атрибуты View помогают изменять вид элементов на экране. В качестве базовых атрибутов можно перечислить следующие:
- `id` - id объекта;
- `text` - текст;
- `visibility` - видимость объекта;
- `textSize` - размер текста;
- `paddingTop` - отступ контента от верхнего края прямоугольника;
- `layout_height/layout_width` - высота/ширина виджета;
- `layout_marginTop/layout_marginBottom/…` - отступы для различных сторон виджета;
- `background color` - задать цвет фона `view`.


<!-- Корневым элементом иерархии представлений в этом макете является элемент `ConstraintLayout`. В нем должно быть указано пространство имен XML ресурсов Android http://schemas.android.com/apk/res/android. `ConstraintLayout` наследует от дочернего класса `View` с именем `ViewGroup`. Виджет `ViewGroup` предназначен для хранения и размещения других виджетов. LinearLayout используется в тех случаях, когда вы хотите выстроить виджеты в один столбец или строку. Другие дочерние классы `ViewGroup` — `FrameLayout`, `TableLayout` и `RelativeLayout`.

Если виджет содержится в `ViewGroup`, он называется потомком (child) `ViewGroup`. Корневой элемент `ConstraintLayout` имеет двух потомков: `TextView` и другой элемент `Button`. -->

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

Где мы можем увидеть наше новое `Activity` в списке проекта.

## Переход между Activity (Intent, вкратце)

В рамках "удобства" по работе с несколькими `Activity` рассмотрим небольшой пример работы класса [Intent]()

`Intent` — это абстрактное описание операции, которая должна быть выполнена. Его можно использовать с [startActivity](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) для запуска [Activity](https://developer.android.com/reference/android/app/Activity), [broadcastIntent](https://developer.android.com/reference/android/content/Context#sendBroadcast(android.content.Intent)) для отправки его любым заинтересованным компонентам [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) и [Context.startService(Intent)](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)) или [Context.bindService(Intent, BindServiceFlags, Executor, ServiceConnection)](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent,%20android.content.Context.BindServiceFlags,%20java.util.concurrent.Executor,%20android.content.ServiceConnection)) для связи с фоновой службой [Service](https://developer.android.com/reference/android/app/Service).

Для начала, нам понадобится только метод `startActivity()`. Добавим переход на другое `Activity` при помощи `Button` во время нажатия (`setOnClickListener`).
Добавим кнопку в файле `activity_имя.xml`:

```xml
<Button
    android:id="@+id/bViews"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Views" />
```

Инициализируем кнопку в коде `ИМЯ_Activity.kt`, выделяя память под кнопку в методе `onCreate()`, инициализируя обработчик нажатия на кнопку в методе `onResume()` (когда `Activity` уже видна пользователю):

```Kotlin
class MainActivity : AppCompatActivity() {

    private lateinit var bViewExamples: Button

    // onCreate() – вызывается при первом создании Activity
    override fun onCreate(savedInstanceState: Bundle?) {

        ...
        ...
        bViewExamples = findViewById<Button>(R.id.bViews)
    }

    override fun onResume() {
        super.onResume()
        bViewExamples.setOnClickListener({
            val randomIntent = Intent(this, ViewExamples::class.java)
            startActivity(randomIntent)
        });
    }
```
Из обработчика нажатия мы видим создание экземпляра класса `Intent`, используя конструктор `public Intent(Context packageContext, Class<?> cls)`:

```Kotlin
val randomIntent = Intent(this, ViewExamples::class.java)
startActivity(randomIntent)
```

Согласно документации аргументами функции являются:
```
Создание `Intent` для определенного компонента.  Это обеспечивает удобный способ создания `Intent`, которое предназначено для выполнения `hard-coded` класса.

Params:
packageContext – A Context of the application package implementing this class. 
cls – The component class that is to be used for the intent.
```

Первый параметр – это `Context`. `Activity` является подклассом `Context`, можем использовать запись `ИМЯ_КЛАССА_В_КОТОРОМ_НАХОДИМСЯ.this`, или укороченную запись `this`.

Метод `startActivity(randomIntent)` выполняет переход на необходимый нам класс, т.е. `Activity`.


## Виджеты (Views)

### findViewById()
Метод `findViewById()` возвращает объект класса `View` по его идентификатору на разметке (какой то из виджетов, например кнопку). Теперь, имея данный экземпляр **виджета**, вы можете вызывать реализованные для него методы, такие как изменение размеров, цвета, текста и т.п. Метод работает таким образом, что получает этот объект из предварительно подготовленного через инфлейт (парсинг разметки) и сгенерированного на его основе класса R нужный нам виджет из дерева объектов отображаемых на экране.

### TextView

**Инициализация**

В рамках `.xml-layout`'а добавляем след. образом:

```xml
    <TextView
        android:id="@+id/textView"
        android:layout_width="130dp"
        android:layout_height="0dp"
        android:layout_marginStart="20dp"
        android:layout_marginBottom="579dp"
        android:text="TextView"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/button_back_to_main" />
```

В коде Kotlin мы должны воспользоваться классом `TextView`, импортировав его из `import android.widget.TextView`. 

Инициализация в коде и работа с конкретным обхъектом `View` происходит при помощи метода findVewiById():
```Kotlin
private lateinit var tvView_01: TextView
tvView_01 = findViewById(R.id.textView)
```
#### Атрибуты
Список основных атрибутов:
||

**Программное изменение текста**

Программно можно изменить наполнение TextView при помощи метода класса: `setText(CharSequence text)`:
```Kotlin
tvView_01.setText("Hello from Code")
```

**Изменение размера текста**

Приведем лишь 2 примера с установлением размера текста:
```Kotlin
// COMPLEX_UNIT_PX - Value is raw pixels                
tvView_01.setTextSize(TypedValue.COMPLEX_UNIT_PX, 10F)  
// COMPLEX_UNIT_DIP - Value is Device Independent Pixels
tvView_01.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20F) 
```

Остальные возможные типы значений размера текста можно увидеть в классе `TypedValue.java`:
```Java
    /** complex unit: Value is raw pixels. */
    public static final int COMPLEX_UNIT_PX = 0;
    /** complex unit: Value is Device Independent Pixels. */
    public static final int COMPLEX_UNIT_DIP = 1;
    /** complex unit: Value is a scaled pixel. */
    public static final int COMPLEX_UNIT_SP = 2;
    /** complex unit: Value is in points. */
    public static final int COMPLEX_UNIT_PT = 3;
    /** complex unit: Value is in inches. */
    public static final int COMPLEX_UNIT_IN = 4;
    /** complex unit: Value is in millimeters. */
    public static final int COMPLEX_UNIT_MM = 5;
```

**Изменение цвета текста**

```Kotlin                      
tvView_01.setTextColor(Color.rgb(255,192,0))    
```
![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/widgets/set_text_size.PNG?raw=true )


**Возможность нажать на TextView**

Если вы хотите, чтобы `TextView` обрабатывал нажатия (атрибут `android:onClick`), то не забывайте также использовать в связке атрибут `android:clickable="true"` (в файле layout/*.xml). Иначе работать не будет!

```Kotlin
// Возможность нажать на кнопку                           
tvView_01.setOnClickListener({                             
  tvView_01.setTextColor(Color.rgb(55,12,0))              
})                                                         
```
Меняем цвет текста при нажатии на `TextView`.

![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/widgets/set_onclick_listener.PNG?raw=true )


### Button

Наследуется от `TextView`и является базовым классом для класса `СompoundButton`. От класса `CompoundButton` в свою очередь, наследуются такие элементы как `CheckBox`, `ToggleButton` и `RadioButton`. В Android для кнопки используется класс `android.widget.Button`. На кнопке располагается текст и на кнопку нужно нажать, чтобы получить результат.

**Инициализация**

В рамках `.xml-layout`'а добавляем след. образом:

```xml
    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginEnd="99dp"
        android:text="Button"
        app:layout_constraintBottom_toBottomOf="@+id/textView"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toEndOf="@+id/textView" />
```
**Три способа обработать нажатие на кнопку**

#### Первый, атрибут - onClick

Добавляем указатель на нашу функцию обработки нажатия на кнопку в атрибуты `Button`:
```xml
android:onClick="customOnClick"
```

В коде добавим функцию:
```Kotlin
fun customOnClick(v: View?){
    bExample.setText("1st method")
}
```

#### Второй, метод - setOnClickListener()

В данном случае можно задать обработку нажатия для конкретной кнопки отдельно:
```Kotlin
bExample2.setOnClickListener({
    bExample2.setText("2nd method")
})
```


#### Третий, интерфейс - OnClickListener()

В этом случае необходимо сначала добавить интерфейс `View.OnClickListener` к текущему классу, затем `override` метод обработки нажатий `onClick` для всех кнопок текущего класса `Activity`:

```Kotlin
class ViewExamples : AppCompatActivity(), View.OnClickListener {

    override fun onCreate(savedInstanceState: Bundle?) {...}

    override fun onClick(v: View?){
        bExample3.setText("3dr method")
    }
}
```

Далее, можем указать обработчику на интерфейс текущего класса:

```Kotlin
bExample3.setOnClickListener(this)
```
![alt text](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/android/widgets/buttons.PNG?raw=true )


### SeekBar (Слайдер)

### ListView

Для визуализации списка элементов на экране нам понадобится класс (или его наследники) `android.widget.AdapterView` (наследники: `ListView`, `GridView`, `Spinner` и т.д.).

![1761877535959](image/05_widgets/1761877535959.png)

Для связывания списка `ListView` понадобится "помощник", который создать отдельное `TextView` для каждого элемента списка данных, предоставленных обычным массивом (`arrayOf`). Соответственно, для корректного отображения списка элементов экрана необходимо 3 компонента:
1. Класс `ListView`\`GridView`;
2. `AdapterView` (наследник: `ArrayAdapter`);
3. **Источник данных** - `Array` (или что-то другое).

<!-- При работе со списками мы имеем дело с тремя компонентами. Во-первых, это визуальный элемент или виджет, который на экране представляет список (`ListView`, `GridView`) и который отображает данные. Во-вторых, это источник данных - массив, объект ArrayList, база данных и т.д., в котором находятся сами отображаемые данные. И в-третьих, это адаптер - специальный компонент, который связывает источник данных с виджетом списка. -->

**ArrayAdapter**
Для отображения списка элементов на экране потребуется класс `ArrayAdapter`, который, в свою очередь, связывает массив данных с набором элементов TextView, из которых, к примеру, может состоять `ListView`. В данном случае `ArrayAdapter` вызовет метод у каждого элемента массива `.toString()`, а затем выполнит к элементу `TextView` метод `.setText()`, отобразив значение массива на `TextView`.

**Пример**

**XML**
```xml
    <ListView
        android:id="@+id/myFirstListView"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="1.0"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView"
        app:layout_constraintVertical_bias="0.0" />
```

**Kotlin**
```kotlin
private lateinit var lvMyList: ListView
override fun onCreate(savedInstanceState: Bundle?) {
    ...
    lvMyList = findViewById(R.id.myFirstListView)
    val my_array = arrayOf(
            "1", "2", "10", "Привет", "HelloWorld", "Stroka"
        )
    val adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_1, my_array
        )
    lvMyList.adapter = adapter

}
```
При создании ArrayAdapter использовали конструктор `public ArrayAdapter(@NonNull Context context, @LayoutRes int resource, @NonNull T[] objects)`, где:
- **context** The current context;
- **resource** The resource ID for a layout file containing a layout to use when instantiating views;
- **objects** The objects to represent in the ListView.

В нашем случае это:
 - **this** : текущий объект класса `Activity`;
 - **android.R.layout.simple_list_item_1** - файл разметки списка **по умолчанию**.Он находится в папке `Android SDK` по пути `platforms/[android-номер_версии]/data/res/layout`;
 - **my_array** - массив из строковых значений, который мы хотим отобразить на экране.
 
` lvMyList.adapter = adapter` - это связывание `ArrayAdapter` с `ListView`.

**Обработчик нажатия** на элемент `ListView`:
```
lvMyList.setOnItemClickListener(OnItemClickListener { parent, view, position, id ->
            view.setBackgroundColor(Color.rgb(255, 22, 10))
        })
```
В итоге, **получили**:

![1761878990149](image/05_widgets/1761878990149.png)
