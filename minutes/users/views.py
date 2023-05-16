from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from utils.databases_utils import get_last_id, get_next_id
from protocol.models import ProtocolData
from .forms import UserLoginForm
from .models import CustomUser
from users.decorators import user_not_authenticated
from users.forms import UserLoginForm

@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserRegistrationForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("index")


def block_user(user):
    # Если пользователь заблокирован, выкидываем его из системы
    user.is_active = False
    user.is_staff = False
    user.is_superuser = False
    user.save(update_fields=['is_active', 'is_staff', 'is_superuser'])
    # Отправляем сообщение пользователю
    messages.info(request, "You have been blocked and logged out.")


def blocked_page(request):
    return render(request, 'users/blocked_page.html')


@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                if user.is_blocked:
                    return redirect("blocked_page")
                else:
                    if len(user.first_name) > 1:
                        messages.success(request, f"Dear <b>{user.first_name}</b>, you have been logged in")
                    else:
                        messages.success(request, f"Dear <b>{user.username}</b>, you have been logged in")
                    return redirect("index")
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                messages.error(request, error)
    else:
        form = UserLoginForm()
    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )


# def custom_login(request):
#     if request.method == "POST":
#         form = UserLoginForm(request=request, data=request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 if len(user.first_name) > 1:
#                     messages.success(request, f"Dear <b>{user.first_name}</b>, you have been logged in")
#                 else:
#                     messages.success(request, f"Dear <b>{user.username}</b>, you have been logged in")
#                 return redirect("index")
#         else:
#             for key, error in list(form.errors.items()):
#                 if key == 'captcha' and error[0] == 'This field is required.':
#                     messages.error(request, "You must pass the reCAPTCHA test")
#                     continue
#                 messages.error(request, error)
#     form = UserLoginForm()
#     return render(
#         request=request,
#         template_name="users/login.html",
#         context={"form": form}
#     )


@login_required
@user_not_authenticated
def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Your profile has been updated!')
            return redirect('profile', user_form.username)
        for error in list(form.errors.values()):
            messages.error(request, error)
    user = get_user_model().objects.filter(username=username).first()
    if user:
        User = get_user_model()
        user = User.objects.get(username=username)
        protocols = ProtocolData.objects.filter(user=user)  # Retrieve the user's protocols

        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        last_protocol = ProtocolData.objects.order_by('-id').first()
        context = {
            'title': 'Create_doc_online - Index',
            'form': form,
            'last_db_id': get_last_id(),
            'edit_protocol_url': reverse('edit_protocol', args=(get_last_id(),)),
            'data': last_protocol,
            'protocols': protocols,  # Pass the protocols to the template context
        }
        return render(
            request,
            'users/profile.html',
            context
        )
    return redirect("index")



