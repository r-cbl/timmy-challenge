from django.test import TestCase

from timmy_mountains.helpers.mountain_helper import MountainHelper


# helpers test
class MountainTests(TestCase):
    """
       returns True if the input is a valid mountain. Otherwise, returns False
    """

    def test_success_1(self):
        helper_test = MountainHelper()
        input_mountain = r"/\ "
        input_mountain = input_mountain[:-1]  # due to language limitations
        self.assertIs(helper_test.validate_mountain(input_mountain), True)

    def test_success_2(self):
        helper_test = MountainHelper()
        input_mountain = r"//\\//\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), True)

    def test_success_3(self):
        helper_test = MountainHelper()
        input_mountain = r"////\\\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), True)

    def test_success_4(self):
        helper_test = MountainHelper()
        input_mountain = r"////\\\/////\\\\\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), True)

    def test_fail_1(self):
        helper_test = MountainHelper()
        input_mountain = r"//\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), False)

    def test_fail_2(self):
        helper_test = MountainHelper()
        input_mountain = r"/\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), False)

    def test_fail_3(self):
        helper_test = MountainHelper()
        input_mountain = r"\///\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), False)

    def test_fail_4(self):
        helper_test = MountainHelper()
        input_mountain = r"///\\\\/ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_mountain(input_mountain), False)
