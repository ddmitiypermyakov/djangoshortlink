from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from shorterurl.models import Short_link
from shorterurl.forms import ShortForm


class ShortUrlHome(CreateView):
    """
    Create Short URL
    """
    template_name = "index.html"
    context_data = {}
    context_data['form'] = ShortForm()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, self.context_data)
        elif request.method == 'POST':
            form = ShortForm(request.POST)
            if form.is_valid():
                object_url = form.save(commit=False)
                object_url.user_use_id = request.user.id
                form.save()
                new_url = request.build_absolute_uri('/') + object_url.short_url
                long_url = object_url.long_url
                self.context_data['new_url'] = new_url
                self.context_data['long_url'] = long_url
                return render(request, self.template_name, self.context_data)
            self.context_data['errors'] = form.errors

            return render(request, self.template_name, self.context_data)

def my_history_url(request):
    """
    My History Link
    """
    link_user = Short_link.objects.filter(user_use_id=request.user.id).order_by('created')
    template = "history.html"
    context= {}
    context['link_user'] = link_user
    context['new_url'] = request.build_absolute_uri('/')
    return render(request, template, context)

def redirect_url_view(request, short_part):
    """
    Redirect Short URL to Long URL
    """
    shortener = get_object_or_404(Short_link, short_url=short_part)
    return HttpResponseRedirect(shortener.long_url)
