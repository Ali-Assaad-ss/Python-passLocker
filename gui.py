from tkinter import *
from export.export import export
from passwords import passwords_f
from twofa import two_fa_f
from credit import credit_f
from accset import account_f
from loginint import loginint_f
from launch import resource_path

NSF = (r".\assets\frame0\\")
NHSF = (r".\assets\frame1\\")
NCSF = (r".\assets\frame2\\")
CSF = (r".\assets\frame3\\")
CHSF = (r".\assets\frame4\\")
CCSF = (r".\assets\frame5\\")


def dash(window, user, MP):
    global back_image, Butto, canvas
    window.geometry("800x600")
    _list = window.winfo_children()

    for item in _list:
        item.destroy()

    def reset():
        try:
            window.scroll_y.destroy()
        except:
            pass
        to_keep = [canvas.back]
        for button in menu_Button.buttons:
            to_keep.append(button.tk)

        for child in canvas.winfo_children():
            child.destroy()

        for item in canvas.find_all():
            if item not in to_keep:
                canvas.delete(item)

    def pass_f():
        reset()
        passwords_f(window, canvas, user, MP, Butto, menu_Button)

    def _2fa_f():
        reset()
        two_fa_f(window, canvas, user, MP, Butto, menu_Button)

    def credit():
        reset()
        credit_f(window, canvas, user, MP, Butto, menu_Button)

    def backup_f():
        canvas.itemconfig(
            canvas.back, image=back_image)
        reset()
        if export(user):
            invalid_log = canvas.create_text(
                450.0,
                500.0,
                anchor="center",
                text="Backup successfull",
                fill="#7370F4",
                font=("ZenKakuGothicAntique Regular", 30 * -1))
        else:
            invalid_log = canvas.create_text(
                450.0,
                500.0,
                anchor="center",
                text="Backup failed",
                fill="#7370F4",
                font=("ZenKakuGothicAntique Regular", 30 * -1))

    def account():
        reset()
        account_f(window, canvas, user, Butto)

    def logout_f():
        window.geometry("800x565")
        _list = window.winfo_children()
        for item in _list:
            item.destroy()
        loginint_f(window)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    back_image = PhotoImage(
        file=resource_path((NSF+"image_1.png")))

    canvas.back = canvas.create_image(
        400.0,
        300.0,
        image=back_image
    )

    class Butto:
        def __init__(self, canvas, x, y, I, IH, IC=False, CI=False, CIH=False, CIC=False, func=False, func2=False):

            self.func = func
            self.func2 = func2
            if I:
                self.I = PhotoImage(file=resource_path((NSF+f"image_{I}.png")))
            if IH:
                self.IH = PhotoImage(
                    file=resource_path((NHSF+f"image_{IH}.png")))
            if IC:
                self.IC = PhotoImage(
                    file=resource_path((NCSF+f"image_{IC}.png")))
            if CI:
                self.CI = PhotoImage(
                    file=resource_path((CSF+f"image_{CI}.png")))
            if CIH:
                self.CIH = PhotoImage(
                    file=resource_path((CHSF+f"image_{CIH}.png")))
            if CIC:
                self.CIC = PhotoImage(
                    file=resource_path((CCSF+f"image_{CIC}.png")))
            self.canvas = canvas

            self.tk = self.canvas.create_image(
                x,
                y,
                image=self.I,
                activeimage=self.IH)
            self.clicked = False
            self.canvas.tag_bind(self.tk, "<ButtonRelease-1>",
                                 lambda x: self.on_release())

        def on_release(self):
            if self.clicked:
                if self.func2:
                    self.func2()

                try:
                    self.canvas.itemconfig(
                        self.tk, image=self.I, activeimage=self.IH)
                except:
                    self.canvas.itemconfig(
                        self.tk, image=self.I, activeimage=self.IH)
                self.clicked = False
            else:
                if self.func:
                    self.func()
                self.clicked = True
                try:
                    self.canvas.itemconfig(
                        self.tk, image=self.CI, activeimage=self.CIH)
                except:
                    self.canvas.itemconfig(
                        self.tk, image=self.I, activeimage=self.IH)

    class menu_Button:
        buttons = []

        def __init__(self, x, y, I, IH, IC=False, CI=False, func=False):
            menu_Button.buttons.append(self)
            self.func = func

            if I:
                self.I = PhotoImage(file=resource_path((NSF+f"image_{I}.png")))
            if IH:
                self.IH = PhotoImage(
                    file=resource_path((NHSF+f"image_{IH}.png")))
            if IC:
                self.IC = PhotoImage(
                    file=resource_path((NCSF+f"image_{IC}.png")))
            if CI:
                self.CI = PhotoImage(
                    file=resource_path((CSF+f"image_{CI}.png")))
            self.tk = canvas.create_image(
                x,
                y,
                image=self.I,
                activeimage=self.IH)
            self.clicked = False
            canvas.tag_bind(self.tk, "<Button-1>", lambda x: self.on_hold())
            canvas.tag_bind(self.tk, "<ButtonRelease-1>",
                            lambda x: self.on_release())

        def on_hold(self):
            if not self.clicked:
                try:
                    canvas.itemconfig(self.tk, image=self.IC,
                                      activeimage=self.IC)
                except:
                    canvas.itemconfig(self.tk, image=self.I,
                                      activeimage=self.IH)

        def on_release(self):
            try:

                canvas.itemconfig(pass_.tk, image=pass_.I,
                                  activeimage=pass_.IH)
                canvas.itemconfig(_2fa.tk, image=_2fa.I, activeimage=_2fa.IH)
                canvas.itemconfig(credit_card.tk, image=credit_card.I,
                                  activeimage=credit_card.IH)
                canvas.itemconfig(backup.tk, image=backup.I,
                                  activeimage=backup.IH)
                canvas.itemconfig(profile.tk, image=profile.I,
                                  activeimage=profile.IH)
                if self.clicked:
                    canvas.itemconfig(self.tk, image=self.CI,
                                      activeimage=self.CI)
            except:
                pass

            if not self.clicked:

                if self.func:
                    self.func()
                for button in menu_Button.buttons:
                    button.clicked = False
                self.clicked = True

                try:
                    canvas.itemconfig(self.tk, image=self.CI,
                                      activeimage=self.CI)
                except:
                    canvas.itemconfig(self.tk, image=self.I,
                                      activeimage=self.IH)

    pass_ = menu_Button(69, 156, 2, 4, 6, 1, func=pass_f)
    _2fa = menu_Button(69, 220, 3, 5, 7, 2, func=_2fa_f)
    credit_card = menu_Button(69, 285, 4, 6, 8, 3, func=credit)
    backup = menu_Button(69, 349, 5, 7, 9, 4, func=backup_f)
    profile = menu_Button(69, 413, 6, 8, 10, 5, func=account)
    logout = menu_Button(75, 550, 7, 9, 4, 6, func=logout_f)

    pass_.on_release()


if __name__ == '__main__':
    window = Tk()
    window.geometry("800x600")
    window.resizable(False, False)
    window.mainloop()
