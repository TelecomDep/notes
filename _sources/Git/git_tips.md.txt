# Git tips

## 1. Начало использования Git

Официальная ссылка на скачивание приложения Git - [https://git-scm.com/downloads](https://git-scm.com/downloads)

ВАЖНО! !

ИМЯ ЛОКАЛЬНОЙ ПАПКИ (репозитория) ДОЛЖНО СОВПАДАТЬ С УДАЛЕННЫМ РЕПОЗИТОРИЕМ

### 1.1. Создание удалённого репозитория с целью объединения локального и удалённого.

Имя удалённого репозитория должно совпадать с названием локального репозитория (локальной папки проекта)

![git_test_2.PNG](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/git/git_test_2.png?raw=true )

### 1.2. Создание локального репозитория

```bash
# Создать папку с названием проекта (репозитория)
mkdir git_test_2
cd git_test_2
echo "# git_test_2" >> README.md
# Инициализация Git-репозитория (локального)
git init
git add README.md # добавление файла в git 
git commit -m "first commit" # первый "слепок" вашего проекта
git branch -M master # создание ветки с названием "master"
# Добавление удаленного репозитория для дальнейшей синхронизации, где
# origin - это название ссылки удаленного репозитория
git remote add origin https://github.com/fzybot/git_test_2.git

# загрузка всем коммитов на удаленный репозиторий
git push -u origin master
```

### 1.3. Персональный токен (GitHub personal auth token)

Для получения персонального токена перейдите по ссылке ниже.

[https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

```bash
git config --global user.name "username"
git config --global user.email "username@email.com"

git clone <personal repository>
git config --global credential.helper cache
git pull
#тут от вас потребуется ввести свой логин, 
#но вместо пароля вставьте персональный токен
#"username"
#<TOKEN>
#Далее вы сможете обновлять репозиторий без постоянного ввода пароля и логина.

```

### 1.4. Добавление SSH-ключа в профиль github

[Оригинальная статья по подключению SSH к профилю github](https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

1. Для начала необходимо сгенерировать SSH-ключ:
```bash
ssh-keygen -t ed25519 -C your_email@example.com
```
Путь и ключевую фразу добавляйте по желанию.

2. Выведете содержимое сгенерированных ключей (нам нжунен публичный `.pub`):

```bash
cd ~/.ssh/
cat id_ed25519.pub 
```
3. Копируем полученное содержимое в профиль github:

![git_add_ssh_key.PNG](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/git/github_add_ssh_key.png?raw=true )

4. Клонируем репозиторий при помощи SSH-ссылки:

![git_add_ssh_key.PNG](https://github.com/sibsutisTelecomDep/blog/blob/main/book/figures/git/git_clone_with_ssh.png?raw=true )

5. Проверяем работу командами `push`, `pull`. Работа с профилем становится в разы удобнее.


## 2. Небольшие практические наработки

### Перенести последний commit [из одной ветки в текущую](https://ru.stackoverflow.com/questions/57963/%D0%9F%D0%B5%D1%80%D0%B5%D0%BD%D0%B5%D1%81%D1%82%D0%B8-%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D1%82-%D0%B8%D0%B7-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D0%B2%D0%B5%D1%82%D0%BA%D0%B8-%D0%B2-%D0%B4%D1%80%D1%83%D0%B3%D1%83%D1%8E)

```bash
# Перенос последнего коммита в из ветки testBranch в текущую
# Выполнить не из ветки targetBranch
git cherry-pick targetBranch

```

### Удаление последнего коммита

```bash
#удаляет текущий коммит, переводит HEAD на предыдущий
git reset --hard HEAD~1 

# заставляем удаленный репозиторий перейти на коммит после удаленного
git push -f origin master 
```

### Восстановить удаленный коммит

[https://stackoverflow.com/questions/5473/how-can-i-undo-git-reset-hard-head1](https://stackoverflow.com/questions/5473/how-can-i-undo-git-reset-hard-head1)

Важно помнить, что git garbage collection производится примерно раз в месяц [[2](https://www.notion.so/Git-38baaf5fd51b42abb9ec4e330923d5f6?pvs=21)]. 

```bash
#Выводим информацию о HEAD несколько шагов назад
git reflog
c4a978f5 (HEAD -> pusch_non_3gpp, origin/pusch_non_3gpp) HEAD@{0}: pull: Fast-forward
2964d9be HEAD@{1}: reset: moving to HEAD~1
4bcc52c4 HEAD@{2}: reset: moving to HEAD

# был удален, необходимо восстановить
**4bcc52c4 HEAD@{3}: commit: 10 ssymbols in slot - success, find seg11**
 
2964d9be HEAD@{4}: reset: moving to HEAD~
360dd6b6 HEAD@{5}: pull: Fast-forward

#Ищем нужный, удаленный коммит и восстанавливаем по {SHA1 хэшу}.
git reset --hard 4bcc52c4
```

### Объединение нескольких последних коммитов в один (VS Code)

Выполняется при помощи интерактивного **rebase**.

```bash
git rebase -i HEAD~8 # 8 - количество коммитов, которые необходимо объединить в один
```

Далее, откроется окно редактора коммитов, будет выглядеть след. образом:

```bash
pick 3d8c4702 fapi в CMakeLists
pick 8f79668b Удалил неиспользуемые библиотеку nng и опцию is_server, начал переписывать файл sim_phy_main
pick 2e7ab2e0 Поднимается туннель
pick b21b5b9b Есть передача данных, не работает хэндовер, часто не доходит до ПД - PLMN не сходится TODO
pick 9e9b490c Исправлено: получение переотправок на L2/L3; DCIss_type после MSG4 в sim_phy становится UE_specific (берется из L2 конфигурации)
pick 962a2179 pucch_pdu и pusch_pdu теперь корректно отправляются в одном слоте
pick 691919fb Добавлена обработка Registration Accept и PDU Session Establishment Accept при получении через DL Information Transfer
pick 239a638f Работает ХО на UE через fapi sim
....

...

# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
...
...
```

Порядок в списке коммитов читается `снизу вверх, внизу самый последний коммит`. Необходимо заменить **pick** нижних коммитов на **squash**, оставляя **pick** последний коммит в который вы хотите объединить все остальные. 

```bash
**pick** 3d8c4702 fapi в CMakeLists # Коммит, в который объеденятся остальные
squash 8f79668b Удалил неиспользуемые библиотеку nng и опцию is_server, начал переписывать файл sim_phy_main
squash 2e7ab2e0 Поднимается туннель
squash b21b5b9b Есть передача данных, не работает хэндовер, часто не доходит до ПД - PLMN не сходится TODO
squash 9e9b490c Исправлено: получение переотправок на L2/L3; DCIss_type после MSG4 в sim_phy становится UE_specific (берется из L2 конфигурации)
squash 962a2179 pucch_pdu и pusch_pdu теперь корректно отправляются в одном слоте
squash 691919fb Добавлена обработка Registration Accept и PDU Session Establishment Accept при получении через DL Information Transfer
squash 239a638f Работает ХО на UE через fapi sim
....
```

Сохраняем и закрываем файл. Далее, вам предложат отредактировать комментарии, т.к. они все объединятся  в одном комментарии. Аналогично, сохраняем и закрываем. Проверить можно будет при помощи команды:

```bash
git log
```

### Изменить имя пользователя

```
git config --global --replace-all user.name "new name"
```

### Изменить имя автора последнего commit’а

Вероятно вы работаете в нескольких компаниях и случайно оставили `—global user.*` одной из них. Вы случайно могли выполнить `commit` не под тем пользователем\автором. Не составит труда изменить авторство последнего `commit’а`:

```cpp
git commit --amend --author="John Doe <john@doe.org>"
```

## Список Литературы

[1] Краткое видео по основам работы с Git - [https://www.youtube.com/watch?v=SWYqp7iY_Tc](https://www.youtube.com/watch?v=SWYqp7iY_Tc)

[2] git-gc - [https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-gc.html](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-gc.html)

[3] Онлайн-редактор оформления Readme. [Online]. Available: [https://humble-ballcap-e09.notion.site/Git-38baaf5fd51b42abb9ec4e330923d5f6?pvs=4](https://www.notion.so/Git-38baaf5fd51b42abb9ec4e330923d5f6?pvs=21)

[4] Git в игровой форме - [https://learngitbranching.js.org/?locale=ru_RU](https://learngitbranching.js.org/?locale=ru_RU)