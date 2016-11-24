import wsgi
#import app

class WSGIService(object):
    def __init__(self):
#	self.loader = wsgi.Loader()
#        self.app = self.loader.load_app()
        self.app = wsgi.Loader().load_app()
        self.server = wsgi.Server(self.app,
                                  '0.0.0.0',
                                  8080)
    def start(self):
        self.server.start()

    def wait(self):
        self.server.wait()

    def stop(self):
        self.server.stop()

#class mes(object):
#    def __init__(self):
#        self.headers = {'X-Auth-Token':'open-sesame'}
#        self.get_reponse = app.Hello()

if __name__ == "__main__":
    server = WSGIService()
#    m = mes()
#    print server.app(m)
    server.start()
    server.wait()
