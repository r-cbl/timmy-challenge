from django.test import TestCase

from timmy_mountains.helpers.mountain_helper import MountainHelper


# helpers test
class MountainTunnelTests(TestCase):
    """
       returns True if the input is a valid mountain with tunnels. Otherwise, returns False
    """

    def test_success_1(self):
        helper_test = MountainHelper()
        input_mountain = r"/>//\\<\ "
        input_mountain = input_mountain[:-1]  # due to language limitations
        self.assertIs(helper_test.validate_tunnel_mountain(input_mountain), True)

    def test_success_2(self):
        helper_test = MountainHelper()
        input_mountain = r"//>/\<\/>/>/\<\<\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_tunnel_mountain(input_mountain), True)

    def test_fail_1(self):
        helper_test = MountainHelper()
        input_mountain = r"/>//\\\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_tunnel_mountain(input_mountain), False)

    def test_fail_2(self):
        helper_test = MountainHelper()
        input_mountain = r"///\<\/>/>/\\\<\\ "
        input_mountain = input_mountain[:-1]
        self.assertIs(helper_test.validate_tunnel_mountain(input_mountain), False)
