import pytest
from team1ArithmeticTrainer import functions

class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #
    @pytest.fixture
    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_checkPerfectSquare(self):
        """
        Tests the auxiliary function checkPerfectSquare that returns -1 
        if the number is not a perfect square and returns the square root
        of the number if the number is a perfect square.
        """
        expected=11
        actual=functions.checkPerfectSquare(121)
        assert actual == expected,"Expected to return 11 but returned something else."
        expected2=-1
        actual2=functions.checkPerfectSquare(11)
        assert actual2==expected,"Expected to return -1 but returned something else."
        expected3=1
        actual3=functions.checkPerfectSquare(1)
        assert actual3==expected,"Expected to return 1 but returned something else."
    
    def test_checkPerfectCube(self):
        """
        Tests the auxiliary function checkPerfectCube that returns -1 
        if the number is not a perfect cube and returns the cube root
        of the number if the number is a perfect cube.
        """
        expected=4
        actual=functions.checkPerfectCube(64)
        assert actual == expected,"Expected to return 4 but returned something else."
        expected2=-1
        actual2=functions.checkPerfectCube(11)
        assert actual2==expected,"Expected to return -1 but returned something else."
        expected3=1
        actual3=functions.checkPerfectCube(1)
        assert actual3==expected,"Expected to return 1 but returned something else."
        
    