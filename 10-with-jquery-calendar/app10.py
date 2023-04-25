"""Example of datepicker (datetimepicker) 
https://github.com/trentrichardson/jQuery-Timepicker-Addon

input date and time and validation of it,
example of jquery datetime input vidget
"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index10.html")



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
