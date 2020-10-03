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


def run():
    regex, input_string = input().split('|')
    print(match(regex, input_string))


if __name__ == "__main__":
    run()
