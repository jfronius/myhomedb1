import hw1
import unittest
import os

class Prob11Tests(unittest.TestCase):
  """Tests of vowel count"""

  def test_vowel_count(self):
    """Testing vowel_count"""
    tests = [('Harry', 2),
             ('hairy', 3),
             ('hare', 2),
             ('the', 1),
             ('Mr', 0)]
    for tst in tests:
      self.assertEqual(tst[1], hw1.vowel_count(tst[0]),
                       'Failed on vowel_count("' + tst[0]
                       + '"), result should be ' + str(tst[1]))

class Prob2Tests(unittest.TestCase):
  """Tests of syllable_count"""

  def test_syllable_count(self):
    tests = [('Harry', 2),
             ('hairy', 2),
             ('hare', 1),
             ('the', 1)]
    for tst in tests:
      self.assertEqual(tst[1], hw1.syllable_count(tst[0]),
                       'Failed on syllable_count("' + tst[0]
                       + '"), result should be ' + str(tst[1]))
  
def random_filename():
  """Creates a random sequence of 6 lowercase letters"""
  import string
  import random
  return "".join([random.choice(string.ascii_lowercase) for i in range(6)])

class RandFileTest(unittest.TestCase):
  """Base class for tests that need random file"""
  def setUp(self):
    self.infilename = random_filename() + self.namesuffix
    with open(self.infilename, 'w') as f:
      f.writelines([val + '\n' for val in self.sample_data])
  
  def tearDown(self):
    if os.path.exists(self.infilename):
      os.remove(self.infilename)

class Prob3Tests(RandFileTest):
  """Tests of filter_dict"""

  sample_data = ['abc', 'ab', 'bcdef', 'abcd',  'bcd', 'cdefg', 'bd']
  results = ['abc\n', 'abcd\n',  'bcd\n']

  def __init__(self, methodName='runTests'):
    super(Prob3Tests, self).__init__(methodName)
    self.namesuffix = '_prob3.txt'

  def setUp(self):
    super(Prob3Tests, self).setUp()
    self.outfilename = 'filtered-' + self.infilename
  
  def test_filter_dict(self):
    hw1.filter_dict(self.infilename, 3, 4)
    # check for creation of correct file
    self.assertTrue(os.path.exists(self.outfilename), 
                    'Output file not created or misnamed! Should be named '
                    + self.outfilename)
    # check file contents
    if os.path.exists(self.outfilename):
      with open(self.outfilename, 'r') as resfile:
        your_output = "".join(resfile.readlines())
      self.assertMultiLineEqual(''.join(self.results), your_output)
    else:
      self.fail('Could not test output due to the fact that the output'
                + ' file is either misnamed or missing')
      
class Prob4Tests(RandFileTest):
  """Tests of gematria"""

  sample_data = sorted(['buffer', 'coder', 'find', 'racer', 'gore', 'bios', 'knife', 'debased', 'shameful', 'acted', 'flower'])
  results = sorted(['coder', 'racer', 'gore', 'bios', 'knife'])

  def __init__(self, methodName='runTests'):
    super(Prob4Tests, self).__init__(methodName)
    self.namesuffix = '_prob4.txt'
    
  def test_gematria(self):
    your_results = hw1.gematria('Phil', self.infilename)
    self.assertListEqual(self.results, your_results)

class Prob5Tests(unittest.TestCase):
  """Tests of credit_check"""

  sample_data = ['26174557', '05448727']
  def test_credit_check(self):
    tests = [('26174557', True),
             ('05448727', False)]
    for tst in tests:
      self.assertEqual(tst[1], hw1.credit_check(tst[0]),
                       'Failed on credit_check("' + tst[0]
                       + '"), result should be ' + str(tst[1]))
      
if __name__ == "__main__":
  unittest.main(verbosity=2,exit=False)
    
