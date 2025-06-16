# Используем стабильный Python-образ
FROM python:3.10-slim

# Отключаем буферизацию вывода
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8000

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
