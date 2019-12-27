import json
from urllib import request
from urllib.parse import urlencode
from blog.models import News


def add_news():
    # 配置聚合新闻的APPKey
    appkey = "a326ac7ce2a8d317fae228378a23638a"
    get_juhe_news(appkey, "GET")


def get_juhe_news(appkey, m="GET"):
    url = "http://v.juhe.cn/toutiao/index"
    params = {
        "type": "",  # 类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "key": appkey,  # 您申请的key
    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read().decode()
    res = json.loads(content)
    save_res(res)


def save_res(res):
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            json_str = res["result"]["data"]
            print(json_str)
            news_list = json.loads(str(json_str).replace("\"", '-').replace("'", '"'))
            for news in list(news_list):

                try:
                    user = News.objects.get(uniquekey=get_res(news, 'uniquekey'))
                except Exception as e:
                    user = None
                if user:
                    print('本条新闻数据已存在')
                else:
                    j = News()
                    j.title = get_res(news, 'title')
                    j.url = get_res(news, 'url')
                    j.date = get_res(news, 'date')
                    j.thumbnail_pic_s = get_res(news, 'thumbnail_pic_s')
                    j.thumbnail_pic_s02 = get_res(news, 'thumbnail_pic_s02')
                    j.thumbnail_pic_s03 = get_res(news, 'thumbnail_pic_s03')
                    j.category = get_res(news, 'category')
                    j.uniquekey = get_res(news, 'uniquekey')
                    j.author_name = get_res(news, 'author_name')
                    j.save()
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


def get_res(news,values):
    try:
        return news[values]
    except Exception as e:
        return ''


if __name__ == '__main__':
    main()