from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from shop.forms1 import UserCreationForm
from shop.models import Product, Buy, Return

"""
The link on which the product will be displayed
"""


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        """
        If the user is autistic, then show the list of products
        """
        if request.user.is_authenticated:
            products = Product.objects.all()
            l = {'products': products}
            return render(request, self.template_name, l)
        else:
            return render(request, self.template_name, {})


"""
shopping list
"""


class BuyList(ListView):
    model = Buy
    paginate_by = 10
    template_name = 'buy.html '

    def get_queryset(self):
        return Buy.objects.filter(user=self.request.user)


"""
Returns list
"""


class ReturnListView(ListView):
    model = Return
    paginate_by = 10
    template_name = 'return_list.html'
    queryset = Return.objects.all()


"""
Link to which the user will be redirected in case of successful registration
"""


class RegisterFormView(FormView):
    form_class = UserCreationForm
    """
    There is a link to the login page for registered users.
    """
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        """
        We create a user if the data in the form were entered correctly.
        """
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        """
        If the data entered is incorrect, return to registration
        """
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = UserCreationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        """
       user object reception
        """
        self.user = form.get_user()

        """
        user authentication
        """
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(View):
    """
    Execute logout for user
    """

    def get(self, request):
        logout(request)
        """
        We redirect the user to the main page.
        """

        return HttpResponseRedirect('/')


