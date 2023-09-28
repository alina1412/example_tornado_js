'''tornado test example 
pytest 3-tornado_js_post/test_3.py '''
import json

import pytest
import tornado
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase

from app3 import MainHandler
# pytestmark = pytest.mark.asyncio

# @pytest.fixture
# def app():
#     return tornado.web.Application([(r"/", MainHandler)])


class TestMainHandler(AsyncHTTPTestCase):
    def get_app(self):
        return tornado.web.Application([(r"/", MainHandler)])

    # @pytest.mark.asyncio
    @tornado.testing.gen_test
    async def test_post_options(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)
        http_client = AsyncHTTPClient(self.io_loop)

        response = await http_client.fetch(self.get_url('/'), 
                                           method="POST", 
                                           body=f'options={options_json}'
                                           )
        
        assert response.code == 200
        assert response.body == options_json.encode()

