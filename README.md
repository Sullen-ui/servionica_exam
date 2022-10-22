## Задание 1.1

* Установить VirtualBox (или VMware workstation player), разобраться как  создать виртуальную машину и создать новую vm на базе дистрибутива  Centos
( Centos это параллельная open source ветка rhel );
![image](https://user-images.githubusercontent.com/82956250/197356738-2c87f5fa-e147-44f1-afb2-f90f935e2d4c.png)
* Подключиться к созданной vm по ssh через любой клиент.;
* Установить Python на созданной vm;

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/197357026-144746c7-2b7f-42cb-9d47-8ae8a616f8c8.png?raw=true" alt="Sublime's custom image"/>
</p>

* В домашней директорий пользователя создать папку task; реализовать собственное key-values хранилище на Python. Данные будут сохраняться в файле storage.data(в формате JSON, можно использовать библиотеку tempfile, для хранения данных во временных файлах). Добавление новых данных в хранилище и получение текущих значений осуществляется с помощью утилиты командной строки storage.py.Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже сохраненным. Другими словами - по одному ключу могут храниться несколько значений. При выводе на печать, значения выводятся в порядке их добавления в хранилище (Пример ввода "test_value,test_value2,test_value3" ). Формат вывода на печать для нескольких значений через запятую. Если значений по ключу не было найдено, выведите пустую строку или None. Сделать обработку исключений, если они будут возникать при тестировании. Скрипт должен работать в разных ОС.

Ссылки на файлы:<br>
[storage.py](https://github.com/Sullen-ui/servionica_exam/blob/main/task1/main.py)<br>
[storage.data](https://github.com/Sullen-ui/servionica_exam/blob/main/task1/storage.data)<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/197357436-c567eb58-2372-43c5-b496-1f74794a3574.png?raw=true" alt="Sublime's custom image"/>
  Запуск на Win10
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/197357587-74ffd7f3-a125-41bf-a8b3-53b9a4e36d7e.png?raw=true" alt="Sublime's custom image"/><br>
  Запуск на CentOS 7
</p>

