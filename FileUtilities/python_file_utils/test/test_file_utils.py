import unittest
from file_utils import FileUtils

class FileUtilsTests(unittest.TestCase):

    FILE_EXISTS = {
        "name": "existingFile",
        "extension": "txt"
    }

    FILE_AVAILABLE = {
        "name": "availableFileName",
        "extension": "json"
    }

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_file_name_exists(self):
        file_name = FileUtils.get_available_file_name(
            FileUtilsTests.FILE_EXISTS.get("name"),
            FileUtilsTests.FILE_EXISTS.get("extension")
        )

        self.assertEqual(
            file_name,
            f"{FileUtilsTests.FILE_EXISTS.get('name')} (1).{FileUtilsTests.FILE_EXISTS.get('extension')}"
        )

    def test_get_file_name_available(self):
        file_name = FileUtils.get_available_file_name(
            FileUtilsTests.FILE_AVAILABLE.get("name"),
            FileUtilsTests.FILE_AVAILABLE.get("extension")
        )

        self.assertEqual(
            file_name,
            f"{FileUtilsTests.FILE_AVAILABLE.get('name')}.{FileUtilsTests.FILE_AVAILABLE.get('extension')}"
        )

if __name__ == "__main__":
    unittest.main()
