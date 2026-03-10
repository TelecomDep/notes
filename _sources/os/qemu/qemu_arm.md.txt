# Установка Ubuntu (ARM) на QEMU

Официальный [источник](https://canonical-ubuntu-hardware-support.readthedocs-hosted.com/boards/how-to/qemu-riscv/).

## Установка зависимостей

Для загрузки виртуальной машины `ARM` вам потребуются следующие пакеты:

- ` qemu-system-aarch64` — QEMU используется для эмуляции машины ARM.
- `qemu-user-static` .

**Устанавливаем**
```bash
sudo apt update
sudo apt install qemu-user-static qemu-system-aarch64
```

## Запуск при помощи готового образа ОС (Raspberry Pi)

1) Скачиваем образ с [официального сайта](https://www.raspberrypi.com/software/operating-systems/).

2) Распаковываем образ:
```bash
cd Downloads/
unxz "$IMAGE_FILE.xz"
```

3) Увеличиваем объем памяти:

```bash
qemu-img resize -f raw "$IMAGE_FILE.img" 8G

```

4) 

