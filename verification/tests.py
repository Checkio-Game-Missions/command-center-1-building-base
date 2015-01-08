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
        prepare_test(middle_code="Building(0.54345, 1.12313, 2./6, 3.3 * 5, 1./2)")
    ],
    "2. Str": [
        prepare_test(test="str(Building(1, 1, 2, 2))",
                     answer="Building(1, 1, 2, 2, 10)", ),
        prepare_test(test="str(Building(0.2, 1, 2, 2.2, 3.5))",
                     answer="Building(0.2, 1, 2, 2.2, 3.5)", ),
    ],
    "3. Corners": [
        prepare_test(test="Building(1, 1, 2, 2).corners()",
                     answer={"south-west": [1, 1], "north-west": [3, 1], "north-east": [3, 3],
                             "south-east": [1, 3]}),
        prepare_test(test="Building(100.5, 0.5, 24.3, 12.2, 3).corners()",
                     answer={"north-east": [112.7, 24.8], "north-west": [112.7, 0.5],
                             "south-west": [100.5, 0.5], "south-east": [100.5, 24.8]}),
    ],
    "4. Area, Volume": [
        prepare_test(test="Building(1, 1, 2, 2, 100).area()",
                     answer=4),
        prepare_test(test="Building(100, 100, 135.5, 2000.1).area()",
                     answer=271013.55),
        prepare_test(test="Building(1, 1, 2, 2, 100).volume()",
                     answer=400),
        prepare_test(test="Building(100, 100, 135.5, 2000.1).volume()",
                     answer=2710135.5),
    ]

}
