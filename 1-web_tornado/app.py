"""Simple tornado application with get and post handlers.
Render html page with tornado. Input form in tornado web.
Usage of jquery for post"""
import asyncio
from tornado import web
import os
import json


class HelloHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World")


class MyFormHandler(web.RequestHandler):
    def get(self):
        # print("MyFormHandler - get")
        self.render("./static/index.html")

    def post(self):
        # print("MyFormHandler - post")
        self.set_header("Content-Type", "text/plain")
        data = self.request.body
        try:
            data = json.loads(data)
            self.write("You wrote " + json.dumps(data))
        except json.JSONDecodeError:
            print("JSONDecodeError")
        print(data)
        # self.redirect("/")


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/hello", HelloHandler),
            (r"/", MyFormHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
