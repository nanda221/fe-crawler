import unittest
from urllib import error, request


class TestRobotFile(unittest.TestCase):
    def test_baidu_robotfile(self):
        try:
            BAIDU_ROBOTS_URL = 'http://www.baidu.com/robots.txt'
            response = request.urlopen(BAIDU_ROBOTS_URL)
            robots_txt = response.read()
            print(robots_txt)
        except error.URLError as e:
            print('We failed to reach: {0}'.format(BAIDU_ROBOTS_URL))


if __name__ == '__main__':
    unittest.main()
