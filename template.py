# TAG: incomplete

import helper


def get_input(test):
    with open(helper.get_file_name(test), "r", encoding="utf-8") as f:
        return f.read()


def main():
    test = True
    inputs = get_input(test=test)


if __name__ == "__main__":
    main()
