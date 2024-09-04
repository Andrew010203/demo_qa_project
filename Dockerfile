#FROM python:3.10-alpine3.17
#
## Обновление репозиториев
#RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
#    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories
#
## Установка chromedriver
#RUN apk update
#RUN apk add --no-cache chromium chromium-chromedriver tzdata
#
## Установка рабочего каталога
#WORKDIR /app
#
## Копирование файлов
#COPY requirements.txt .
#
##Стоит отметить, что шаг с удалением py-pip на самом деле размер итогового образа не уменьшит,
##ведь каждая команда RUN просто создаёт новый слой. Чтобы избежать этого, стоит объединять операции в RUN через &&.
#
## Обновление трех пакетов pip, setuptools, wheel.
#RUN pip install --upgrade pip setuptools wheel
#
## Установка зависимостей
#RUN pip install -r requirements.txt
#
## Копирование файлов
## Откуда(имя локальной папки с файлами)/ ./куда(имя папки в контейнере)
#COPY tyt/ ./tyt
#
## Создание каталога для результатов
#RUN mkdir -p allure_results
#
## Команда для запуска тестов
##                Путь к исполняемому файлу
#CMD ["pytest", "tyt/tests", "--alluredir=allure_results"]


#FROM python:3.10-alpine3.17
#
## Обновление репозиториев
#RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
#    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories
#
## Установка chromedriver и chromium
#RUN apk update && \
#    apk add --no-cache chromium chromium-chromedriver tzdata
#
## Установка рабочего каталога
#WORKDIR /app
#
## Копирование файлов
#COPY requirements.txt .
#
## Обновление pip и установка зависимостей
#RUN pip install --upgrade pip setuptools wheel
#RUN pip install -r requirements.txt
#
## Копирование тестов
#COPY tyt/ ./tyt
#
## Создание каталога для результатов и установка прав
#RUN mkdir -p allure_results && mkdir -p download && chmod -R 777 download
#
## Команда для запуска тестов
#CMD ["pytest", "tyt/tests", "--alluredir=allure_results"]

FROM python:3.9-slim

# Установите необходимые зависимости
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    gnupg2 \
    libnss3-dev \
    libxss1 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Установите Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Установите Python-библиотеки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY tyt/ ./tyt
CMD ["pytest", "tyt/tests", "--alluredir=allure_results"]
