# Первая программа с Dear Imgui

Схематично вся работа нашей программы будет выглядеть следующим образом (см рисунок ниже):
![alt text](image/imgui_int_main/imgui_int_main_01.png)


С точки зрения кода программы, то простой интерфейс с одной кнопкой и выводом текста будет выглядеть следующим образом:

```c++
#include <GL/glew.h>
#include <SDL2/SDL.h>

#include <iostream>
#include <chrono>
#include <thread>
#include <cmath>

#include "backends/imgui_impl_opengl3.h"
#include "backends/imgui_impl_sdl2.h"
#include "imgui.h"

int main(int argc, char *argv[]) {

    // SDL
    SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER);
    SDL_Window* window = SDL_CreateWindow(
        "Backend start", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        1024, 768, SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE);
    SDL_GLContext gl_context = SDL_GL_CreateContext(window);

    // Imgui
    ImGui::CreateContext();
    ImPlot::CreateContext();

    // Ввод\вывод
    ImGuiIO& io = ImGui::GetIO(); (void)io;
    io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Включить Keyboard Controls
    io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Включить Gamepad Controls
    io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // Включить Docking

    // Imgui + OpenGl backend
    ImGui_ImplSDL2_InitForOpenGL(window, gl_context);
    ImGui_ImplOpenGL3_Init("#version 330");

    bool running = true;
    while (running) {

        // 0) Обработка event'ов (inputs, window resize, mouse moving, etc.);
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            std::cout << "Processing some event: "<< event.type << std::endl;
            ImGui_ImplSDL2_ProcessEvent(&event);
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }

        // 1) Начинаем создавать новый фрейм;
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplSDL2_NewFrame();
        ImGui::NewFrame();
        ImGui::DockSpaceOverViewport(0, nullptr, ImGuiDockNodeFlags_None);


        // 2) Наш виджет с кнопкой;
        {
            static int counter = 0;
            ImGui::Begin("Hello, world!"); 
                ImGui::Text("This is some useful text.");    
                if (ImGui::Button("Button"))                         
                    counter++;
                ImGui::Text("counter = %d", counter);
            ImGui::End();
        }

        // 3) Отправляем на рендер;
        ImGui::Render();
        glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        SDL_GL_SwapWindow(window);
    }

    // Закрываем приложение безопасно.
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplSDL2_Shutdown();
    ImPlot::DestroyContext();
    ImGui::DestroyContext();
    SDL_GL_DeleteContext(gl_context);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
```

**Получаем**:

![alt text](image/imgui_int_main/imgui_simple_example.png)
## Окно GUI интерфейса (SDL2)

