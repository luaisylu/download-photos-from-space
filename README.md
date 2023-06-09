# Загружаем фотографии с космоса в телеграм канал

Проект берет с картинки космоса с сайтов [SpaceX](https://api.spacexdata.com/v3/launches/), [NASA](https://api.nasa.gov/planetary/apod), [EPIC](https://api.nasa.gov/EPIC/api/natural/images) и публикует в телеграм канал.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные окружения
Для получения `TELEGRAM_CHANNEL_CHAT_ID` необходимо зайти в свой телеграм канал и найти ссылку. `TG_TOKEN` нужно получить у `@BotFather`. `NASA_KEY` нужно взять с сайта [api.nasa.gov](https://api.nasa.gov/).
Для запуска необходимо создать файл `.env`. В нем хранятся переменные окружения для правильной работы кода. Пример содержимого файла `.env`:
```python
TELEGRAM_CHANNEL_CHAT_ID="@publish_tg_idry"
TG_TOKEN="5805997756:AHLKyZhhl3m_C_SXMBhknKIt78YJ1I_16rg"
NASA_KEY="uV02SJszkmrye1jcejjNbM61S7bs3Oc7fVU6QYt8"
```

### Примеры запуска скриптов
Для загрузки фотографий в папку "media" из SpaceX необходимо ввести следующий:
```python
python fetch_spacex_images.py
```
Если вы хотите скачать фотографии с определенного запуска необходимо ввести необязательный аргумент ``--id:
```python
python fetch_spacex_images.py --id 5eb87d42ffd86e000604b384 
```

Для загрузки фотографий в папку `media` из NASA необходимо ввести следующий код:
```python
python fetch_nasa_images.py
```

Для загрузки фотографий в папку `media` из EPIC необходимо ввести следующий код:
```python
python fetch_epic_images.py --id 5eb87d42ffd86e000604b384 
```

Для запуска скрипта и публикаций фотографий из папки `media` в телеграм канал необходимо ввести следующий код:
```python
python main.py
```
Код берет одно значение `publication_time`. Аргумент необязательный и по умолчанию частота публикаций выставлена раз в 4 часа.
Для того чтобы запустить скрипт и установить свое время частоту публикаций, необходимо вызвать необязательный аргумент:
```python
python main.py --publication_time 5
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
