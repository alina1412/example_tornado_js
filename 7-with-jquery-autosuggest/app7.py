"""Example of autocomplete usage in html with js and jquery. (script7.js)
Suggestion of a fixed variants for autocomplete.
Getting data from user and processing it in tornado web app."""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index7.html")


class MyFormHandler(web.RequestHandler):
    def get(self, args=None):
        self.set_header("Content-Type", "text/plain")
        message = self.get_argument('message')
        id = self.get_argument('id')
        self.write("You wrote " + message)


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login"
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MainHandler),
            (r"/form/?", MyFormHandler),
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
