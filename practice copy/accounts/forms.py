from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')
    