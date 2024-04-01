"""Example of selector for filters, reload after each choice.
usage of magicsuggest example,
getting data by js (jquery)
"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    '''page with filters'''
    FILTERS =      {
        '1': [{'name': 'FRUITS', 'val': 1, 'had_chosen': None}, {'name': 'VEGETABLES', 'val': 2, 'had_chosen': None}],
            '2': [{'name': 'COOKED', 'val': 1, 'had_chosen': None}, {'name': 'FRESH', 'val': 2, 'had_chosen': None}],
            '3': [{'name': "RED", 'val': 1, 'had_chosen': None}, {'name': "GREEN", 'val': 2, 'had_chosen': None}]
                                                                 }
                  

    def get(self):
        self.render("./static/index19.html", filters=self.FILTERS)

    def post(self):
        options = self.get_argument('options')
        options = json.loads(options)
        print("data   : ", options) 

        for id, filter in self.FILTERS.items():
            selected = options.get(f"{id}select[]", None)
            selected = int(selected[0]) if selected else ''
            print("selected: ", selected)

            for opt in filter:
                if opt['val'] == selected:
                    opt['had_chosen'] = True
                else:
                    opt['had_chosen'] = False

        print(self.FILTERS)
        self.render("./static/part.html", filters=self.FILTERS)


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
