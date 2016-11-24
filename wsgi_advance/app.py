from webob import Response
from webob.dec import wsgify
from webob import exc
from webob import Request

class Hello(object):
    @wsgify(RequestClass=Request)
    def __call__(self, request):
        return  Response('Hello, Secret World of WebOb !\n')
def app_factory(global_config, **local_config):
    return Hello()
