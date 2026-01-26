# Виджеты


## Text



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
![alt text](<image/imgui_widgets/Screenshot from 2026-01-26 16-11-27.png>)



