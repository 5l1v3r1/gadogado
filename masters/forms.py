from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from .models import Author,Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'title': _('Title of Book'),
        }
        help_texts = {
            'title': _('Please input the title.'),
        }
        error_messages = {
            'title': {
                'max_length': _("This title's name is too long."),
            },
        }
        