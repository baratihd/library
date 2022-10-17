from django import forms


class BookSearchForm(forms.Form):
    search = forms.CharField()
