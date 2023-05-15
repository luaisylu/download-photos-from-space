# Загружаем фотографии с космоса в телеграм канал

Проект берет с картинки космоса с сайтов [SpaceX](https://api.spacexdata.com/v3/launches/), [NASA](https://api.nasa.gov/planetary/apod), [EPIC](https://api.nasa.gov/EPIC/api/natural/images) и публикует в телеграм канал.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Переменные окружения
Для получения `CHANNEL_CHAT_ID` необходимо зайти в свой телеграм канал и найти ссылку. `TG_TOKEN` нужно получить у `@BotFather`. `NASA_KEY` нужно взять с сайта [api.nasa.gov](https://api.nasa.gov/).
Для запуска необходимо создать файл `.env`. В нем хранятся переменные окружения для правильной работы кода. Пример содержимого файла `.env`:
```python
CHANNEL_CHAT_ID="@publish_tg_idry"
TG_TOKEN="5805997756:AHLKyZhhl3m_C_SXMBhknKIt78YJ1I_16rg"
NASA_KEY="uV02SJszkmrye1jcejjNbM61S7bs3Oc7fVU6QYt8"
```

### Примеры запуска скриптов

Для запуска скрипта необходимо ввести следующий код:
```python
python main.py
```
Код берет одно значение `publication_time`. Необходимо ввести частоту публикаций. Аргумент необязательный и по умолчанию частота публикаций выставлена раз в 4 часа.
Для того чтобы запустить скрипт и установить свое время частоту публикаций, необходимо вызвать необязательный аргумент:
```python
python main.py 5 --publication_time
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
