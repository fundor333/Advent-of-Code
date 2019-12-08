import unittest


def check_checker(value_in) -> bool:
    if len(value_in) != 6:
        return False
    last_one = int(value_in[0])
    duble = False
    for element in value_in[1:]:
        i = int(element)
        if last_one > i:
            return False
        elif i == last_one:
            duble = True
        elif i > last_one:
            last_one = i
    return duble


def check_checker_2(value_in) -> bool:
    flag = check_checker(value_in)
    if flag:
        for cifer in value_in:
            if value_in.count(cifer) == 2:
                return True
    return False


def generate_array_range(start_in, end_in):
    started = int(start_in)
    ended = int(end_in)
    array = []
    for e in range(started, ended + 1):
        array.append(f"{e:06}")
    return array


if __name__ == "__main__":
    start_in = "146810"
    end_in = "612564"
    array = generate_array_range(start_in, end_in)
    counter = 0
    for e in array:
        if check_checker(e):
            counter += 1
    print(counter)
    counter = 0
    for e in array:
        if check_checker_2(e):
            counter += 1
    print(counter)


class Day03TestCase(unittest.TestCase):
    def test_check_checker(self):
        self.assertEqual(check_checker("111111"), True)
        self.assertEqual(check_checker("223450"), False)
        self.assertEqual(check_checker("123789"), False)

    def test_check_checker_2(self):
        self.assertEqual(check_checker_2("112233"), True)
        self.assertEqual(check_checker_2("123444"), False)
        self.assertEqual(check_checker_2("111122"), True)
