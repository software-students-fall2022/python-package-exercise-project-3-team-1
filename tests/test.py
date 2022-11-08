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
        
    def test_add(self):
        """
        Tests the auxiliary function add that returns sum of two numbers
        """
        assert functions.add(20,1)==21, "Expected to return sum but returned something else."
        assert functions.add(1,100)==101, "Expected to return sum but returned something else."
        assert functions.add(0,0)==0, "Expected to return sum but returned something else."
        
    def test_subtract(self):
        """
        Tests the auxiliary function subtract that returns difference of two numbers
        """
        assert functions.subtract(20,1)==19, "Expected to return difference but returned something else."
        assert functions.subtract(1,1)==0, "Expected to return difference but returned something else."
        assert functions.subtract(1,3)==-2, "Expected to return difference but returned something else."
    
    def test_multiply(self):
        """
        Tests the auxiliary function multiply that returns product of two numbers
        """
        assert functions.multiply(20,1)==20, "Expected to return product but returned something else."
        assert functions.multiply(1,0)==0, "Expected to return product but returned something else."
        assert functions.multiply(5,-2)==-10, "Expected to return product but returned something else."
    
    def test_divide(self):
        """
        Tests the auxiliary function divide that returns quotient when
        one number is divided by another number
        """
        assert functions.divide(20,5)==4, "Expected to return quotient but returned something else."
        assert functions.divide(2,1)==2, "Expected to return quotient but returned something else."
        assert functions.divide(0,1)==0, "Expected to return quotient but returned something else."
    
    def test_sqr_root(self):
        """
        Tests the auxiliary function sqr_root that returns square root of a
        number
        """
        assert functions.sqr_root(36)==6, "Expected to return square root but returned something else."
        assert functions.sqr_root(1)==1, "Expected to return square root but returned something else."
        assert functions.sqr_root(64)==8, "Expected to return square root but returned something else."
    
    def test_cube_root(self):
        """
        Tests the auxiliary function cube_root that returns cube root of a
        number
        """
        assert functions.cube_root(8)==2, "Expected to return cube root but returned something else."
        assert functions.cube_root(1)==1, "Expected to return cube root but returned something else."
        assert functions.cube_root(64)==4, "Expected to return cube root but returned something else."
    
    def test_modulus(self):
        """
        Tests the auxiliary function add that returns remainder when one
        number is divided by another
        """
        assert functions.modulus(20,5)==0, "Expected to return remainder but returned something else."
        assert functions.modulus(1,100)==1, "Expected to return remainder but returned something else."
        assert functions.modulus(23,3)==2, "Expected to return remainder but returned something else."