import json

from mitmproxy import ctx, http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows" % self.num)

        # 使用 request 事件实现 map local
        if 'https://stock.xueqiu.com/v5/stock/batch/quote.json?_t' in flow.request.pretty_url:
            # 读取数据文件
            with open('data.json', encoding='utf-8') as f:
                # 给 flow.response 赋值：状态码， 响应体， 响应头
                flow.response = http.HTTPResponse.make(200,
                    f.read(),
                    {'Content-Tyo': 'text/html'}
                )

    def response(self, flow: http.HTTPFlow):
        if 'https://stock.xueqiu.com/v5/stock/batch/quote.json?_t' in flow.request.pretty_url:
            # 拿到响应数据
            data = json.loads(flow.response.text)
            # 修改响应数据
            data['data']['items'][0]['quote']['name'] = 'test'
            # 给响应数据重新赋值
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]