'''
Created on Apr 15, 2011

@author: jdrumgoole
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testBasetools(self):
        import basetools
        basetools.LOG.debug( "hello")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBasetools']
    unittest.main()