from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView

from shop.forms1 import UserCreationForm
from shop.models import Product

"""
Ссылка, на которой будет отображаться продукт
"""


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        """
        Если пользователь аутифинцирован, то показать список продуктов(товара)
        """
        if request.user.is_authenticated:
            products = Product.objects.all()
            l = {'products': products}
            return render(request, self.template_name, l)
        else:
            return render(request, self.template_name, {})


"""
Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации
"""


class RegisterFormView(FormView):
    form_class = UserCreationForm
    """
    Указана ссылка на страницу входа для зарегистрированных пользователей.
    """
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        """
        Создаём пользователя, если данные в форму были введены корректно.
        """
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        """
        Если данные введены не верно, возврат на регистрацию
        """
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = UserCreationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        """
        получение объекта пользователя
        """
        self.user = form.get_user()

        """
        аутентификация пользователя
        """
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(View):
    """
    Выполняем выход для пользователя
    """

    def get(self, request):
        logout(request)
        """
        Перенаправляем пользователя на главную страницу.
        """

        return HttpResponseRedirect('/')
