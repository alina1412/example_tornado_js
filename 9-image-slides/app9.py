"""Examples of showing images with js/jquery plugins"""
import asyncio
from tornado import web, autoreload
import os
import json


slides = [
    {
    "title" : "1/2",
    "img" : '1.png'
    },
    {
        "title" : "2/2",
        "img" : '2.png'
    }
]

class MainHandler(web.RequestHandler):
    """Show a page with slide-show images"""
    def get(self):
        self.render("./static/index9.html", slides=slides)


class SecondHandler(web.RequestHandler):
    """Second example with slide-show images"""
    def get(self):
        self.render("./static/index9_2.html", slides=slides)


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MainHandler),
            (r"/s", SecondHandler),
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
