import unittest

from HtmlTestRunner import HTMLTestRunner

import TestFactory.TestLondanTheatre


suite = unittest.TestSuite()

suite.addTests([

    unittest.defaultTestLoader.loadTestsFromModule(TestFactory.TestLondanTheatre, True)

])

testRunner = HTMLTestRunner(
    output='./Reports'
)

testRunner.run(suite)
