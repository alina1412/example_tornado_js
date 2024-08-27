"""Example of selector for filters.
usage of chosen plugin selectors example,
getting data by js (jquery), tornado app
"""
import asyncio
from tornado import web, autoreload
import os
import json


class MainHandler(web.RequestHandler):
    '''page with filters'''
    FILTERS =      {
        '1': [{'name': 'FRUITS', 'val': '1', 'had_chosen': None}, {'name': 'VEGETABLES', 'val': '2', 'had_chosen': None}],
            '2': [{'name': 'COOKED', 'val': '1', 'had_chosen': None}, {'name': 'FRESH', 'val': '2', 'had_chosen': None}],
            '3': [{'name': "RED", 'val': '1', 'had_chosen': None}, {'name': "GREEN", 'val': '2', 'had_chosen': None}],
            '4': [{'name': "AAA", 'val': '1', 'had_chosen': None}, {'name': "BBB", 'val': '2', 'had_chosen': None}]
                                                                 }
    lst = [{'name': 'apple', 'id': 1, 'chosen': ''}, {'name': 'banana', 'id': 2, 'chosen': ''}, {'name': 'apple3', 'id': 3, 'chosen': ''}, {'name': 'banana4', 'id': 4, 'chosen': ''},
               {'name': 'apple5', 'id': 5, 'chosen': ''}, {'name': 'banana6', 'id': 6, 'chosen': ''}]

    def get(self):
        self.render("./static/index.html", filters=self.FILTERS, single_opt='', part='', lst=self.lst)

    def post(self):
        options = self.get_argument('options')
        options = json.loads(options)
        print("data   : ", options) 
        single_opt = options.get('single', tuple())
        single_opt = single_opt if not single_opt else single_opt[0]

        for id, filter in self.FILTERS.items():
            selected = options.get(f"{id}select", tuple())
            print("selected: ", selected)

            for opt in filter:
                opt['had_chosen'] = True if opt['val'] in selected else False
               
        print(self.FILTERS)
        self.render("./static/part.html", filters=self.FILTERS, single_opt=single_opt, part='form')

class SuggestHandler(web.RequestHandler):
    '''page with suggest'''
    def get(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        query = self.get_argument('query', "")
        field = self.get_argument('field', "")
        
        suggest = [{
            'label': 'title',
            'id': 'code',
            'region_id': 1
        }]
    
        self.write(json.dumps(suggest)) 

    def post(self):
        options = json.loads(self.request.body)
        print("data   : ", options)
        single_opt = options.get('options', {}).get('suggest_form')
        for opt in MainHandler.lst:
            if str(opt['id']) == single_opt:
                opt['chosen'] = 1
            else:
                opt['chosen'] = 0

        self.render("./static/index.html", lst=MainHandler.lst, part='list')

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
            (r'/suggest/?', SuggestHandler),
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
