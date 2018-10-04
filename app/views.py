from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from app.models import Movie


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


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
            message = "We cannot find your account."
            return render(request, "registration/login.html", {"message": message})


@method_decorator(login_required, name='dispatch')
class SearchView(View):
    def get(self, request):
        return render(request, "search.html")


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name='dispatch')
class FavouriteView(View):
    def get(self, request):
        list_movie = Movie.objects.filter(user=request.user).order_by(
            "-pk"
        )
        paginator = Paginator(list_movie, 5)
        page = request.GET.get('page', 1)
        try:
            movie = paginator.page(page)
        except PageNotAnInteger:
            movie = paginator.page(1)
        except EmptyPage:
            movie = paginator.page(paginator.num_pages)

        return render(request, "favourite.html", {"list_movie": movie})

    def post(self, request):
        data = JSONParser().parse(request)
        try:
            Movie.objects.create(
                user=request.user,
                title=data["title"],
                year=data["year"],
                actors=data["actors"],
                awards=data["awards"],
                country=data["country"],
                dvd=data["dvd"],
                director=data["director"],
                genre=data["genre"],
                plot=data["plot"],
                released=data["released"],
                runtime=data["runtime"],
                poster=data["poster"],
            )
            return HttpResponse(status=201)
        except Exception:
            return HttpResponse(status=403)
