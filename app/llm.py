import base64
import os
import requests
import time

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

catalog_id = os.getenv('CATALOG_ID')
apikey = os.getenv('API_KEY')


def generate_quenta(race, char_class, gender, age, keywords):
    prompt = {
        "modelUri": f"gpt://{catalog_id}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "1000"
        },
        "messages": [
            {
                "role": "user",
                "text": "Я создаю нового персонажа для игры в D&D. "
                        "Мне нужно придумать интересную и подробную историю моего персонажа, "
                        "историю его жизни, почему он ступил на тропу приключений. "
                        f"Раса моего персонажа — {race}, класс — {char_class}, пол — {gender}, возраст — {age} лет. "
                        f"Придумай имя и опиши прошлое моего D&D-персонажа на красивом литературном русском языке по "
                        f"ключевым словам: {keywords}. Не указывай в конце сообщения, что это лишь пример истории "
                        f"и подобное. В секции «имя» не нужно "
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {apikey}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    assistant_text = result["result"]["alternatives"][0]["message"]["text"]

    return assistant_text


def generate_portrait(prompt, seed, attempts=30):
    prompt = {
        "modelUri": f"art://{catalog_id}/yandex-art/latest",
        "generationOptions": {
            "seed": seed,
            "aspectRatio": {
                "widthRatio": "1",
                "heightRatio": "1"
            }
        },
        "messages": [
            {
                "weight": "1",
                "text": prompt
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-key {apikey}"
    }

    create_request = requests.post('https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync',
                                   headers=headers, json=prompt)

    try:
        return create_request.json()['error']
    except:
        pass

    attempt = 0

    while attempt < attempts:
        attempt += 1
        done_request = requests.get(f'https://llm.api.cloud.yandex.net:443/operations/{create_request.json()["id"]}',
                                    headers=headers)
        if done_request.json()['done']:
            with open('yandexart_' + create_request.json()['id'] + '.jpeg', 'wb') as file:
                file.write(base64.b64decode(done_request.json()['response']['image']))

            break

        time.sleep(5)

    return 'yandexart_' + create_request.json()['id'] + '.jpeg'
