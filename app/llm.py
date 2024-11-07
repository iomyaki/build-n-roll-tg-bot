import random
import requests
import base64
import time

catalog_id = 'b1glk8jqpe4b0vqet2ao'
apikey = 'AQVN3Om8LWbcmqZMziIyTBhJOCrj7ubBJrlJVl13'


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
                "text": "Я создаю нового персонажа для игры в D&D. Мне нужно придумать интересную и подробную историю моего персонажа, историю его жизни, почему он ступил на тропу приключений. Придумай имя и прошлое моего D&D персонажа по ключевым словам: "
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {apikey}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    return response.text


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
