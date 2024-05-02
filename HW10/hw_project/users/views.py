from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

class RegisterView(View):
    template_name = "users/register.html"
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["pass1"])
            new_user.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"Вітаємо {username}. Ваш акаунт успішно створено"
            )
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})


def logout_view(request):
    logout(request)
    return redirect('users:login')