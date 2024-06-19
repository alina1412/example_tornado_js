"""Html draft with bootstrap containers, Menu with submenu
draft of tornado web app with full-page html example."""
import asyncio
from tornado import web
import os


class MyHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index.html")



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
