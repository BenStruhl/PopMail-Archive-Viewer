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
    get_destination(reformed_string)

def get_destination(email):
    email_without_date = str(email.split("To: "))

    print(email_without_date)

if __name__ == "__main__":
    main()
