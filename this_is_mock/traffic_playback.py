"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx, http


class AD:

    def request(self, flow: http.HTTPFlow):
        # 获取请求信息
        url = flow.request.pretty_url
        method = flow.request.method

    def response(self, flow: http.HTTPFlow):
        pass


addons = [
    AD()
]