"""How to make an alert with js and jquery after the submit.
Success flying alert. Example of tornado web app with a submit form and an alert."""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    def get(self):
        # print("get /main/")
        self.render("./static/index4.html")


class MyFormHandler(web.RequestHandler):
    def post(self):
        # print("post /form/")
        self.set_header("Content-Type", "text/plain")
        data = json.loads(self.request.body)
        print(data)
        self.write("You wrote " + json.dumps(data))


settings = {
    "static_path": os.path.join(
        os.path.dirname(__file__), "static"
    )
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
