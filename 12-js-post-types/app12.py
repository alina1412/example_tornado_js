"""Example of js and jquery POST-requests. (script12.js)
Getting data from user and processing it in tornado web app.
Tornado post requests, arguments from frontend,
handling post-requests andn getting arguments from body in tornado example"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index12.html")


class MyFormHandler(web.RequestHandler):
    def post(self, args=None):
        message = self.get_argument('message')
        print("data from argument 1: ", message)
         

class MyFormHandler2(web.RequestHandler):
    def post(self, args=None):
        data = json.loads(self.request.body)
        print("data from body json 2: ", data)
        try:
            empty_message = self.get_argument('message')
        except Exception:
            print('no argument 2') 


class MyFormHandler3(web.RequestHandler):
    def post(self, args=None):
        data = json.loads(self.request.body)
        print("data from body json 3: ", data)
        try:
            empty_message = self.get_argument('message')
        except Exception:
            print('no argument 3') 


class MyFormHandler4(web.RequestHandler):
    def post(self, args=None):
        options = self.get_argument('options')
        print("data from argument 4: ", options) 
        try:
            print(self.request.body, "loaded as bytes")
            request_body_data = json.loads(self.request.body)
        except Exception:
            print('request_body_data - not loaded as json') 


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    )
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MainHandler),
            (r"/f1", MyFormHandler),
            (r"/f2", MyFormHandler2),
            (r"/f3", MyFormHandler3),
            (r"/f4", MyFormHandler4),
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
