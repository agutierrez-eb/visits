from django.template.loader import render_to_string
from django.http import HttpResponse
from visits_app.redis_connection import RedisConnection

# Create your views here.

redis_connection = RedisConnection()

def index(request):

    redis_connection.increment_visits()

    rendered = render_to_string(
        'visits_app/visits_list.html',
        {
            'visits_number': str(redis_connection.get_visits())
        }
    )

    return HttpResponse(rendered)
