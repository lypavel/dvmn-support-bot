# Telegram и VK боты для онлайн-издательства "Игра глаголов"

Чат-боты для помощи службе поддержки. Они обучены отвечать на стандартные вопросы пользователей с помощью сервиса DialogFlow от Google.

## Примеры работы ботов

### [Бот в Телеграме](https://t.me/devman_lessons_bot)

<details>
  <summary>Пример работы бота</summary>
  <img src="https://dvmn.org/filer/canonical/1569214094/323/" alt="Пример работы бота в телеграм">
</details>

### [Бот в ВК](https://vk.com/club226638798)

<details>
  <summary>Пример работы бота</summary>
  <img src="https://dvmn.org/filer/canonical/1569214089/322/" alt="Пример работы бота в телеграм">
</details>

## Установка

1. Установите [Python 3.10.12](https://www.python.org/downloads/release/python-31012/) и, если необходимо, создайте виртуальное окружение и активируйте его:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Установите необходимые зависимости с помощью `pip`:
    ```sh
    pip install -r requirements.txt
    ```
3. Создайте проект в Google Cloud. Подробнее в [документации](https://cloud.google.com/dialogflow/es/docs/quick/setup).
4. Создайте агент в DialogFlow. Проследите, чтобы id вашего проекта в Google и id агента совпадали. Подробнее в [документации](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
5. Получите [API-ключ Dialogflow](https://cloud.google.com/docs/authentication/api-keys). Для этого запустите скрипт:
    ```sh
    python3 dialogflow/create_api_key.py
    ```
    Информация для авторизации будет сохранена в файл `./project_api_key.txt`
6. Добавьте `Intents` в вашего агента DialogFlow. Это можно сделать как вручную (см. [документацию](https://cloud.google.com/dialogflow/es/docs/quick/api#detect_intent)), так и с помощью скрипта:
    ```sh
    python3 dialogflow/create_intents.py --file_name <path_to_intents_info.json>
    ```
    где `<path_to_intents_info.json>` - путь к вашему JSON-файлу, содержащему информацию об `Intents`.<br>По-умолчанию -  `questions.json`

    Файл должен иметь следующую структуру:
    ```json
    {
        "Устройство на работу": {
            "questions": [
                "Как устроиться к вам на работу?",
                "Как устроиться к вам?",
                "Как работать у вас?",
                "Хочу работать у вас",
                "Возможно-ли устроиться к вам?",
                "Можно-ли мне поработать у вас?",
                "Хочу работать редактором у вас"
            ],
            "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
        }
    }
    ```
7. Получите токен для вашего телеграм-бота и для вашего сообщества в ВК.
8. Создайте файл `./.env` и поместите в него следующие переменные окружения:
    ```env
    TG_BOT_TOKEN='токен телеграм бота'
    VK_API_KEY='api-ключ вашего сообщества в ВК'
    TG_LOGS_CHAT_ID='id чата в телеграм для отправки логов'
    GOOGLE_CLOUD_PROJECT_ID='id проекта в Google Cloud'
    GOOGLE_APPLICATION_CREDENTIALS='путь к файлу с информацией об авторизации в Google Cloud'
    ```

## Запуск

1. Запустите телеграм бота:
    ```sh
    python3 tg_bot.py
    ```
2. Запустите ВК бота:
    ```sh
    python3 vk_bot.py
    ```

***
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](dvmn.org).