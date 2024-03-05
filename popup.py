from tkinter import *
from jsonenc import encryptjson
from confirmation import conf_popup_fs
from add_password import addtojson
import pyotp
from launch import resource_path
import random
import string
import clipboard
from jsonenc import decryptjson


def popup_f(window, canvas, user, MP, type, Butto, menu_Button, index, searchaccs=False):
    global entry_1, entry_2, entry_3
    global blur, saveeditb, saveeditbh, saveeditbc, pop, trashb, trashbh, trashbc, popback, dicehi, dicei

    def dice():
        characters = string.ascii_letters + string.digits + "!@#$%&*"
        password = ''.join(random.choice(characters) for _ in range(16))
        entry_3.delete(0, "end")
        entry_3.insert(0, password)
        clipboard.copy(password)

    def generate_otp(secret_key):
        totp = pyotp.TOTP(secret_key)
        otp = totp.now()
        return otp

    def savepass(index=False):
        global invalid_log
        website = entry_1.get()
        User = entry_2.get()
        password = entry_3.get()
        if website != "" and User != "" and password != "":
            if type == "editpass" or type == "pass":
                note = text_widget.get("1.0", "end-1c")
                if type == "editpass":
                    del data["accounts"][index]
                encryptjson(data, user, MP)
                addtojson("pass", user, MP, website, User, password, note)
                reset()
            if type == "editauth" or type == "auth":
                try:
                    password = password.replace(" ", "")
                    generate_otp(password)
                    if type == "editauth":
                        del data["authacc"][index]
                    encryptjson(data, user, MP)
                    addtojson("auth", user, MP, website, User, password)
                    reset()
                except:
                    try:
                        canvas.delete(invalid_log)
                    except:
                        pass
                    invalid_log = canvas.create_text(
                        480.0,
                        500.0,
                        anchor="center",
                        text="Invalid secret code",
                        fill="#c93e3e",
                        font=("ZenKakuGothicAntique Regular", 20 * -1))
                    canvas.after(3000, lambda: canvas.delete(invalid_log))

        else:
            print("invalid")
            return False

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
        if type == "auth" or type == "editauth":
            from twofa import two_fa_f
            two_fa_f(window, canvas, user, MP, Butto, menu_Button)
        if type == "pass" or type == "editpass":
            from passwords import passwords_f
            passwords_f(window, canvas, user, MP, Butto, menu_Button)

    data = decryptjson(user, MP)
    if type == "auth" or type == "editauth":
        entry_1 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_1.place(
            x=321.0,
            y=195.0,
            width=315.0,
            height=37.0
        )

        entry_2 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_2.place(
            x=321.0,
            y=270.0,
            width=315.0,
            height=37.0
        )

        entry_3 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_3.place(
            x=321.0,
            y=344.0,
            width=315.0,
            height=37.0
        )

    if type == "pass" or type == "editpass":
        entry_1 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_1.place(
            x=322.0,
            y=99.0,
            width=315.0,
            height=37.0
        )

        entry_2 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_2.place(
            x=322.0,
            y=173.0,
            width=315.0,
            height=37.0
        )

        entry_3 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_3.place(
            x=322.0,
            y=247.0,
            width=315.0,
            height=37.0
        )
        entry_4 = Entry(
            canvas,
            bd=0,
            bg="#EBEBEB",
            fg="#424242",
            highlightthickness=0,
            font=("ZenKakuGothicAntique Regular", 16 * -1)
        )
        entry_4.place(
            x=322.0,
            y=320.0,
            width=315.0,
            height=160.0
        )
        text_widget = Text(entry_4, wrap=WORD, height=20,
                           width=60, bg="#EBEBEB", borderwidth=0, highlightthickness=0, font=("ZenKakuGothicAntique Regular", 15 * -1), fg="#424242")
        text_widget.pack()

    blur = PhotoImage(file=resource_path("popup/image_0.png"))
    back = canvas.create_image(
        480,
        300,
        image=blur)

    if type == "pass":
        popback = PhotoImage(file=resource_path("popup/PASS2.png"))
    if type == "auth":
        popback = PhotoImage(file=resource_path("popup/otp.png"))
    if type == "editpass":
        popback = PhotoImage(file=resource_path("popup\image_1p2.png"))
    if type == "editauth":
        popback = PhotoImage(file=resource_path("popup\image_1a.png"))
    pop = canvas.create_image(
        480,
        300,
        image=popback)

    saveeditb = PhotoImage(file=resource_path("popup/image_2.png"))
    saveeditbh = PhotoImage(file=resource_path("popup/image_7.png"))
    saveeditbc = PhotoImage(file=resource_path("popup/image_8.png"))

    trashb = PhotoImage(file=resource_path("popup/image_4.png"))
    trashbh = PhotoImage(file=resource_path("popup/image_6.png"))
    trashbc = PhotoImage(file=resource_path("popup/image_5.png"))
    if type == "auth" or type == "editauth":
        savedit = canvas.create_image(
            481,
            426,
            image=saveeditb,
            activeimage=saveeditbh)
    else:
        savedit = canvas.create_image(
            481,
            530,
            image=saveeditb,
            activeimage=saveeditbh)

    def on_hold(image_id, c):
        canvas.itemconfig(image_id, image=c,
                          activeimage=c)

    def on_release(image_id, window, user, b, h):

        canvas.itemconfig(image_id, image=b,
                          activeimage=h)
        if image_id == savedit:
            savepass(index)
        if image_id == trash:
            conf_popup_fs(window, canvas, user, MP, type,
                          Butto, menu_Button, index)
    if type == "pass" or type == "editpass":
        dicei = PhotoImage(file=resource_path("popup/dice.png"))
        dicehi = PhotoImage(file=resource_path("popup/diceh.png"))
        diceb = canvas.create_image(
            665,
            265,
            image=dicei,
            activeimage=dicehi)
        canvas.tag_bind(diceb, "<Button-1>",
                        lambda x: dice())

    if type == "editauth":
        trash = canvas.create_image(
            680,
            150,
            image=trashb,
            activeimage=trashbh)
        canvas.tag_bind(trash, "<Button-1>", lambda x: on_hold(trash, trashbc))
        canvas.tag_bind(trash, "<ButtonRelease-1>",
                        lambda x: on_release(trash, window, user, trashb, trashbh))

    if type == "editpass":
        trash = canvas.create_image(
            680,
            65,
            image=trashb,
            activeimage=trashbh)
        canvas.tag_bind(trash, "<Button-1>", lambda x: on_hold(trash, trashbc))
        canvas.tag_bind(trash, "<ButtonRelease-1>",
                        lambda x: on_release(trash, window, user, trashb, trashbh))

    if type == "editpass":
        if searchaccs:
            accs = searchaccs
        else:
            accs = data.get("accounts")

        passw = accs[index]["password"]
        entry_1.insert(0, accs[index]["website"])
        entry_2.insert(0, accs[index]["username"])
        entry_3.insert(0, passw)
        text_widget.insert("insert", accs[index]["note"])

    if type == "editauth":
        accs = data.get("authacc")
        passw = accs[index]["authkey"]
        entry_1.insert(0, accs[index]["website"])
        entry_2.insert(0, accs[index]["username"])
        entry_3.insert(0, passw)

    canvas.tag_bind(savedit, "<Button-1>",
                    lambda x: on_hold(savedit, saveeditbc))
    canvas.tag_bind(savedit, "<ButtonRelease-1>",
                    lambda x: on_release(savedit, window, user, saveeditb, saveeditbh))

    canvas.tag_bind(back, "<Button-1>", lambda x: reset())
