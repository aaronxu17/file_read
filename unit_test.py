# unit_test
import os
import os.path
import io, sys
import unittest

Max_File_Size = 1000000.0 # MB,1TB

filename = 'test_file.txt'


# Here's the "unit tests".
class TestCase(unittest.TestCase):

    def test_wrong_filename(self):
		self.assertFalse(os.path.isfile('wrongfile.txt') ,"Can access wrong file!")
     
    def test_access_file(self):
        self.assertTrue(os.access(filename,os.R_OK))
    
    def test_huge_file_size(self):
        self.assertLessEqual(float(os.path.getsize(filename))/(1024*1024), Max_File_Size)
    
    def test_sum_exceeds_max_float(self):
        numsum = 2*sys.float_info.max
        self.assertTrue(numsum>sys.float_info.max)

        

if __name__ == '__main__':
    unittest.main()

