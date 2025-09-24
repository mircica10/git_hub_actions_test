import unittest

class TestBasic(unittest.TestCase):
  
    def setUp(self):
        pass

    def test_sum(self):
        v1, v2 = 4, 5    
        v3 = v1 + v2
        assert v3 == 9, 'sum should be 9'

    def test_mul(self):
        v1, v2 = 3, 4
        v3 = v1 * v2
        assert v3 == 12, 'mul should be 12'
  
    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
