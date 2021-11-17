from django.urls import path

from .views import *

app_name = 'surveyApp'
urlpatterns = [
    path("login/", login),
    #survey
    path("survey/view/", survey_view, name="login"),
    path("survey/create/", survey_create),
    path("survey/update/<int:survey_id>/", survey_update),
    path("survey/view/active", active_survey_view),
    #question
    path("question/create/", question_create),
    path("question/update/<int:question_id>/", question_update),
    #choice
    path("choice/create/", choice_create),
    path("choice/update/<int:choice_id>/", choice_update),
    #answer
    path("answer/create", answer_create),
    path("answer/update/<int:answer_id>/", answer_update),
]
