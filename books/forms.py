from django.contrib.auth.forms import UserCreationForm
from .models import Book


class SignUpForm(UserCreationForm):
    class Meta:
        model = Book
        fields = ('email',)