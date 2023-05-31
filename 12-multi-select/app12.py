"""Example of stylized multi-selector, get data from multiple selector.
usage of magicsuggest example,
getting data by js (jquery)
"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    '''page with a multi-selector'''
    def get(self):
        self.render("./static/index12.html")



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
