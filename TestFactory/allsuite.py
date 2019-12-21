import datetime
import os
import unittest

from HtmlTestRunner import HTMLTestRunner

import TestFactory.TestLondanTheatre


suite = unittest.TestSuite()

suite.addTests([

    unittest.defaultTestLoader.loadTestsFromModule(TestFactory.TestLondanTheatre, True)

])
now = datetime.datetime.now()

getDate = str(now.year) + str("-") + str(now.month) + str("-") + str(now.day)

testRunner = HTMLTestRunner(
    output='./Reports'
)

testRunner.run(suite)
