import asyncio
from tornado import web
import os


class ImgHandler(web.RequestHandler):
    def get(self):
        """shows an img on html page"""
        self.render("./static/index5.html")


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
            (r"/get", ImgHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
