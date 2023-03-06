import asyncio
import json

from tornado import web

from for_test import function2_for_test, async_function_for_test


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


class MoreForMock(web.RequestHandler):
    def get(self):
        self.write(json.dumps({"res": function2_for_test()}))

    async def put(self):
        ans = json.dumps({"res": await async_function_for_test()})
        self.write(ans)

    async def post(self):
        letters = "abc"
        ans = json.dumps({"res": letters})
        return self.write(ans)


settings = {"cookie_secret": "jhvkv.kjb;bkucthtxgrx"}


def make_app():
    return web.Application(
        [
            (r"/", MainHandler),
            ("/m", MoreForMock)
        ],
        **settings,
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
