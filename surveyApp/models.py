from django.db import models


class Survey(models.Model):
    survey_name = models.CharField(max_length=200, verbose_name='Название')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    end_date = models.DateTimeField(verbose_name='Дата окончание')
    survey_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.survey_name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE, verbose_name='Опрос')
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    question_type = models.CharField(max_length=200, verbose_name='Тип вопроса')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200, verbose_name='Текст выбора')

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField(verbose_name='ID пользователя')
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE, verbose_name='Опрос')
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE, verbose_name='Вопрос')
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True, verbose_name='Выбор')
    choice_text = models.CharField(max_length=200, null=True, verbose_name='Текст выбора')

    def __str__(self):
        return self.choice_text


# create example
# {
#     "id": 1,
#     "survey_name": "interview",
#     "pub_date": "2021-11-10T15:58:31Z",
#     "end_date": "2021-11-13T15:58:42Z",
#     "survey_description": "Questions for interview"
# }
