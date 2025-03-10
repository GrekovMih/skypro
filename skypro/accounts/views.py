from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import StyledAuthenticationForm, CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "Регистрация прошла успешно. Вы автоматически вошли в систему."
            )
            login(request, user)
            return redirect("product_table")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = StyledAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f"Вы вошли как {user.username}.")
            return redirect("product_table")
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = StyledAuthenticationForm(request)
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect("login")
