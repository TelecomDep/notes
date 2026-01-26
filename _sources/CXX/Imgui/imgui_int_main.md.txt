# Первая программа с Dear Imgui

Схематично вся работа нашей программы будет выглядеть следующим образом (см рисунок ниже):
![alt text](image/imgui_int_main/imgui_int_main_01.png)



## Окно GUI интерфейса (SDL2)

```cxx
SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER);
SDL_Window* window = SDL_CreateWindow(
                    "Backend start", 
                    SDL_WINDOWPOS_CENTERED, 
                    SDL_WINDOWPOS_CENTERED,
                    1024, 768, 
                    SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE);
```
- `title` — имя окна.
- `x,y` — координаты окна. Если хотим открыть на весь экран, то нужно ставить 0,0
- `w,h` — размеры окна. Что бы открыть на весть экран обращаемся к объекту displayMode.
- `flags` — тут выставляем флаги инициализации окна.


## Backends




