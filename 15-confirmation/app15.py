"""Example of bootstrap-confirmation with bootstrap 4, popper, js and jquery. 
button with confirmation window for submit
"""
import asyncio
from tornado import web, autoreload
import os
import json



class MyFormHandler(web.RequestHandler):
    def get(self):
        self.render("./static/index15.html")

    def post(self, args=None):
        message = self.get_argument('message')
        print("data from argument 1: ", message)
         


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    )
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/", MyFormHandler),
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
