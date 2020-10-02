# write your code here
def compare(regex, input_string):
    if not regex and not input_string:
        return True
    if not input_string:
        return False
    if not regex:
        return True
    if regex == '.':
        return True
    return regex == input_string


def match(regex, input_string):
    if not regex:
        return True
    if not input_string:
        return False
    if not compare(regex[0], input_string[0]):
        return False
    return match(regex[1:], input_string[1:])


def run():
    regex, input_string = input().split('|')
    print(match(regex, input_string))


if __name__ == "__main__":
    run()
