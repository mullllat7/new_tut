from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activation_mail(email, activation_code):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}/'
    message = f'''
    Спасибо за регистрацию!
    Пожалуйста активируйте ваш аккаунт.
    Активационная ссылка: {activation_url}
    '''

    send_mail(
        'Activate your account',
        message,
        'test@stack_overflow.kg',
        [email, ],
        fail_silently=False
    )