import argparse
import os
import sys

import pypandoc
from html.parser import HTMLParser
import time


# convert docx/pdf to html


def convert_to_html(filename):
    output = pypandoc.convert_file(filename, "html")


    # write the output
    filename, ext = os.path.splitext(filename)
    filename = "{0}.html".format(filename)
    with open(filename, "w") as f:
        # Python 2 "fix". If this isn't a string, encode it.
        if type(output) is not str:
            output = output.encode("utf-8")
        f.write(output)
        # Implement HTMLParser

        # save console output to file
        sys.stdout = open("results.txt", "w")
        # provide content to html parser
        html_parser = MyHTMLParser()
        html_parser.feed(output)
        # close file
        sys.stdout.close()

        print("Done! Output written to: {}\n".format(filename))


# parse generated html into useable format
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):

        # Ordered List Handling
        if tag == "ol":
            print("Ordered List found")
            print("Start tag:", tag)
            for attr in attrs:
                print("     attr:", attr)

        # Unordered List handling
        if tag == "ul":
            print("Unorganised List found")
            print("Start tag: ", tag)
            for attr in attrs:
                print("     attr:", attr)

        # List Item Handling
        if tag == "li":
            print("Start tag: ", tag)

            # Link Handling

        if tag == "h2":
            print("h2 found")
            print("Start tag: ", tag)
            for attr in attrs:
                print("     attr:", attr)

        if tag == "h3":
            print("h3 found")
            print("Start tag: ", tag)
            for attr in attrs:
                print("     attr:", attr)

        if tag == "h4":
            print("h4 found")
            print("Start tag: ", tag)
            for attr in attrs:
                print("     attr:", attr)

        if tag == "strong":
            print(tag)
        if tag == "b":
            print(tag)
        if tag == "em":
            print(tag)
        if tag == "i":
            print(tag)
        if tag == "u":
            print(tag)

    def handle_data(self, data):
        print("Content: ", data)

    def handle_endtag(self, tag):
        pass


# output results
if __name__ == "__main__":
    t0 = time.perf_counter()
    parser = argparse.ArgumentParser(
        description="Convert a Word document to an HTML document."
    )
    parser.add_argument("path", type=str, help="Path to your word document")
    args = parser.parse_args()
    convert_to_html(args.path)
    t1 = time.perf_counter()
    print(f"Generated in {t1 - t0:0.4f} seconds")

