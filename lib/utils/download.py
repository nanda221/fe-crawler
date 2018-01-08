from urllib import error, request
import ssl

# 阻止ssl验证，参考：http://blog.csdn.net/hudeyu777/article/details/76021573
ssl._create_default_https_context = ssl._create_unverified_context


class Download:
    # def __init__(self):
    default_headers = {
        'User_agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Connection':
        'Keep-Alive',
    }

    def html(self, url, headers=default_headers, num_retries=2):
        html = None

        # another way is: dict1.update(dict2). because update method returns None, we need add: `dict_final = dict1` after that. but, it pollutes dict.
        # anyway, the spread systax pattern below looks better.
        req_headers = {**self.default_headers, **(headers or {})}

        req_body = request.Request(url, headers=req_headers)
        ssl._create_unverified_context()
        try:
            # 创建未经验证的上下文，以阻止ssl验证，参考：http://blog.csdn.net/hudeyu777/article/details/76021573
            # ssl_context = ssl._create_unverified_context()
            response = request.urlopen(req_body).read()
            # bytes converts to string
            html = response.decode()

        except ValueError as e:
            print('invalid url format')
        except error.HTTPError as e:
            print('HttpError(\033[31m{error.code}\033[0m): {error.reason}'.
                  format(error=e))
            if num_retries > 0:
                if 500 <= e.code < 600:
                    print(
                        'retry to download again, {} times left(include this time).'.
                        format(num_retries))
                    return self.html(url, headers, num_retries - 1)
                else:
                    print('no need to retry.')
            else:
                print('no times for retry.')

        except error.URLError as e:
            print('We failed to reach the server. The reason shows below:')
            print(e.reason)
        except Exception as e:
            print(e)
        else:
            print('download success!')
        finally:
            return html

    def robots(self, robots_url):
        robots_txt = None
        try:
            response = request.urlopen(robots_url)
            robots_txt = response.read()
        except error.URLError as e:
            print('We failed to reach the server: {0}'.format(robots_url))
        finally:
            return robots_txt


download = Download()

# print(download.html('http://www.baidu21321321.com', None, 3))
# print(download.html('http://httpstat.us/500'))
# print(download.html('http://www.baidu.com'))
# print(download.robots('http://www.baidu.com/robots.txt'))
