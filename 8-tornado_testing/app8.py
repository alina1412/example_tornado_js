import asyncio
from tornado import web
import json


def function_for_test():
    return False


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hi")

    def post(self):
        login = self.get_argument("login", None)
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + json.dumps({"login": login}))

    def put(self):
        self.set_header("Content-Type", "text/plain")
        self.write(json.dumps({"res": function_for_test()}))


settings = {"cookie_secret": "jhvkv.kjb;bkucthtxgrx"}


def make_app():
    return web.Application(
        [
            (r"/", MainHandler),
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
