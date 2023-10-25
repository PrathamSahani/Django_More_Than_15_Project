
from django.conf import settings
from django.utils import timezone


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = None
        self.website= {
            'url': 'https://gfg.com',
            'debug':settings.DEBUG,
            'response_time': None
        }
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # print("Middelware Called")
        # Code to be executed for each request/response after
        # the view is called.
        
        # user_agent = request.META.get('HTTP_USER_AGENT')
        # print('####')
        # print(user_agent)
        # print("##")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(view_func)
        self.start_time = timezone.now()
        
    
    def process_template_response(self, request, response):
        # print("process_template_response")
        if settings.DEBUG:
            response.context_data['website'] = self.website
            response.context_data['website']['response_time'] =timezone.now()-self.start_time
        return response

