# DDF24 Dungeon Pythons 🎲

❗ Проект, созданный в рамках хакатона ИПКН ИТМО «DevDays Fall 2024».

Мы — партия приключенцев «DDF24 Dungeon Pythons». Мы несём вам радость игры. Не успели создать персонажа, а до партии осталось 10 минут? Ваш ГМ в очередной раз просит не создавать пятого в партии человека-воина? Тогда мы идём к вам!

## Описание приключения

D&D Assistant — это решение для генерации персонажей в игре Dungeons & Dragons. Наш проект позволяет с помощью бота в Telegram сгенерировать полноценный, готовый к игре, лист персонажа по заданным критериям. У пользователя есть возможность сгенерировать либо полностью случайного персонажа, либо заполнить некоторые поля листа персонажа, а остальные сгенерировать так, чтобы они подходили к уже заполненным.

Мы прекрасно знаем, насколько грустно бывает, когда вы создаёте крутого (по вашему мнению) персонажа, а он оказывается абсолютно бесполезным из-за того, что вы набрали полный список ненужных или даже бесполезных заклинаний. Поэтому мы взяли на себя смелость предложить вам список заклинаний, с которыми вам будет максимально комфортно осваивать игровой контент в зависимости от вашего персонажа.

В дальнейшем мы планируем расширить доступный в нашем генераторе список классов и происхождений, а также добавить возможность генерировать карты подземелий или даже неожиданные сюжетные повороты для ваших приключений.

## Преимущества нашего приключения

Помимо бесплатной путёвки в Забытые Королевства вы получите:
- Генерацию квент и аватаров персонажей через YandexGPT API для полноценного отыгрыша.
- Доступ к homebrew и добавлению своих правил жизни.
- Возможность балансировать характеристики, заклинания и способности по рейтингу полезности сообщества.

Хранить информацию по спеллам предполагаем в базе данных, а генерацию характеристик осуществлять при помощи собственного алгоритма для эффективного распределения характеристик и подбора классов и рас. Таким образом, созданный с помощью нашего бота персонаж гарантированно будет не только уникальным, но и будет комфортно ощущаться в игровом мире.

## Партия приключенцев

- ГМ (тимлид, реализация алгоритма генерации) — Иван Золотников
- Колдун (реализация бота) — Иван Мякиньков
- Воин (реализация БД заклинаний) — Иван Ступницкий
- Волшебник (реализация работы с API) — Матвей Багров
- Монах (реализация бота, тестирование) — Александр Крюков

## Установка и использование

Клонируйте репозиторий:
```bash
git clone https://github.com/iomyaki/build-n-roll-tg-bot.git
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

Запустите бота и насладитесь быстрой генерацией прекрасных персонажей!
```bash
python main.py
```
или
```bash
python3 main.py
```

Для работы также потребуется в файле .env указать токен Telegram-бота, а также API-ключ и CATALOG_ID для работы с YandexGPT.

Для генерации квенты и портрета персонажа вам будет предложено ввести ключевые слова для генеративной модели. Вы можете отправить что угодно, но учитывайте, что написанное повлияет на сгенерированный результат (иногда весьма непредсказуемо). Генерировать квенту и портрет для персонажа можно неограниченное число раз — у вас будет возможность подобрать ключевые слова для наилучшего результата. Количество символов в вашем сообщении с ключевыми словами не должно превышать 500.

## Контрибьюция

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория и отправьте пулл-реквест с вашими изменениями.

## Материалы для презентации

Ссылка на презентацию проекта: https://docs.google.com/presentation/d/1SUfxcJUfvSjAPUVbx636RNYPHiQ619aMU0qOwrFOLC0/edit?usp=sharing

## Признание

<div align="center">
  <img src="https://github.com/user-attachments/assets/daadb78f-621c-46cc-8292-192af801861a" alt="Diploma" style="width:65%; height:auto">
</div>
