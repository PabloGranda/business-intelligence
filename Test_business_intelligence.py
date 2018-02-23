# tests.py

import unittest
import json
import GlucosaChi

class TestDensityMapsMethods(unittest.TestCase):

    def test_prediction(self):
    	json_data = GlucosaChi.prediccion()
    	js = json.loads(json_data)
    	self.assertTrue(int(js["value"]) > 0 and int(js["value"])<300)
    
if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

# if __name__ == '__main__':
#     unittest.main()