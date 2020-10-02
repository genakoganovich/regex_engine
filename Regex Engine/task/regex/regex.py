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


def run():
    regex, input_string = input().split('|')
    print(compare(regex, input_string))


if __name__ == "__main__":
    run()
