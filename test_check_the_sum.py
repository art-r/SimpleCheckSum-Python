import check_the_sum

def test_check_the_sum():
    """
    This is the test function for check_the_sum (used by pytest)
    It will check the checksum generation by checking the checksum of the LICENSE file
    If it succeeds the return value will be 0
    Else the return value will be 1 and thus pytest will fail
    """

    assert check_the_sum.check("LICENSE", "sha256", 
    "6b9a233c470849c3ba6fc3772467b6211c43dcf36748434ab70bc5915be308e1") == 0
