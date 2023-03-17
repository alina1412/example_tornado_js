"""Simple example of tornado web app.
How to make navbar in html, responsive bootstrap navbar."""
import asyncio
from tornado import web
import os


class MainHandler(web.RequestHandler):
    def get(self):
        """Shows a navbar draft"""
        self.render("./static/index2.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MainHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
