import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    """Show a page with slide-show images"""
    def get(self):
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
        self.render("./static/index9.html", slides=slides)



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
