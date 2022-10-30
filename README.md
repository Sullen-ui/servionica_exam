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
[storage.py](https://github.com/Sullen-ui/servionica_exam/blob/main/task1.1/main.py)<br>
[storage.data](https://github.com/Sullen-ui/servionica_exam/blob/main/task1.1/storage.data)<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/197357436-c567eb58-2372-43c5-b496-1f74794a3574.png?raw=true" alt="Sublime's custom image"/>
  Запуск на Win10
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/197357587-74ffd7f3-a125-41bf-a8b3-53b9a4e36d7e.png?raw=true" alt="Sublime's custom image"/><br>
  Запуск на CentOS 7
</p>

----------
## Задание 1.2
<p>Написать сервис API на Python к key-values хранилищу из задания 1. Самый простой фреймворк для реализации flask и дополнительный модуль flaskRESTful. Хранить данные можно так же во временных файлах в файле storage.data(в формате JSON, можно использовать библиотеку tempfile). Сервис должен уметь отвечать на запросы POST и GET. Требования к выводу можно взять из задания 1. Ниже в скриншотах есть демонстрация основных запросов и их вывода. На главной странице сервиса ‘/’ сделать описание возможностей сервиса API.Из сервиса сделать новый Docker Image и запустит контейнер, данные хранить внутри контейнера, при перезапуске будут отчищается. </p><br>

<p>Т.к. изначально данных нет, необходимо добавить запись</p>
    <h3>Добавление записи</h3>
    
    <p>curl -i -H "Content-Type: application/json" -X POST -d "{"\key\": \"value\"}" http://localhost:5000/api/v1/storage/json/write</p>
    
<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198864048-35c55c03-7c4a-4b7e-bfd4-2cc257e3d88c.png?raw=true" alt="Sublime's custom image"/>
</p>
    
    <h3>Получить все записи</h3>
    
    <p>http://localhost:5000/api/v1/storage/json/all</p>
    
    <p>curl -i -X GET http://localhost:5000/api/v1/storage/json/all</p>
   
      <p align="center">
        <img src="https://user-images.githubusercontent.com/82956250/198866943-d540f6fe-d6fb-49e5-a42c-8d1c50105e19.png?raw=true" alt="Sublime's custom image"/>
      </p>
      
    <h3>Получение записи по ключу</h3>
    
    <p>http://localhost:5000/api/v1/storage/json/key=value</p>
    
    <p>curl -i -X GET http://localhost:5000/api/v1/storage/json/key=key</p>
    
      <p align="center">
        <img src="https://user-images.githubusercontent.com/82956250/198867020-0f6b904b-6ea7-46f2-a3ca-b3944c0a4596.png?raw=true" alt="Sublime's custom image"/>
      </p>

 * Написал докерфайлы под flask и nginx, сборка через docker-compose<br>
 <a href="https://github.com/Sullen-ui/servionica_exam/blob/main/task1.2/docker-compose.yml">Ссылка на docker-compose</a>
 ``` docker-compose up --build -d ```
      <p align="center">
        <img src="https://user-images.githubusercontent.com/82956250/198867242-a6d54faf-cca8-4f83-98d7-6b448d1aa574.png?raw=true" alt="Sublime's custom image"/>
      </p>
       <p align="center">
        <img src="https://user-images.githubusercontent.com/82956250/198867265-3d6f4ee2-a7ca-4964-b933-fc3c28907bb5.png?raw=true" alt="Sublime's custom image"/>
      </p>


 
---
## Задание 2.1
Создать 2 WEB сервера с выводом страницы «Hello Word! \n Server 1» (аналогично для второго Server 2). Сделать балансировку нагрузки (HA + keepalived), чтобы при обновлении страницы мы попадали на любой из WEB серверов(Для балансировки можно сделать 2 отдельных сервера, в сумме 4).
Будет плюсом использование Docker.<br>
Решение:

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198123427-65faee88-cddc-4d83-892d-937d0794f02d.png?raw=true" alt="Sublime's custom image"/>
</p>
<br>
 ### Подготовка ###<br>
 
* Создание двух VM на дистрибутиве CentOS 7 (CentOS(Master),CentOS(Slave)) Со статичными IP. Создаём одну ВМ и средствами VirtualBox делаем клон.<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198009340-18fbe7f9-66a7-4def-b2d6-2d3100254ddd.png?raw=true" alt="Sublime's custom image"/>
</p><br>

* В Virtualbox создаем сеть и пробрасываем порты.<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198009590-5a9e3937-3b5e-4048-8a87-7c03c80b77b2.png?raw=true" alt="Sublime's custom image"/>
  <img src="https://user-images.githubusercontent.com/82956250/198009766-b17968d7-51ca-406a-a484-d071abc1e770.png?raw=true" alt="Sublime's custom image"/>
</p>

* Устанавливаем необходимое ПО
```
    yum install epel-release
    yum install docker haproxy keepalived
```     
* Запустим контейнер nginx на обоих ВМ<br>
```
    docker run -p 8080:80 nginx:stable-alpine --restart=always
    #Добавим инфу в стартовые страницы index.html
    docker exec -ti <container id> /bin/sh
    >echo "Hello world! Server1-2" > /usr/share/nginx/html/index.html
    >exit
```
* Проверим работу контейнеров

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198018928-708c70f7-28f5-4d37-a97f-11b33b991ac1.png?raw=true" alt="Sublime's custom image"/>
</p><br>

* Конфигурации HAproxy , Keepalived

<table>
  <tr>
    <td></td>
    <td>HAproxy</td>
    <td>Keepalive</td>
  </tr>
  <tr>
    <td>CentOS(Master)</td>
    <td>
      <a href="https://github.com/Sullen-ui/servionica_exam/blob/main/task2.1/haproxy/haproxy1.cfg">haproxy.cfg</a>
    </td>
    <td>
      <a href="https://github.com/Sullen-ui/servionica_exam/blob/main/task2.1/keepalived/keepalived1.conf">keepalived.conf</a>
    </td>
  </tr>
  <tr>
    <td>CentOS(Slave)</td>
    <td>
      <a href="https://github.com/Sullen-ui/servionica_exam/blob/main/task2.1/haproxy/haproxy2.cfg">haproxy.cfg</a>
    </td>
    <td>
      <a href="https://github.com/Sullen-ui/servionica_exam/blob/main/task2.1/keepalived/keepalived2.conf">keepalived.conf</a>   
    </td>
  </tr>
</table>

* Запуск сервисов HAproxy, Keepalived( на всех ВМ)<br>

  ```
   # HAproxy <br>
   systemctl enable haproxy <br>
   systemctl start haproxy
   
   # Keepalived
   # Включим поддержку VIP
   echo "net.ipv4.ip_nonlocal_bind = 1" >> /etc/sysctl.conf
   systemctl enable keepalived
   systemctl start keepalived
  
  ```
* Проверим статусы и работу сервисов.

<p align="center">
  <img src="https://user-images.githubusercontent.com/82956250/198070521-d347e64f-5ead-4f46-a9d3-7390618bab41.png?raw=true" alt="Sublime's custom image"/>
</p><br>
  
  Приоритет vrrp выше на centOS(Master), можем проверить на какой ноде и устройстве сейчас VIP ``10.0.2.100``
  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198073823-5cb6199e-11cf-4295-aa97-7237c6909387.png?raw=true" alt="Sublime's custom image"/>
  </p><br>
  
* С главного хоста у нас проброшен порт в виртуальную сеть. Мы можем отправлять запрос на ``localhost:8083`` чтобы попасть на наш keepalived ``10.0.2.100``

  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198075056-55716e2d-8eb9-4d73-b2e1-b454272b6c95.png?raw=true" alt="Sublime's custom image"/>
  </p><br>
  
* Сэмулируем крах keepalived и HAproxy на ноде СentOS(Master)(см.схемку)

  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198124260-84c0130b-f0b5-4975-8746-e17a4c4e6ad4.png" alt="Sublime's custom image"/>
  </p><br>
  
  Остановим эти сервисы 


  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198124532-e3cf9796-4317-45c1-902e-78a76c495387.png" alt="Sublime's custom image"/>
  </p><br>
  
  Посмотрим на какой ноде VIP
  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198078253-37259634-2efc-472b-96bf-ee6b0403466d.png" alt="Sublime's custom image"/>
  </p><br>
  
  Пробуем снова отправлять запрос на Nginx'ы
  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198124767-a9935461-a6fc-473b-a520-4e6c3338ce6b.png" alt="Sublime's custom image"/>
  </p><br>
  
* Теперь cэмулируем крах keepalived и HAproxy на ноде СentOS(Slave)

  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198125356-ebd3e980-90a7-4e37-b81e-324ed5bd493e.png" alt="Sublime's custom image"/>
  </p><br>
  
  Посмотрим на какой ноде VIP
  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/82956250/198125660-2950a6d9-6b89-46e4-8a64-aa3a6b5b154d.png" alt="Sublime's custom image"/>
  </p><br>
  
  Пробуем снова отправлять запрос на Nginx'ы
  
    <p align="center">
      <img src="https://user-images.githubusercontent.com/82956250/198125868-5cf10bff-1511-4249-9f00-c39bb444adc9.png" alt="Sublime's custom image"/>
    </p><br>
    
---

## Задание 2.2
<p>Написать роль на Ansible по развёртыванию стенда из Задание 2.1. Можно написать 1 большую роль, либо 3 роли и потом вызвать их поочёрдно.Конфиги nginx, HA proxy, keepalived оформить, используя шаблоны Jinja2(язык шаблонов).</p><br>

* Подготовил ВМ на базе Rocky Linux 9. 2 рабочие ноды + 1 Asnible Master. Развернул стенд по схеме из задания 2.1. Использовал роли, доп. коллекции, шаблонизатор.

    <p align="center">
      <img src="https://user-images.githubusercontent.com/82956250/198626709-4798c98c-ea13-42c8-a7aa-a9b71973c298.png" alt="Sublime's custom image"/>
    </p><br>
 
* Структура проекта Ansible

    <p align="center">
      <img src="https://user-images.githubusercontent.com/82956250/198627775-8333c8a1-7007-4ffb-a984-317f5abe8fde.png" alt="Sublime's custom image"/>
    </p><br>

* Запуск плейбука

    <p align="center">
      <img src="https://user-images.githubusercontent.com/82956250/198623670-a30fe809-0175-409a-9b1e-289afe4b1165.png" alt="Sublime's custom image"/>
    </p><br>
 
 * Проверка. Результаты запросов и тестов идентичны заданию 2.1
 
    <p align="center">
      <img src="https://user-images.githubusercontent.com/82956250/198631781-c41e2f2f-9cb4-479b-bcaf-8dd7fb803ec1.png" alt="Sublime's custom image"/>
    </p><br>
    
