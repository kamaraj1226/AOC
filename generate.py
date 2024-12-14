import os
import sys
import argparse
import requests
from bs4 import BeautifulSoup


def get_heading(day, year):

    url = "https://adventofcode.com/{year}/day/{day}"

    r = requests.get(url.format(year=year, day=day))
    soup = BeautifulSoup(r.content, "html.parser")
    heading = soup.find("article").find("h2").get_text()

    heading = heading.split("---")[1].split(":")[-1].strip()
    return heading


def generate_file_name(day, year, heading: str):
    month = "12"
    day = "0" + day if len(day) == 1 else day

    base_file_name = day + month + year + "_" + "_".join(heading.split())
    python_name = base_file_name + ".py"
    txt_name = base_file_name + ".txt"
    test_txt_name = base_file_name + "_test.txt"

    return python_name, txt_name, test_txt_name


def create_files(py_name, txt_name, test_txt_name):
    base_dir = os.path.dirname(sys.argv[0])

    # incase if generate.py is not run with absolute path.
    # base_dir value will be empty
    base_dir = "." if not base_dir else base_dir
    data_path = "/datas/"
    with open(base_dir + "/src/" + py_name, "w") as f:

        with open(base_dir + "/template.py") as template_file:
            f.write(template_file.read())

    with open(base_dir + data_path + txt_name, "w"):
        ...

    with open(base_dir + data_path + test_txt_name, "w"):
        ...


def main(args):

    day = args.day
    year = args.year
    heading = get_heading(day, year)
    py_name, txt_name, test_txt_name = generate_file_name(day, year, heading)
    create_files(py_name, txt_name, test_txt_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="generate.py", description="Generate required files"
    )
    parser.add_argument(
        "-y",
        "--year",
        required=False,
        type=str,
        help="Type the AOC year.",
        default="2024",
    )
    parser.add_argument(
        "-d", "--day", required=True, type=str, help="Type the AOC day."
    )
    args = parser.parse_args()
    main(args)
