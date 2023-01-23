from django.test import TestCase

from timmy_mountains.helpers.mountain_helper import MountainHelper


# helpers test
class FixMountainTests(TestCase):
    """
       returns the number of changes needed to convert the input into a mountain
    """

    def test_case_1(self):
        helper_test = MountainHelper()
        input_mountain = r"/\\ "
        input_mountain = input_mountain[:-1]  # due to language limitations
        self.assertIs(helper_test.validate_fix_not_mountain(input_mountain), 1)

    def test_case_2(self):
        helper_test = MountainHelper()
        input_mountain = r"\///\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_fix_not_mountain(input_mountain), 2)

    def test_case_3(self):
        helper_test = MountainHelper()
        input_mountain = r"//\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_fix_not_mountain(input_mountain), 0)
