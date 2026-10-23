# Подсказки по Linux

### Grub (while booting)

Нашел [здесь](https://unix.stackexchange.com/questions/329926/grub-starts-in-command-line-after-reboot/330852#330852).
Cause: boot process can't find the root partition

Please type ls This will show all partitions, and then type individual
```bash
ls (hd0,1)/
ls (hd0,2)/ 
```

до тех пор пока не найдем что-то похожее на:

```bash
(hd0,1)/boot/grub   OR (hd0,1)/grub

# или это

(hd0,1)/efi/boot/grub OR (hd0,1)/efi/grub
```

```bash
set prefix=(hd0,1)/grub

# или 

set prefix=(hd0,1)/boot/grub
```

Продолжаем:

```bash
set root=(hd0,1)
insmod linux
insmod normal
normal
```
Готово!


### Ноутбук с закрытой крышкой не включается если переключать KVM (внешние мониторы)

```bash
sudo nano /etc/systemd/logind.conf 
```

Меняем значения полей:

```bash
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
```

Перезагружаем сервис:

```bash
sudo systemctl restart systemd-logind.service 
```

### Ручное изменение яркости экрана на ноутбуке (Lenovo)

```bash
xrandr --output eDP-1 --brightness 0.3
```


### Использование .ssh директории Windows через WSL (т.е. общие ключи и конфиги)


1. Enable Linux Metadata for Windows Drives

```bash
sudo nano /etc/wsl.conf
```

Добавить:

```bash
[automount]
options = "metadata,umask=022,fmask=111"
```

Рестарт WSL (из PowerShell или CMD):

```bash
wsl --shutdown
```


2. Move and Link the .ssh Directory

Если хотим сохранить старые конфиги\ключи: 

```bash
mkdir -p /mnt/c/Users/<YourWindowsUsername>/.ssh
cp -r ~/.ssh/* /mnt/c/Users/<YourWindowsUsername>/.ssh/ 2>/dev/null
rm -rf ~/.ssh
```

Создаем символьную ссылку:

```bash
ln -s /mnt/c/Users/<YourWindowsUsername>/.ssh ~/.ssh
```

Раздаем права:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa ~/.ssh/id_ed25519 ~/.ssh/config 2>/dev/null
chmod 644 ~/.ssh/authorized_keys ~/.ssh/known_hosts ~/.ssh/*.pub 2>/dev/null
```


### Работа с Tmux

`Prefix + c` - это сочетание клавиш (по умолчанию `ctrl + b`).

Создайте или отредактируйте файл `~/.tmux.conf`:

```
# Включение поддержки мыши (прокрутка, выбор панелей, изменение размера)
set -g mouse on

# Изменение префикса на Ctrl + a (вместо неудобного Ctrl + b)
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Нумерация окон и панелей с 1, а не с 0 (удобно переключаться с клавиатуры)
set -g base-index 1
setw -g pane-base-index 1

# Удобная перезагрузка конфига по клавише prefix + r
bind r source-file ~/.tmux.conf \; display "Конфиг перезагружен!"

# Интуитивное разделение панелей (через | и -)
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %
```

Основные горячие клавиши по умолчанию

Префикс по умолчанию: Ctrl + b (если не изменен в конфиге):

- `Prefix + c` — создать новое окно
- `Prefix + w` — список всех окон и сессий
- `Prefix + n` / Prefix + p — следующее / предыдущее окно
- `Prefix + "`  — разделить панель по горизонтали
- `Prefix + %` — разделить панель по вертикали
- `Prefix + стрелки` — переключение между панелями
- `Prefix + d` — отсоединиться от сессии (оставить работать в фоне)
- `Prefix + x `— закрыть текущую панель

Полезные команды сессий в терминале

- `tmux` — запустить новую сессию
- `tmux new -s myname` — создать сессию с именем myname
- `tmux ls` — посмотреть список запущенных сессий
- `tmux attach -t myname` — подключиться к сессии myname
- `tmux kill-session -t myname` — завершить сессию myname