import unittest
import filter

class TestCases(unittest.TestCase):
   def test_1(self):
      t=[1,2,-1,-2,4,5]
      self.assertEqual(filter.are_positive(t),[1,2,4,5])
   def test_2(self):
      t=[-1,-2,-3,-4,5]
      self.assertEqual(filter.are_positive(t),[5])
   def test_3(self):
      t=[1,3,1,2,-9,5]
      self.assertEqual(filter.are_greater_than(t,2),[3,5])
   def test_4(self):
      t=[7,3,2,1,9,8]
      self.assertEqual(filter.are_greater_than(t,4),[7,9,8])
   def test_5(self):
      t=[[1,2],[3,4],[-1,2],[-2,2]]
      self.assertEqual(filter.are_in_first_quadrant(t),[[1,2],[3,4]])
   def test_6(self):
      t=[[3,4],[-2,-2],[-1,2],[0,0]]
      self.assertEqual(filter.are_in_first_quadrant(t),[[3,4],[0,0]])
      
                     


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

