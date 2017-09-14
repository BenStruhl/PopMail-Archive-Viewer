from appJar import gui
import os


def main():
    app = gui()
    app.addLabel("title", "Welecome to appJar")
    app.setLabelBg("title", "red")


if __name__ = "__main__":
    main()
