### Author: Kiselev Valentin

#### Test task for Задание 5. Практикум разработки с Docker

Развёртывание:
```
docker-compose build
docker-compose up -d # development версия, статистика получается с помощью 'telnet localhost 9191'
docker-compose -f docker-compose-production.yml up -d # production версия
```