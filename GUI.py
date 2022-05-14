from GUI_code import *


def main():
    window = Tk()
    window.title('Password Checker')
    window.geometry('250x180')
    widgets = GUI(window)
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()