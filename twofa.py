from tkinter import *
from popup import popup_f
import clipboard
import pyotp
from launch import resource_path
from jsonenc import decryptjson

NSF = (r".\assets\frame0\\")
NHSF = (r".\assets\frame1\\")
NCSF = (r".\assets\frame2\\")
CSF = (r".\assets\frame3\\")
CHSF = (r".\assets\frame4\\")
CCSF = (r".\assets\frame5\\")


def two_fa_f(window, canvas, user, MP, Butto, menu_Button):
    global back_image, passbar_img

    def generate_otp(secret_key):
        totp = pyotp.TOTP(secret_key)
        otp = totp.now()
        return otp

    def eye1(auths, eye, index):
        passw = auths[index]["authkey"]
        otp = generate_otp(passw)
        cont.itemconfig(
            eye, text=trim(otp))

    def eye2(eye):
        cont.itemconfig(eye, text="***********")

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

    def popup(type, index=False):
        reset()
        popup_f(window, canvas, user, MP, type, Butto, menu_Button, index)

    def copyotp(auths, index):
        passw = auths[index]["authkey"]
        otp = (generate_otp(passw))
        clipboard.copy(otp)

    back_image = PhotoImage(
        file=resource_path(("2fa\\2fa.png")))

    canvas.itemconfig(
        canvas.back, image=back_image)
    cont = Canvas(
        canvas,
        bg="#FFFFFF",
        height=350,
        width=610,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    cont.place(x=169, y=160)

    passbar_img = PhotoImage(
        file=resource_path((NSF+"image_8.png")))

    def trim(string):
        if len(string) > 13:
            result_string = string[:13]
            return (result_string+"...")
        else:
            return string
    i = 36
    index = 0
    data = decryptjson(user, MP)
    auths = data.get("authacc")
    if auths:
        for acc in auths:

            passbar = cont.create_image(
                306.0,
                i,
                image=passbar_img
            )

            website = cont.create_text(21, i, text=trim(acc["website"]), fill="#7370F4", font=(
                'Helvetica 10 bold'), anchor="w")
            userl = cont.create_text(221, i, text=trim(acc["username"]), fill="#7370F4", font=(
                'Helvetica 9 bold'), anchor="center")
            passwo = cont.create_text(
                366, i, text="************", fill="#7370F4", font=('Helvetica 9 bold'), anchor="center")
            eye = Butto(cont, 489, i, 9, 1, 1, 7, 7, 7, func=lambda passwo=passwo, index=index: eye1(
                auths, passwo, index), func2=lambda passwo=passwo: eye2(passwo))
            copy = Butto(cont, 530, i, 10, 2,
                         func=lambda index=index: copyotp(auths, index))
            edit = Butto(cont, 575, i, 11, 3,
                         func=lambda index=index: popup("editauth", index))
            cont.configure(scrollregion=cont.bbox("all"))
            i += 55
            index += 1
    canvas.create_text(753, 64, text=index, font=(
        'Helvetica 9 bold'), fill="#A2A0ED", anchor="nw")

    scroll_y = Scrollbar(window, orient=VERTICAL, command=cont.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    window.scroll_y = scroll_y
    cont.configure(yscrollcommand=scroll_y.set)

    def _on_mousewheel(event):
        cont.yview_scroll(int(-1*(event.delta/120)), "units")

    cont.bind_all("<MouseWheel>", _on_mousewheel)

    plus = Butto(canvas, 735, 550, 12, 10, 5, 8, 1,
                 1, func=lambda: popup("auth"))
    canvas.cont = cont
