Запускаем проект на своей машине (все команды применимы к MacOS, Linux "Ubuntu") 

Клонируем репозиторий:
git clone https://github.com/Nurgazy22/modul_1.git

Переходим в папку с проектом:
cd Parsing

Устанавливаем виртуальное окружение (для python 3):
python3 -m venv venv

Запускаем виртуальное окружение:
. venv/bin/activate

Обновляем систему управления пакетами:
pip install --upgrade pip

Устанавливаем в виртуальном окружении зависимости для проекта:
pip install -r req.txt

Если у вас не установлен Postgres, нужно установить:
sudo apt-get -y install postgresql

Открываем консоль бд:
psql

Создаем бд с названием test:
CREATE DATABASE test;

Выходим из консоли командой:
\q Enter

Запускаем программу:
python main.py 

Можно проверить записанные данные из бд:
1) psql        <!--открываем консоль бд -->
2) \c test     <!--подключаемся к бд test -->
3) select * from houses;    <!--выбираем все записи из таблицы houses -->


