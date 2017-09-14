# import the appJar library
import os


def main():
    print(os.path.dirname(__file__))
   # choose = input("choose email file to parse: ")
    parse_email("/Users/benstruhl/downloads/example1")

def parse_email(email):
    file = open(email, 'rb')
    muffled_up_string = str(file.read())
    reformed_string = muffled_up_string.replace("\\xc9", "")
    print(reformed_string)

if __name__ == "__main__":
    main()
