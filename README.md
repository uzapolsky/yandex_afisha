# Куда пойти. Москва глазами любителя активного отдыха

Cайт https://uzapolsky.pythonanywhere.com/ о самых интересных местах в Москве.

## Запуск

- Скачайте код
- Установите зависимости

  ```python
  pip3 install -r requirements.txt
  ```

- Примените миграции

  ```python
  python3 manage.py migrate
  ```

- Запустите сервер

  ```python
  python3 manage.py runserver
  ```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

## Добавление мест

Для отображения места на карте необходим [json-файл](https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json) с описанием.

Для быстрой загрузки локаций на карту можно воспользоваться командой `python3 manage.py load_place <link>`.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).