"""
urls.py

Created on 2020-12-26
Updated on 2021-01-02

Copyright © Ryan Kan

Description: The file which contains the URLconfig for the `questions` app.
"""


# IMPORTS
from django.urls import path, re_path

from questions import views

# URL CONFIG
urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^questions/(?P<question_id>\d+)(?:/OK=(?P<override_key>\w+))?/$", views.display_question,
            name="display_question"),
    path("questions/<int:question_id>/input", views.generate_input, name="generate_input"),
    path("questions/<int:question_id>/answer", views.check_question_answer, name="check_question_answer"),
    path("questions/<int:question_id>/reset-input-for-all-users", views.reset_question_input,
         name="reset_question_input")
]
