# Указываем базовый образ
FROM python:3.11

# Устанавливаем переменную окружения PYTHONUNBUFFERED в значение 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию контейнера
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию контейнера
COPY . /app/

# Запускаем команду для запуска сервера при старте контейнера
CMD python manage.py runserver 0.0.0.0:8000