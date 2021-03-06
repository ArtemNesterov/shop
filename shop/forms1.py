from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    """
    Форма для создания новых пользователей.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        """
        Проверка на то что две записи пароля совпадают
        """

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """
        Сохранить предоставленный пароль в хэшированном формате
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
