import unittest
import map

class TestCases(unittest.TestCase):
   def test_1(self):
      t =[1,2,3,4,5]
      self.assertEqual(map.square_all(t),[1,4,9,16,25])
   def test_2(self):
      t=[-1,-2,-3,-4,-5]
      self.assertEqual(map.square_all(t),[1,4,9,16,25])
   def test_3(self):
      t=[1,2,3,4,5]
      self.assertEqual(map.add_n_all(t,2),[3,4,5,6,7])
   def test_4(self):
      t=[1,-2,3,-4,5]
      self.assertEqual(map.add_n_all(t,-1),[0,-3,2,-5,4])
   def test_5(self):
      t=[[3,4],[6,7],[8,9]]
      self.assertAlmostEqual(map.distance_all(t),[5,9.2,12.0])
   def test_6(self):
      t=[[-6,-7],[8,9],[0,2]]
      self.assertAlmostEqual(map.distance_all(t),[9.2,12.0,2])
      
      


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
   

