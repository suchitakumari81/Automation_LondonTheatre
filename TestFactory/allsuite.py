import datetime
import os
import unittest

from HtmlTestRunner import HTMLTestRunner

import TestFactory.TestLondanTheatre

folder = './Snapshots/Chrome/ActualScreenshots'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

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
