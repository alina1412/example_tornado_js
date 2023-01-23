import asyncio
from tornado import web
import os
import json


class BaseHandler(web.RequestHandler):
    def initialize(self):
        self.session_id = None


class MainHandler(BaseHandler):
    def get(self):
        self.write(f"Hello, {self.session_id }")


class MyFormHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index.html")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        print("here")
        data = json.loads(self.get_argument("options", ""))
        print(data)
        self.write("You wrote " + json.dumps(data))


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ),  # "web_tornado/static", #
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    # "xsrf_cookies": True,
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/main", MainHandler),
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
