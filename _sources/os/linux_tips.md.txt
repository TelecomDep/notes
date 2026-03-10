

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