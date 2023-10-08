""" Example of tornado echo websocket, js websocket"""
import asyncio
from tornado import ioloop, web, websocket
import os
import json

from tornado.websocket import WebSocketHandler


class WSHandler(WebSocketHandler):
    live_web_sockets = set()
    removable = set()

    async def on_message(self, message):
        try:
            message = json.loads(message)
            print(message)
            message = message['message']
            self.send_message(message)    
        except websocket.WebSocketClosedError:
            self.close(reason='websocket closed') 
        except Exception as exc:
            print(exc)
            return
        
    @classmethod
    def send_message(cls, message):
        for ws in cls.live_web_sockets:
            if not ws.ws_connection or not ws.ws_connection.stream.socket:
                cls.removable.add(ws)
            else:
                ws.write_message(json.dumps({'event': message}))
        for ws in cls.removable:
            cls.live_web_sockets.remove(ws) 

    def open(self):
        # self.set_nodelay(True)
        self.live_web_sockets.add(self)

    # def on_close(self):
    #     print("WebSocket closed")



class MyFormHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index16.html")

    async def post(self):
        message = self.get_argument('message')
        print()


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    )
}


def make_app():
    print(settings)
    return web.Application(
        [
            (r"/main/", WSHandler),
            (r"/", MyFormHandler),
        ],
        **settings, autoreload=True,
        debug=True
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
