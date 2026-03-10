# Методическое пособие по JavaScript и React

## Оглавление

1. [Введение](#введение)
2. [Часть I: JavaScript](#часть-i-javascript)
   - [Основы синтаксиса](#основы-синтаксиса)
   - [Функции](#функции)
   - [Объекты и массивы](#объекты-и-массивы)
   - [Асинхронность](#асинхронность)
   - [Примеры взаимодействия с DOM](#примеры-взаимодействия-с-dom)
3. [Часть II: React](#часть-ii-react)
   - [Введение в React](#введение-в-react)
   - [Компоненты](#компоненты)
   - [Хуки](#хуки)
   - [Роутинг](#роутинг)
4. [Практические задания](#практические-задания)
5. [Дополнительные ресурсы](#дополнительные-ресурсы)
6. [Сборщик VIte](#сборщик-vite)

---

## Введение

Это методическое пособие предназначено для изучения основ JavaScript и библиотеки React. Предполагается, что читатель знаком с базовыми понятиями веб-разработки (HTML, CSS).

---

## Часть I: JavaScript

### Основы синтаксиса

#### Переменные

```javascript
// Объявление переменных
let name = "John"; // может быть изменено
const age = 25; // не может быть изменено
var oldWay = "value"; // устаревший способ
```

#### Типы данных

```javascript
// Примитивные типы
const string = "Hello";
const number = 42;
const boolean = true;
const nullValue = null;
const undefinedValue = undefined;
const symbol = Symbol("id");

// Объекты
const object = { key: "value" };
const array = [1, 2, 3];
```

#### Операторы

```javascript
// Арифметические
let sum = 5 + 3; // 8
let difference = 5 - 3; // 2

// Сравнение
console.log(5 == "5"); // true (нестрогое)
console.log(5 === "5"); // false (строгое)

// Логические
console.log(true && false); // false
console.log(true || false); // true
```

### Основы синтаксиса

#### Function Declaration

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```

#### Function Expression

```javascript
const greet = function (name) {
  return `Hello, ${name}!`;
};
```

#### Стрелочные функции

```javascript
const greet = (name) => {
  return `Hello, ${name}!`;
};

// Сокращенная форма
const square = (x) => x * x;
```

Главные отличия:

1. Function Declaration

```javascript
// Можно вызвать ДО объявления
console.log(greet("Alice")); // "Hello, Alice!"

function greet(name) {
  return `Hello, ${name}!`;
}
```

2. Function Expression

```javascript
// Вызов ДО объявления вызовет ошибку
console.log(greet("Alice")); // ReferenceError: Cannot access 'greet' before initialization

const greet = function (name) {
  return `Hello, ${name}!`;
};
```

3. Стрелочные функции

```javascript
// Тоже ошибка - ведут себя как const
console.log(greet("Alice")); // ReferenceError

const greet = (name) => {
  return `Hello, ${name}!`;
};
```

Также есть различия в контексте (this), в аргументах и в использовании в качестве конструктора, если интересно про это можете сами почитать подробнее.

### Объекты и массивы

#### Работа с объектами

```javascript
const person = {
  name: "Alice",
  age: 30,
  greet() {
    console.log(`Hello, I'm ${this.name}`);
  },
};

// Деструктуризация
const { name, age } = person;

// Spread оператор
const updatedPerson = { ...person, city: "Moscow" };
```

Как работает деструктуризация

1. JavaScript смотрит на объект person
2. Ищет свойства с именами name и age
3. Создает новые переменные name и age
4. Копирует значения из соответствующих свойств объекта

Что происходит в spread операторе

1. ...person - "распаковывает" все свойства объекта person
2. Создается новый объект, куда копируются все свойства из person
3. Добавляется новое свойство city: "Moscow"
4. Если бы в person уже было свойство city, оно бы перезаписалось

#### Работа с массивами

```javascript
const numbers = [1, 2, 3, 4, 5];

// Методы массивов
const doubled = numbers.map((num) => num * 2);
const even = numbers.filter((num) => num % 2 === 0);
const sum = numbers.reduce((acc, num) => acc + num, 0);
```

1. Метод map() - Создает новый массив, применяя функцию к каждому элементу исходного массива.

```javascript
// Пример
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((num) => num * 2);

// Пошагово что происходит:
// 1. num = 1 → return 1 * 2 = 2
// 2. num = 2 → return 2 * 2 = 4
// 3. num = 3 → return 3 * 2 = 6
// 4. num = 4 → return 4 * 2 = 8
// 5. num = 5 → return 5 * 2 = 10

console.log(doubled); // [2, 4, 6, 8, 10]
console.log(numbers); // [1, 2, 3, 4, 5] - исходный массив не изменился!
```

2. Метод filter() - Создает новый массив с элементами, которые прошли проверку (вернули true).

```javascript
// Пример
const numbers = [1, 2, 3, 4, 5];
const even = numbers.filter((num) => num % 2 === 0);

// Пошагово что происходит:
// 1. num = 1 → 1 % 2 === 0? false → исключаем
// 2. num = 2 → 2 % 2 === 0? true → оставляем
// 3. num = 3 → 3 % 2 === 0? false → исключаем
// 4. num = 4 → 4 % 2 === 0? true → оставляем
// 5. num = 5 → 5 % 2 === 0? false → исключаем

console.log(even); // [2, 4]
console.log(numbers); // [1, 2, 3, 4, 5] - исходный массив не изменился!
```

3. Метод reduce() - Преобразует массив в единственное значение, последовательно обрабатывая каждый элемент.

```javascript
// Пример
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, num) => acc + num, 0);

// Пошагово что происходит:
// Начальное значение acc = 0
// 1. acc = 0, num = 1 → return 0 + 1 = 1
// 2. acc = 1, num = 2 → return 1 + 2 = 3
// 3. acc = 3, num = 3 → return 3 + 3 = 6
// 4. acc = 6, num = 4 → return 6 + 4 = 10
// 5. acc = 10, num = 5 → return 10 + 5 = 15

console.log(sum); // 15
```

### Асинхронность

#### Callbacks

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback("Data received");
  }, 1000);
}

fetchData((data) => {
  console.log(data);
});
```

Callback (функция обратного вызова) - это функция, которая передается в другую функцию как аргумент и выполняется после завершения какой-либо операции.

#### Promises

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data received");
      // или reject("Error message");
    }, 1000);
  });
}

fetchData()
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

Promise - это объект, который представляет результат асинхронной операции. У него есть 3 состояния:

1. pending (ожидание)
2. fulfilled (выполнено успешно)
3. rejected (выполнено с ошибкой)

#### Async/await

```javascript
async function getData() {
  try {
    const data = await fetchData();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

Async/await - это синтаксический сахар над Promises, который позволяет писать асинхронный код так, как будто он синхронный.

Про Promise и Async/await можно написать очень много, если интересно, то можно изучить самим

#### Примеры взаимодействия с DOM

```javascript
// Получение элементов
const element = document.getElementById("myId");
const elements = document.querySelectorAll(".myClass");

// Создание элементов
const newDiv = document.createElement("div");
newDiv.textContent = "Hello World";

// Добавление в DOM
document.body.appendChild(newDiv);

// Обработка событий
element.addEventListener("click", function () {
  console.log("Element clicked!");
});
```

DOM (Document Object Model) - это программный интерфейс для HTML и XML документов. Он представляет структуру документа в виде дерева объектов, которые можно изменять с помощью JavaScript.

#### Как устроен DOM (дерево):

```
text
Document (корень)
  ↓
<html>
  ├── <head>
  │     ├── <title>
  │     └── ...
  └── <body>
        ├── <h1 id="header">
        ├── <div class="content">
        │     └── <p>
        └── ...
```

Каждый элемент становится узлом (node) в дереве:

- Element nodes - теги (div, p, h1)
- Text nodes - текстовое содержимое
- Attribute nodes - атрибуты (id, class)

## Часть II: React

### Введение в React

React — это JavaScript-библиотека для создания пользовательских интерфейсов.

#### Создание приложения

```
npx create-react-app my-app
cd my-app
npm start
```

### Компоненты

#### Функциональные компоненты

```javascript
// Welcome.jsx
import React from "react";

function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Welcome;
```

#### Использование компонентов

```javascript
// App.jsx
import React from "react";
import Welcome from "./Welcome";

function App() {
  return (
    <div>
      <Welcome name="Alice" />
      <Welcome name="Bob" />
    </div>
  );
}

export default App;
```

### Хуки

#### useState

```javascript
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

useState - это хук React, который позволяет добавлять состояние в функциональные компоненты. До появления хуков состояние могло быть только в классовых компонентах.

- useState(0) инициализирует состояние значением 0
- Возвращает массив [currentValue, setterFunction]
- Деструктуризация создает переменные count и setCount
- count содержит текущее значение состояния
- setCount - функция для обновления состояния

#### useEffect

```javascript
import React, { useState, useEffect } from "react";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Загрузка данных при изменении userId
    fetch(`/api/users/${userId}`)
      .then((response) => response.json())
      .then((data) => setUser(data));
  }, [userId]); // Зависимости

  if (!user) return <div>Loading...</div>;

  return <div>{user.name}</div>;
}
```

useEffect - это хук, который позволяет выполнять побочные эффекты в функциональных компонентах. Он заменяет методы жизненного цикла в классовых компонентах.

- Эффект выполняется после каждого рендера, где userId изменился
- Делает запрос к API когда userId меняется
- Обновляет состояние user когда данные приходят
- Вызывает ререндер компонента с новыми данными

### Роутинг

#### Установка React Router

```javascript
npm install react-router-dom
```

#### Настройка маршрутов

```javascript
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
}
```

Более крутой пример:

#### Routes.tsx:

```javascript
import { lazy, useEffect, useState } from 'react'
import { RouteProps } from 'react-router-dom'

const Page1 = lazy(() =>
  import('~/pages/Page1').then(module => ({
    default: module.PageFirst
  }))
)

const Page2 = lazy(() =>
  import('~/pages/Page2').then(module => ({
    default: module.PageSecond
  }))
)

const Page3 = lazy(() =>
  import('~/pages/Page3').then(module => ({
    default: module.PageThird
  }))
)


export const AppRoutes = {
  PAGE1: 'page1',
  PAGE2: 'page2',
  PAGE3: 'page3',
} as const

export type AppRoutesT = (typeof AppRoutes)[keyof typeof AppRoutes]

export const RoutePath: Record<AppRoutesT, string> = {
  [AppRoutes.PAGE1]: '/page1',
  [AppRoutes.PAGE2]: '/page2',
  [AppRoutes.PAGE3]: '/page3',
}

export const routeConfig: Record<AppRoutesT, RouteProps> = {
  [AppRoutes.PAGE1]: {
    path: RoutePath.page1,
    element: <PageFirst />
  },
  [AppRoutes.PAGE2]: {
    path: RoutePath.page2,
    element: <PageSecond />
  },
  [AppRoutes.PAGE3]: {
    path: RoutePath.page3,
    element: <PageThird />
  }
}

```

#### app-router.tsx:

```javascript
import { memo, useCallback } from "react";
import { Suspense } from "react";
import { Route, RouteProps, Routes } from "react-router-dom";

import { routeConfig } from "~/shared/config/routes/Routes";

export const AppRouter = memo(() => {
  const renderWithWrapper = useCallback(
    ({ path, element }: RouteProps) => (
      <Route key={path} path={path} element={element} />
    ),
    []
  );

  return (
    <Suspense fallback={<div>Загрузка...</div>}>
      {" "}
      <Routes>{Object.values(routeConfig).map(renderWithWrapper)}</Routes>
    </Suspense>
  );
});
```

Потом вызываете AppRouter в вашем главном файле (обычно main.tsx/App.tsx)

## Сборщик Vite

**Сборщик модулей (Module Bundler)** - это инструмент, который берет различные модули JavaScript и их зависимости, и объединяет их в один или несколько оптимизированных файлов, готовых для использования в браузере.

### Аналогия:

Представьте, что у вас есть:

- **Модули** - отдельные коробки с кодом (файлы .js, .jsx, .ts)
- **Зависимости** - связи между коробками (import/export)
- **Сборщик** - грузовик, который упаковывает все коробки в один контейнер

Исходные файлы → Обход зависимостей → Компиляция → Оптимизация → Бандл

Этапы традиционной сборки:

- Entry Point - начальный файл
- Dependency Graph - построение графа зависимостей
- Transformation - компиляция (JSX → JS, Sass → CSS)
- Bundling - объединение в бандлы
- Optimization - оптимизация, сжатие
- Output - финальные файлы

#### Проблемы традиционных сборщиков:

```javascript
# Медленный запуск в development
npm start    # Может занимать 10-60 секунд!

# Медленный Hot Module Replacement (HMR)
# Изменение файла → пересборка → 1-5 секунд ожидания

# Сложная конфигурация
```

#### Vite

Vite (франц. "быстрый", произносится "вит") - это современный сборщик, который решает проблемы традиционных инструментов за счет использования нативных ES модулей.

Ключевая идея Vite:

Разделение сборки на две части:

- Development - использует нативные ES модули браузера
- Production - использует оптимизированную сборку Rollup

```
Development Mode:
Браузер ← HTTP ← Vite Dev Server ← ES Modules

Production Mode:
Браузер ← Оптимизированные файлы ← Rollup сборка
```

#### Что помогает Vite достигать больших скоростей

### 1. Нативные ES Modules в разработке:

Традиционный подход

```
// Все файлы компилируются в один бандл ДО запуска
// Большое время ожидания при старте
```

Vite подход:

```
// Браузер загружает модули напрямую через HTTP
<script type="module" src="/src/main.jsx"></script>

// Vite сервер преобразует модули на лету
// Только по запросу браузера
```

**ES Modules** (ECMAScript Modules) - это официальная, стандартизированная система модулей в JavaScript, которая позволяет разбивать код на отдельные файлы и организовывать зависимости между ними.

### Простая аналогия:

Представьте книгу:

- **Без модулей** - одна большая глава (1000 страниц)
- **С модулями** - много глав с оглавлением (импорты/экспорты)

### 2. Esbuild для трансформаций

- В 10-100x быстрее чем Babel
- Мгновенная компиляция TypeScript, JSX

#### Пример запуска сервера разработки:

Стандартный вариант:

```
$ npm start
# Compiling...
# Compiled successfully in 15.3s
```

Vite:

```
$ npm run dev
# Vite dev server running in 347ms
# Ready in 500ms
```

## Создание React приложения с Vite

```
# 1. Инициализация проекта
npm create vite@latest

# 2. Интерактивный выбор:
# ✔ Project name: … my-react-app
# ✔ Select a framework: › React
# ✔ Select a variant: › JavaScript + SWC

# 3. Установка зависимостей
cd my-react-app
npm install

# 4. Запуск development сервера
npm run dev

# 5. Открыть в браузере
# → http://localhost:5173/
```

Структура получившегося проекта:

```
my-react-app/
├── node_modules/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
│   └── components/
├── index.html
├── package.json
├── vite.config.js
└── README.md
```

### Ключевые файлы:

### 1. index.html (Корневой HTML):

```javascript
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

### 2. main.jsx (Точка входа):

```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### 3. App.jsx (Основной компонент)

```javascript
import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
```

### 4. Скрипты Package.json

```javascript
{
  "scripts": {
    "dev": "vite",           // Сервер разработки
    "build": "vite build",   // Сборка для production
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview" // Предпросмотр production сборки
  }
}
```

### 5. Настройка Vite (vite.config.js)

```javascript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000, // Порт разработки
    open: true, // Автоматически открывать браузер
  },
  build: {
    outDir: "dist", // Папка для сборки
    sourcemap: true, // Карты исходного кода
  },
});
```
