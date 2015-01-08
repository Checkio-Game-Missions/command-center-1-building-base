init_code = """
if not "Building" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Building'?")

Building = USER_GLOBAL['Building']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="\n", show_code=None):
    if show_code is None:
        show_code = middle_code + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code,
                          "python-27": init_code + middle_code + return_code},
            "show": {"python-3": show_code,
                     "python-27": show_code},
            "answer": answer}


TESTS = {
    "1. Init": [
        prepare_test(middle_code="Building(1, 1, 2, 2)"),
        prepare_test(middle_code="Building(1, 1, 2, 2, 10)"),
        prepare_test(middle_code="Building(1000, 333 * 3, 2 + 6, 10 / 2, 20 - 5)")
    ],
    "2. Str": [
        prepare_test(test="str(Building(1, 1, 2, 2))",
                     answer="Building(1, 1, 2, 2, 10)", ),
        prepare_test(test="str(Building(0.2, 1, 2, 2, 3))",
                     answer="Building(0.2, 1, 2, 2, 3)", ),
    ],
    "3. Corners": [
        prepare_test(test="Building(1, 1, 2, 2).corners()",
                     answer={"south-west": [1, 1], "north-west": [3, 1], "north-east": [3, 3],
                             "south-east": [1, 3]}),
        prepare_test(test="Building(100, 0, 24, 12, 3).corners()",
                     answer={"north-east": [112, 24], "north-west": [112, 0],
                             "south-west": [100, 0], "south-east": [100, 24]}),
    ],
    "4. Area, Volume": [
        prepare_test(test="Building(1, 1, 2, 2, 100).area()",
                     answer=4),
        prepare_test(test="Building(100, 100, 135, 2000).area()",
                     answer=270000),
        prepare_test(test="Building(1, 1, 2, 2, 100).volume()",
                     answer=400),
        prepare_test(test="Building(100, 100, 135, 2000).volume()",
                     answer=2700000),
    ]

}
