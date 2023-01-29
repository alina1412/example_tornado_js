import asyncio
from tornado import web
import os
import json


class BaseHandler(web.RequestHandler):
    def initialize(self):
        self.name = "World"


class HelloHandler(BaseHandler):
    def get(self):
        self.write(f"Hello, {self.name }")


class MyFormHandler(web.RequestHandler):
    def get(self):
        print("MyFormHandler - get")
        self.render("./static/index.html")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        print("MyFormHandler - post")
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
    ),  # "web_tornado/static"
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
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
