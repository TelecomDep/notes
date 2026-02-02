# 3. Виджеты

Лучший вариант для более полного понимания работы виджетов находится в `Demo-версии` самой библиотеки. Запустить ее можно при помощи `ImGui::ShowDemoWindow();`, если в CMakeLists.txt вы подключали исходники `${THIRD_PARTY_DIR}/imgui/imgui_demo.cpp`. Далее, уже по названию виджетов в примерах можно найти реализацию любого элемента на экране и их взаимодействия. 

Проект только с `Demo-окном` можно найти по [ссылке](https://github.com/TelecomDep/backend_notes/blob/DemoWindow/src/main.cpp). Результат выглядит следующим образом:

![alt text](image/imgui_widgets/imgui_widgets_demo.png)

Начало любого виджета (окна внутри главного приложения) начинается с `ImGui::Begin();` и должно заканчиваться `ImGui::End();`. Далее, для примеров виджетов эти конструкции будут проигнорированы для сокращения текста.
```c++
{
    ImGui::Begin("Hello, world!"); 

    ImGui::End();
}
```
Здесь будет просто пустое окно с текстом `Hello World!` в шапке.

![alt text](image/imgui_widgets/imgui_widgets_hello.png)

## Text

Это окно с `текстом` + `текстом с выводом занчения` переменной:

```c++
{ 
    
    ImGui::Begin("Hello, world!"); 

    static int counter = 0;
    ImGui::Text("This is some useful text.");
    ImGui::Text("counter = %d", counter);
    ImGui::TextLinkOpenURL(" Текст с сылкой: https://github.com/epezent/implot");

    ImGui::End();
}
```

![alt text](image/imgui_widgets/imgui_widgets_text_02.png)

## Кнопки

С кнопками можно помнить, что проверка нажатия на каждую кнопку должна осуществляться в инструкции `if() {}`:

```c++
{
    static int counter = 0;
    if (ImGui::Button("Button")){
        counter++;
        // можно что угодно добавить при нажатии на кнопку
    }                        
    ImGui::Text("counter = %d", counter);
}
```

![alt text](image/imgui_widgets/imgui_widgets_button.png)


## Работа с устройствами I\O

Для работы с устройствами ввода вывода присутствует структура `ImGuiIO`. Включение различных устройств осуществляется при помощи флагов конфигурации:  
```cxx
ImGuiIO& io = ImGui::GetIO(); (void)io;
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Включить Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Включить Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // Включить Docking
io.ConfigFlags |= ImGuiConfigFlags_ViewportsEnable;       // Включить Multi-Viewport / Platform Windows. Позволяет работать "окнам" вне основного окна. 
```
После инициализации `ImGuiIO` может получить доступ к работе с устройствами:

### Мышка

Получение текущей позиции мыши:
```cxx
ImVec2 mouse = ImGui::GetMousePos();
ImGui::Text("Mouse position: x = %d, y = %d", mouse.x, mouse.y);
```
![alt text](image/imgui_widgets/mouse_get_position.png)



