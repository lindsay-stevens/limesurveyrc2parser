# -*- coding: utf-8 -*-
from urllib.request import urlopen
import limesurveyrc2parser as pkg
import argparse


def download():
    print("Download the PHP source for the remote control API.")
    url = "https://raw.githubusercontent.com/LimeSurvey/LimeSurvey/master/" \
          "application/helpers/remotecontrol/remotecontrol_handle.php"
    print("Download from %s" % url)
    with urlopen(url) as response, open('lsrc2source.php', mode='w') as f:
        print("Save as lsrc2source.php")
        f.write(response.read().decode("utf-8"))
        print("Done")


def generate_python_code():
    print("Generate Python client code")
    print("Read lsrc2source.php from current directory")
    with open('lsrc2source.php') as f:
        php_source = f.read()
    print("Parse lsrc2source.php")
    parse_result = pkg.LimeSurveyRc2PhpSourceParser.parse(php_source)
    print("  - contains %d function definitions." % len(parse_result))
    print("Generating Python code and writing it to lsrc2client.py")
    py_source = pkg.LimeSurveyRc2PythonSourceGenerator.generate(parse_result)
    with open('lsrc2client.py', mode='w') as f:
        f.write(py_source)
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""LimeSurvey RC2 API Client Generator""")
    parser.add_argument("--download", action="store_true", default=False)
    parser.add_argument("--generate", action="store_true", default=False)
    args = parser.parse_args()
    if args.download:
        download()
    if args.generate:
        generate_python_code()
    if not args.download and not args.generate:
        print("\nChoose a mode: '--download' and/or '--generate'."
              " Or just '--help'.\n")
