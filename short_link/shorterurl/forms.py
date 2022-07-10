from django import forms

from shorterurl.models import Short_link


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your long URL to shorten"}))

    class Meta:
        model = Short_link
        fields = ('long_url',)
