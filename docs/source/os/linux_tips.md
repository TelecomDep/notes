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
