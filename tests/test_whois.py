"""
We can simply use: "whois url" command in shell.
Here we use python-whois to resolve this.
A simple blog(http://blog.163.com/weak_time/blog/static/258528091201694250835/) explains the whois protocol and service.
"""

import unittest
import whois


class TestWhoIs(unittest.TestCase):
    def test_whois_alibaba(self):
        ALIBABA_URL = 'alibaba.com'
        response = whois.whois(ALIBABA_URL)
        print(response)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
