# write your code here
def compare(regex, input_string):
    if not regex:
        return True
    if not input_string:
        return False
    if regex == '.':
        return True
    return regex == input_string


def match_equal_length(regex, input_string):
    if not regex:
        return True
    if regex == '$' and not input_string:
        return True
    if not input_string:
        return False
    if not compare(regex[0], input_string[0]):
        return False
    return match_equal_length(regex[1:], input_string[1:])


def match(regex, input_string):
    if not regex:
        return True
    if regex[0] == '^':
        return match_equal_length(regex[1:], input_string)
    while input_string:
        if match_equal_length(regex, input_string):
            return True
        input_string = input_string[1:]
    return False


def check_regex_all(regex_all, input_string):
    for regex in regex_all:
        if match(regex, input_string):
            return True
    return False


def create_item(regex, index, i):
    return regex[:(index - 1)] + \
           regex[index - 1] * i + regex[(index + 1):]


def create_repetition(regex, index, beg, end):
    repetition = list()
    for i in range(beg, end):
        repetition.append(create_item(regex, index, i))
    return repetition


def check_repetition(regex, input_string):
    if '?' in regex:
        index = str(regex).find('?')
        repetition = create_repetition(regex, index, 0, 2)
        return check_regex_all(repetition, input_string)
    elif '*' in regex:
        index = str(regex).find('*')
        repetition = create_repetition(regex, index, 0, len(input_string))
        return check_regex_all(repetition, input_string)
    elif '+' in regex:
        index = str(regex).find('+')
        repetition = create_repetition(regex, index, 1, len(input_string))
        return check_regex_all(repetition, input_string)
    else:
        return match(regex, input_string)


def run():
    regex, input_string = input().split('|')
    print(check_repetition(regex, input_string))


if __name__ == "__main__":
    run()