```c++
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

## Using standard Backends

**Директория [backends/](https://github.com/ocornut/imgui/blob/master/backends) содержит популярные backend'ы для работы с платформенными и графическими API. Можно использовать в своем проекте, интегрировав в  Dear ImGui. 

Каждый backend состоит и пары файлов: `imgui_impl_XXXX.cpp` + `imgui_impl_XXXX.h`.

- The 'Platform' backends are in charge of: mouse/keyboard/gamepad inputs, cursor shape, timing, and windowing.<BR>
  e.g. Windows ([imgui_impl_win32.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_win32.cpp)), SDL3 ([imgui_impl_sdl3.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_sdl3.cpp)), GLFW ([imgui_impl_glfw.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_glfw.cpp)), etc.

- The 'Renderer' backends are in charge of: creating atlas texture, and rendering imgui draw data.<BR>
  e.g. DirectX11 ([imgui_impl_dx11.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_dx11.cpp)), OpenGL/WebGL ([imgui_impl_opengl3.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_opengl3.cpp)), Vulkan ([imgui_impl_vulkan.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_vulkan.cpp)), etc.

- For some high-level frameworks, a single backend usually handles both 'Platform' and 'Renderer' parts.<BR>
  e.g. Allegro 5 ([imgui_impl_allegro5.cpp](https://github.com/ocornut/imgui/blob/master/backends/imgui_impl_allegro5.cpp)). If you end up creating a custom backend for your engine, you may want to do the same.

An application usually combines one Platform backend + one Renderer backend + main Dear ImGui sources.
For example, the [example_win32_directx11](https://github.com/ocornut/imgui/tree/master/examples/example_win32_directx11) application combines imgui_impl_win32.cpp + imgui_impl_dx11.cpp. There are 20+ examples in the [examples/](https://github.com/ocornut/imgui/blob/master/examples/) folder. See [EXAMPLES.MD](https://github.com/ocornut/imgui/blob/master/docs/EXAMPLES.md) for details.

**Once Dear ImGui is setup and running, run and refer to `ImGui::ShowDemoWindow()` in imgui_demo.cpp for usage of the end-user API.**

### Список поддерживаемых Backend'ов

[backends/](https://github.com/ocornut/imgui/blob/master/backends):

Список **Platforms Backends**:
```
imgui_impl_android.cpp      ; Android native app API
imgui_impl_glfw.cpp         ; GLFW (Windows, macOS, Linux, etc.) http://www.glfw.org/
imgui_impl_osx.mm           ; macOS native API (not as feature complete as glfw/sdl backends)
imgui_impl_sdl2.cpp         ; SDL2 (Windows, macOS, Linux, iOS, Android) https://www.libsdl.org
imgui_impl_sdl3.cpp         ; SDL3 (Windows, macOS, Linux, iOS, Android) https://www.libsdl.org
imgui_impl_win32.cpp        ; Win32 native API (Windows)
imgui_impl_glut.cpp         ; GLUT/FreeGLUT (this is prehistoric software and absolutely not recommended today!)
```
Список **Renderer Backends**:
```
imgui_impl_dx9.cpp          ; DirectX9
imgui_impl_dx10.cpp         ; DirectX10
imgui_impl_dx11.cpp         ; DirectX11
imgui_impl_dx12.cpp         ; DirectX12
imgui_impl_metal.mm         ; Metal (ObjC or C++)
imgui_impl_opengl2.cpp      ; OpenGL 2 (legacy fixed pipeline. Don't use with modern OpenGL code!)
imgui_impl_opengl3.cpp      ; OpenGL 3/4, OpenGL ES 2/3, WebGL
imgui_impl_sdlgpu3.cpp      ; SDL_GPU (portable 3D graphics API of SDL3)
imgui_impl_sdlrenderer2.cpp ; SDL_Renderer (optional component of SDL2 available from SDL 2.0.18+)
imgui_impl_sdlrenderer3.cpp ; SDL_Renderer (optional component of SDL3. Prefer using SDL_GPU!).
imgui_impl_vulkan.cpp       ; Vulkan
imgui_impl_wgpu.cpp         ; WebGPU (web + desktop)
```
Список **high-level Frameworks Backends** (combining Platform + Renderer):
```
imgui_impl_allegro5.cpp
imgui_impl_null.cpp
```

## Обработка ивентов

Обработка ивентов происходит при помощи встроенной структуры `SDL_Event`. Каждый новый фрейм (или итерацию цикла) мы выполняем обработку ивентов в собственном цикле `while`, а потом уже отрисовываем все виджеты и т.д. Допольно простая архитектура.

```c++
// Обработка event'ов (inputs, window resize, mouse moving, etc.)
SDL_Event event;
while (SDL_PollEvent(&event)) {
    std::cout << "Processing some event: "<< event.type << std::endl;
    ImGui_ImplSDL2_ProcessEvent(&event);
    if (event.type == SDL_QUIT) {
        running = false;
    }
}
```

Список ивентов, обрабатываемых библиотекой SDL2 [SDL_EventType](https://wiki.libsdl.org/SDL2/SDL_EventType): 

```c++
typedef enum
{    /* Application events */
    SDL_QUIT           = 0x100, /**< User-requested quit */ # 256
    ...
    /* Window events */
    SDL_WINDOWEVENT    = 0x200, /**< Window state change */ # 512
    ...
        /* Mouse events */
    SDL_MOUSEMOTION    = 0x400, /**< Mouse moved */ # 1024

    SDL_LASTEVENT    = 0xFFFF
} SDL_EventType;
```

![alt text](image/imgui_int_main/imgui_event_example.png)


