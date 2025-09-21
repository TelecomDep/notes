# Основы Объектно-ориентированного программирования в Kotlin

## Классы и объекты

Инициализация **классов** в языке Kotlin производится при помощи ключевого слова `class`: 

```kotlin
class Human{
    // внутренности Human'a
}
```
Объявление класса состоит из его **имени**, **заголовка класса** (задавая свойства класса, первичный конструктор и т.д.) и **тела класса**, заключенного в фигурные скобки `{}`.

Класс также может быть пустым:

```kotlin
class EmptyHuman
```
## Конструкторы

В Kotlin есть **первичный** (`primary constructor`) и один или несколько **вторичных** констукторов (`secondary constructor`).

### Первичный
```kotlin
class Human constructor(addName: String){
    var name: String = addName
}
```
Если primary `constructor` не имеет перед объявлением аннотаций или модификаторов видимости (`visibility modifiers`), можно опустить ключевое слово `constructor`:

```kotlin
// Если есть модификатор доступа
class HumanConstr private constructor (addName: String){
    var name: String = addName
}

// БЕЗ
class Human(addName: String){
    var name: String = addName
}
```

**Нюансы primary constructor**
По умолчанию, он инициализирует **только** `объект класса` и его `свойства` (переменные класса). Если хотим что-то в виде `runnable`-функции, нужно добавить `init{}`:

```kotlin
class Human constructor(addName: String){
    var name: String = addName

    init {
        name = addName.uppercase()
    }
}
```

### Вторичные

Если для класса определен первичный конструктор, то вторичный конструктор должен вызывать первичный с помощью ключевого слова `this`:

```kotlin
class Human(addName: String){
    var name: String = addName
    var age: Int = 0

    constructor(addName: String, addAge: Int): this(addName){
        age = addAge
    }
}
```

Вызываем стандартно:

```kotlin
fun main(){ // Точка входа в программу

    var tom = Human("Tom")      // Первичные конструктор
    var bob = Human("bob", 20)  // Вторичный конструктор
    println(tom.name)
    println(bob.name + "${bob.age}")

}
```
### Методы

Методы определяют поведение объектов данного класса. Такие функции еще называют `member functions` или функции-члены класса:

```kotlin
class Human(addName: String){
    var name: String = addName

    fun sayHello(){
        println("hello")
    }
}

fun main(){

    var tom = Human("Tom")
    tom.sayHello()
}
```

## Наследование
В Kotlin можем унаследовать класс только от одного класса, **множественное наследование не поддерживается**.

Все классы, созданные в Kotlin имеют по умолчанию свой родительский класс `Any` ([root class](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/)).
Имеет в своем вооружении методы:

```kotlin
fun equals(other: Any?): Boolean    // Indicates whether some other object is "equal to" this one.
fun hashCode(): Int                 // Returns a hash code value for the object.
fun toString(): String              // Returns a string representation of the object.
```

**По умолчанию**, все классы - `final`, не могут быть унаследованы кем-то другим.
Для реализации наследования необходимо добавить ключевое слово `open`:

```kotlin
open class Human(addName: String){
    var name: String = addName
}

class HumanWithAge(addName: String, addAge: Int): Human(addName){
    var age: Int = addAge
}
```

При наследовании производный класс **должен** вызывать `первичный конструктор` (а если такого нет, то конструктор по умолчанию) **родительского класса**.

Если дочерний класс не имеет **НЕпустого** первичного конструктора, тогда при вызове вторичного конструктора должен вызываться конструктор родительского класса через ключевое слово `super`:

```kotlin
open class Human(addName: String){
    var name: String = addName
}

class HumanWithAge: Human{
    var age: Int = 0

    constructor(addName: String, addAge: Int): super(addName){
        age = addAge
    }
}
```
**Функции и свойства**

По умолчанию, методы и свойства класса переходят по наследству:

```kotlin
open class Human(addName: String){
    var name: String = addName

    fun sayHello(){
        println("Hello")
    }
}

class HumanWithAge(addName: String, addAge: Int): Human(addName){
    var age: Int = 0

    fun doNotSayHello(){
        println("no")
    }
}

fun main(){ // Точка входа в программу

    var tom = Human("Tom")
    var bob = HumanWithAge("bob", 20)   // Унаследованное свойство "name"
    tom.sayHello()
    bob.sayHello()                      // Унаследованный метод
    bob.doNotSayHello()
}
```

Чтобы функции и свойства родительского класа можно было **переопределить**, к ним применяется аннотация `open`:

```kotlin
open class Human(addName: String){
    var name: String = addName

    open fun sayHello(){
        println("Hello")
    }
}

class HumanWithAge(addName: String, addAge: Int): Human(addName){
    var age: Int = 0

    override fun sayHello() {
        println("Hello from children")
    }
}
```

**Запрещаем переопределение методов**

Для этого применяется ключевое слово `final`:

```kotlin
open class Human(addName: String){
    var name: String = addName

    final fun sayHello(){           // Уже никто не сможет сделать override
        println("Hello")
    }
}
```


## Интерфейсы

**Интерфейсы** набор функциональности, который **должен** реализовать класс.
Для определения интерфейса применяется ключевое слово `interface`:

```kotlin
interface Hellowable{
    fun sayHello()
}
open class Human(addName: String) : Hellowable{
    var name: String = addName

    override fun sayHello(){
        println("Hello")
    }
}
```

Можно добавлять **множество** интерфейсов:

```kotlin
interface Movable{
    fun move()
}
interface Hellowable{
    fun sayHello()
}
open class Human(addName: String) : Hellowable, Movable{
    var name: String = addName

    override fun sayHello(){
        println("Hello")
    }
    
    override fun move(){
        println("moving")
    }
}
```

**Реализация метода по умолчанию**

Если в **интерфейсе** определен метод с **реализацией по умолчанию**, класс, использующий этот интерфейс **не обязан** переопределять у себя данный метод:

```kotlin
interface Movable{
    fun move()
    fun stop(){
        println("stoped")   // Реализация по умолчанию
    }
}

open class Human(addName: String) : Movable{
    var name: String = addName

    override fun move(){
        println("moving")
    }
}
```

**Свойства**

**Интерфейс** может определять **свойства** - им **НЕ** присваиваются значения. Класс же, который реализует интерфейс, также **обязан** реализовать эти свойства:

```kotlin
interface Movable{
    var speed : Int
    fun move()
}

open class Human(addName: String) : Movable{
    var name: String = addName
    override var speed = 0
    override fun move(){
        speed = 100
        println("moving")
    }
}
```

Также можем **переопределить свойсва** интерфейса в конструкторе класса:

```kotlin
interface Movable{
    var speed : Int
    var direction: Int
    fun move()
}

open class Human(addName: String, override var direction: Int) : Movable{
    var name: String = addName
    override var speed = 0
    override fun move(){
        speed = 100
        println("moving")
    }
}
```

Можно еще вызвать методы самого интерфейса:

```kotlin
interface Movable{
    var speed : Int
    var direction: Int
    fun move(){
        println("move from Movable")
    }
}

open class Human(addName: String, override var direction: Int) : Movable{
    var name: String = addName
    override var speed = 0
    override fun move(){
        speed = 100
        println("moving")
        super<Movable>.move()  // вот тут
    }
}
```



