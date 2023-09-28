"""Example of tornado web page with submit form
and jquery submit script. How to make jquery post request."""
import asyncio
from tornado import web
import os
import json

num = 0

class MainHandler(web.RequestHandler):
    def get(self):
        global num
        print("get /main/")
        num += 1    # only increase by manually reload, cause gets to post method
        self.render("./static/index3.html", num=num)

    def post(self):
        options = self.get_argument('options')
        print('-', self.request.headers.get('Cookie'))
        self.write(options)


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
    "login_url": "/login",
}


def make_app():
    print(settings)

    return web.Application(
        [
            (r"/main/", MainHandler),
            (r"/form/", MyFormHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
