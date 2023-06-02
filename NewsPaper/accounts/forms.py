from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail



class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="user")
        user.groups.add(common_users)
        send_mail(
            subject='Добро пожаловать в наш Новостной портал!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        return user

