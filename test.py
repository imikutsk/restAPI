from api import GetText
from api import GetImages
import unittest


class GetTest(unittest.TestCase):

    def test_getText(self):

        self.assertEqual(GetText.get(1), 'Save ixab file in folder txt')

    def test_getImages(self):
        self.assertEqual(GetImages.get(1), 20)



if __name__ == '__main__':
    unittest.main()

