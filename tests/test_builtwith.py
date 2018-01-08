import unittest
import builtwith


class TestBuiltWith(unittest.TestCase):
    def test_alibaba_indexpage(self):
        ALIBABA_INDEX_URL = 'http://www.alibaba.com/'
        response = builtwith.parse(ALIBABA_INDEX_URL)
        self.assertEqual(
            response, {
                'javascript-frameworks': ['Lazy.js'],
                'web-frameworks': ['Twitter Bootstrap']
            })


if __name__ == '__main__':
    unittest.main()
