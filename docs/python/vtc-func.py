from example.views import example_view
from reactpy import component, html

from reactpy_django.components import view_to_component


example_vtc = view_to_component(example_view)


@component
def my_component():
    return html.div(
        example_vtc(),
    )
