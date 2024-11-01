import Q1 as Q1

def test_Q1():
    assert Q1.my_coordinates == [(28, 40), (42, 47), (52, 61)], 'Coordinates incorrect'
    assert Q1.my_list[Q1.target_loc] == Q1.target, "Incorrect word located"
    assert Q1.target2_loc == -1, 'Expecting -1, as word is not found in sentence'