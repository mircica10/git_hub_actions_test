import unittest

class TestBasic(unittest.TestCase):
  def setUp(self):
    pass

  def TestSum(self):
    v1 = 4
    v2 = 5
    v3 = v1 + v2
    assert(v3 == 9, 'sum should be 9')
  
  def TeamDown(self):
    pass
    

if __name__ == '__main__':
    unittest.main()
