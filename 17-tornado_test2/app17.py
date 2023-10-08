"""Example of tornado app fot test.
tornado handlers for testing arguments"""
import asyncio
from tornado import web
import json


class MainHandler(web.RequestHandler):
    def get(self):
        data = self.get_argument('options')
        print('get:' + data)
        self.write('hi')

    def post(self):
        data = self.get_argument('options')
        print('\n in post handler: ' + data)
        self.write(data)

    def put(self):
        body = self.request.body
        print('\n body:' + str(body))
        data = self.get_argument('options', '')
        loaded_dict_data = json.loads(data) if data else None
        print('\n put:' + str(data) + '-')
        # additional = self.get_argument('additional', '')
        # print('put:' + str(additional) + '-')
        self.write("hi")


def make_app():
    return web.Application([
            (r"/", MainHandler),
        ]
    )


async def main():
    application = make_app()
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
