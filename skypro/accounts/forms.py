from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Электронная почта"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Имя пользователя",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя пользователя"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Подтверждение пароля"}
        )


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя пользователя"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )
