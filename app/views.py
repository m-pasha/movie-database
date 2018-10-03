from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        name = "Home page"
        return render(request, "home.html", {"name": name})


class LoginView(View):
    def get(self, request):
        return render(request, "registration/login.html")

    def post(self, request):
        form_data = request.POST.dict()
        try:
            user = User.objects.get(username=form_data["username"])
            if user.is_active:
                user = authenticate(username=form_data["username"], password=form_data["password"])
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    message = "Please enter a correct email and password. Note that both fields may be case-sensitive."
                    return render(request, "registration/login.html", {"message": message})
            else:
                message = "Your account is inactive. Please activate your account."
                return render(request, "registration/login.html", {"message": message})
        except User.DoesNotExist:
            message = "We cannot find your account. Please Sign up first."
            return render(request, "registration/login.html", {"message": message})
