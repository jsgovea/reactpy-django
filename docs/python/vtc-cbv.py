from django.http import HttpResponse
from django.views import View
from reactpy import component, html

from reactpy_django.components import view_to_component


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World!")


vtc = view_to_component(HelloWorldView)


@component
def my_component():
    return html.div(
        vtc(),
    )
