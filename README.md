# Restaurant Reservation API

API для управления бронированием столов в ресторане.

## Требования
- Docker
- Docker Compose

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone <ссылка_на_репозиторий>
   cd restaurant_reserv

2. Создайте файл .env:
    DATABASE_URL=postgresql://user:password@db:5432/restaurant

3. Запустите проект:
    docker compose up --build

## Использование

API доступно на: http://localhost:8000
Эндпоинты:

    GET /tables/ - список столов
    POST /tables/ - создать стол
    DELETE /tables/{id} - удалить стол
    GET /reservations/ - список броней
    POST /reservations/ - создать бронь
    DELETE /reservations/{id} - удалить бронь