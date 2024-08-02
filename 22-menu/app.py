"""Example 
 tornado app
"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):  

    def get(self):
        self.render("./static/index.html")

    # def post(self):
    #     options = self.get_argument('options')
    #     ...


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MainHandler)
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
