# SurveyApp
API для системы опросов пользователей

# Задача:
Спроектировать и разработать API для системы опросов пользователей.

_Функционал для администратора системы:_

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

_Функционал для пользователей системы:_

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

# Технологии:
* Django 2.2.10, 
* Django REST framework,
* Python 3.8.3

Склонируйте репозиторий с помощью git
```bash
https://github.com/Smartboy10/SurveyApp.git
```
Перейти в директорию:
```bash
cd survey
```
Создать и активировать виртуальное окружение Python.
```bash
python -m venv venv
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
# Выполнить следующие команды:
* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту(можно пропустить) и пароль:
```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/

Чтобы получить токен пользователя:
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body:
  * username:
  * password:
* Example:
```bash
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```
Чтобы создать опрос:
* Request method: POST
* URL: http://localhost:8000/api/v1/survey/create/
* Header:
  * Authorization: Token userToken
* Body:
  * survey_name: name of survey
  * pub_date: publication date can be set only when survey is created, format: YYYY-MM-DD HH:MM:SS
  * end_date: survey end date, format: YYYY-MM-DD HH:MM:SS
  * survey_description: description of survey
* Example:
```bash
curl --location --request POST 'http://localhost:8000/api/v1/survey/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'pub_date=%pub_date' \
--form 'end_date=%end_date \
--form 'survey_description=%survey_description'
```
Обновить опрос:
* Request method: PATCH
* URL: http://localhost:8000/api/v1/survey/update/[survey_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * survey_id
* Body:
  * survey_name: name of survey
  * end_date: survey end date, format: YYYY-MM-DD HH:MM:SS
  * survey_description: description of survey
* Example:
```bash
curl --location --request PATCH 'http://localhost:8000/api/v1/survey/update/[survey_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'end_date=%end_date \
--form 'survey_description=%survey_description'
```
Удалить опрос:
* Request method: DELETE
* URL: http://localhost:8000/api/v1/survey/update/[survey_id]
* Header:
  * Authorization: Token userToken
* Param:
  * survey_id Example:
```bash
curl --location --request DELETE 'http://localhost:8000/api/v1/survey/update/[survey_id]/' \
--header 'Authorization: Token %userToken'
```
Посмотреть все опросы:
* Request method: GET
* URL: http://localhost:8000/api/v1/survey/view/
* Header:
  * Authorization: Token userToken
* Example:
```bash
curl --location --request GET 'http://localhost:8000/api/v1/survey/view/' \
--header 'Authorization: Token %userToken'
```
Просмотр текущих активных опросов:
* Request method: GET
* URL: http://localhost:8000/api/v1/survey/view/active/
* Header:
  * Authorization: Token userToken
* Example:
```bash
curl --location --request GET 'http://localhost:8000/api/v1/survey/view/active/' \
--header 'Authorization: Token %userToken'
```
Создаем вопрос:
* Request method: POST
* URL: http://localhost:8000/api/v1/question/create/
* Header:
  * Authorization: Token userToken
* Body:
  * survey: id of survey
  * question_text:
  * question_type: can be only one, multiple or text
* Example:
```bash
curl --location --request POST 'http://localhost:8000/api/v1/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```
Обновляем вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/v1/question/update/[question_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * question_id
* Body:
  * survey: id of survey
  * question_text: question
  * question_type: can be only one, multiple or text
* Example:
```bash
curl --location --request PATCH 'http://localhost:8000/api/v1/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```
Удаляем вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/v1/question/update/[question_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * question_id
* Example:
```bash
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```
Создаем выбор:
* Request method: POST
* URL: http://localhost:8000/api/v1/choice/create/
* Header:
  * Authorization: Token userToken
* Body:
  * question: id of question
  * choice_text: choice
* Example:
```bash
curl --location --request POST 'http://localhost:8000/api/v1/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```
Обновляем выбор:
* Request method: PATCH
* URL: http://localhost:8000/api/v1/choice/update/[choice_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * choice_id
* Body:
  * question: id of question
  * choice_text: choice
* Example:
```bash
curl --location --request PATCH 'http://localhost:8000/api/v1/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```
Удаляем выбор:
* Request method: DELETE
* URL: http://localhost:8000/api/v1/choice/update/[choice_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * choice_id
* Example:
```bash
curl --location --request DELETE 'http://localhost:8000/api/v1/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```
Создаем ответ:
* Request method: POST
* URL: http://localhost:8000/api/v1/answer/create/
* Header:
  * Authorization: Token userToken
* Body:
  * survey: id of survey
  * question: id of question
  * choice: if question type is one or multiple then it’s id of choice else null
  * choice_text: if question type is text then it’s text based answer else null
* Example:
```bash
curl --location --request POST 'http://localhost:8000/api/v1/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```
Обновляем ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/v1/answer/update/[answer_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * answer_id
* Body:
  * survey: id of survey
  * question: id of question
  * choice: if question type is one or multiple then it’s id of choice else null
  * choice_text: if question type is text then it’s text based answer else null
* Example:
```bash
curl --location --request PATCH 'http://localhost:8000/api/v1/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```
Удаляем ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/v1/answer/update/[answer_id]/
* Header:
  * Authorization: Token userToken
* Param:
  * answer_id
* Example:
```bash
curl --location --request DELETE 'http://localhost:8000/api/v1/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```
Просматриваем ответы пользователя:
* Request method: GET
* URL: http://localhost:8000/api/v1/answer/view/[user_id]/
* Param:
  * user_id
* Header:
  * Authorization: Token userToken
* Example:
```bash
curl --location --request GET 'http://localhost:8000/api/v1/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
```
