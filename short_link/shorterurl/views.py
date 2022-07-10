from django.shortcuts import render
from django.views.generic import CreateView
from shorterurl.models import Short_link
from shorterurl.forms import ShortForm


class ShortUrlHome(CreateView):
    template_name = "index.html"
    context_data = {}
    context_data['form'] = ShortForm()

    def dispatch(self, request, *args, **kwargs):
        print(self.context_data)
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
