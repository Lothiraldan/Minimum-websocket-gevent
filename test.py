import json
import time
import random

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


class WebSocketApp(object): 
    '''Funnel messages coming from an inproc zmq socket to the websocket''' 
 
    def __call__(self, environ, start_response):
        ws = environ['wsgi.websocket']
        x = 0
        while True: 
            data = json.dumps({'x': x, 'y': random.randint(1, 5)})
            ws.send(data) 
            x += 1
            time.sleep(0.5)

def main():
    server = pywsgi.WSGIServer(("", 10000), WebSocketApp(),
        handler_class=WebSocketHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()