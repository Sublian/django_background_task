from django.forms import ModelForm
from django import forms
from .models import *


class MessageCreateForm(ModelForm):

    class Meta:
        model = Message
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(
                attrs={
                    "placeholder": "Post a message...",
                    "class": "w-full border-2 border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500",
                    "maxlength": "280",
                }
            ),
        }
