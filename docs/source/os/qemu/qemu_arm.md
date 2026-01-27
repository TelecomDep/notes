# Установка Ubuntu (ARM) на QEMU

Официальный [источник](https://canonical-ubuntu-hardware-support.readthedocs-hosted.com/boards/how-to/qemu-riscv/).

## Установка зависимостей

Для загрузки виртуальной машины `ARM` вам потребуются следующие пакеты:

- ` qemu-system-aarch64` — QEMU используется для эмуляции машины ARM.

**Устанавливаем**
```bash
sudo apt update
sudo apt install qemu-system-aarch64
```
