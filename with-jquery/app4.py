import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    def get(self):
        print("get /main/")
        self.render("./static/index4.html")


class MyFormHandler(web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/plain")
        print("post /form/")
        data = json.loads(self.request.body)
        print(data)
        self.write("You wrote " + json.dumps(data))


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    ), 
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login"
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/main/", MainHandler),
            (r"/form/", MyFormHandler),
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
