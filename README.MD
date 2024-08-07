# KittyBot

## Основные возможности
- Отправка случайных изображений котов по команде /cats или тексту "кот".
- Получение сгенерированных изображений котов по команде /ai_cats или тексту "ai кот".
- Отправка сгенерированных изображений людей по команде /ai_persons или тексту "ai человек".
- Чат поддержки для пользователей с возможностью задать вопрос и получить ответ от администратора.

## Технологии
Проект реализован с использованием следующих технологий:
- **aiogram**: Асинхронная библиотека для работы с Telegram API.
- **aiohttp**: Библиотека для реализации веб-сервера и взаимодействия с внешними API.
- **Redis**: Используется для хранения состояний бота и быстрого доступа к данным.
- **NGINX**: Веб-сервер, который обеспечивает проксирование запросов к боту и поддержку SSL.
- **ngrok**: Сервис для временного создания туннелей, используемый для тестирования веб-хуков без необходимости настройки публичного домена.
- **Let's Encrypt**: Бесплатный сертификационный центр, который предоставляет SSL сертификаты для обеспечения безопасного соединения по HTTPS.

## Установка и запуск

### Настройка окружения
Установите Docker и Docker Compose на вашем компьютере.

### Клонирование репозитория

``` bash
git clone https://github.com/potesuch/kittybot.git
cd kittybot
```

### Настройка конфигурации
Создайте файл **.env** в папке **infra** и заполните его данными:

``` plaintext
bot_token=<ваш токен бота>
cat_api=<URL API для изображений котов>
ai_cats=<URL для сгенерированных изображений котов>
ai_persons=<URL для сгенерированных изображений людей>
redis_host=<хост Redis>
redis_port=<порт Redis>
redis_db=<номер базы данных Redis>
web_server_host=<хост веб-сервера>
web_server_port=<порт веб-сервера>
ngrok_host=<хост ngrok>
ngrok_port=<порт ngrok>
webhook_path=<путь для вебхука>
webhook_base_url=<базовый URL для вебхука, опционально>
```

### Настройка Docker Compose
Добавьте в файл **infra/docker-compose.yml** пути к ssl сертификату и ключу:

``` yaml
services:
  nginx_kittybot:
    image: nginx:1.25.4-alpine
    ports:
      - "443:443"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf/
      - <путь_к_SSL_сертификату>:/etc/nginx/ssl/fullchain.pem
      - <путь_к_SSL_ключу>:/etc/nginx/ssl/privkey.pem
...
```

### Настройка NGINX

Добавьте в файл **infra/nginx/deffault.conf** пути к ssl сертификату и ключу:

``` bash
server {
    listen 443 ssl;
    server_name your_domain.com;

    ssl_certificate /etc/nginx/ssl/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/privkey.pem;
...
```

### Запуск приложения
В папке **infra** выполните:

``` sh
    docker-compose up --build
```
Это соберет и запустит все сервисы в соответствии с вашим docker-compose.yml.

## Примечания
Для использования SSL необходимо предоставить сертификат и ключ, указав соответствующие пути в файле docker-compose.yml.
