


class SoftAssert():


    def __init__(self):
        self.__soft_assert_procs = []

    def assertExperession(self, expression: bool, message: str):
        try:
            assert expression
        except AssertionError:
            self.__soft_assert_procs.append("Assertion failed! {}".format(message))

    def assertAll(self):
        assert len(self.__soft_assert_procs) == 0, 'Soft Assert ----- {}'.format(self.__soft_assert_procs)
