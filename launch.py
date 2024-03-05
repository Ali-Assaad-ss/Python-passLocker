from tkinter import *
import sys
import os
import pygetwindow as gw


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # In development, use the original directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    app_window = gw.getWindowsWithTitle(
        "PASS LOCKER")  # Replace with your app title
    if app_window:
        app_window = app_window[0]
        app_window.activate()
    else:

        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
        from loginint import loginint_f
        window = Tk()

        window.geometry("800x565")
        window.configure(bg="#FFFFFF")
        window.title("PASS LOCKER")
        loginint_f(window)

        window.call('wm', 'iconphoto', window._w, PhotoImage(
            file=resource_path("app.png")))
        window.iconbitmap(resource_path("app.ico"))
        window.resizable(False, False)
        window.mainloop()


if __name__ == "__main__":
    main()