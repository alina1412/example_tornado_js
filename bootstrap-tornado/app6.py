import asyncio
from tornado import web
import os


class HelloHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World")


class MyHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index6.html")



settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/hello", HelloHandler),
            (r"/", MyHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
