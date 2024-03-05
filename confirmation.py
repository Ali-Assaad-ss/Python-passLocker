from tkinter import *
from launch import resource_path
from jsonenc import encryptjson, decryptjson


def conf_popup_f(window, canvas, user, MP, type, Butto, menu_Button, index):
    global image_image_1, image_image_2, image_image_3, image_image_5, image_image_6

    def yes():
        data = decryptjson(user, MP)

        del data["creditcard"][index]
        encryptjson(data, user, MP)
        reset()

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
        from credit import credit_f
        credit_f(window, canvas, user, MP, Butto, menu_Button)

    conf = Canvas(
        canvas,
        bg="#FFFFFF",
        height=534,
        width=465,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    conf.place(x=246.5, y=30)

    image_image_1 = PhotoImage(
        file=resource_path(("confirmation/credit.png")))
    image_1 = conf.create_image(
        235.5,
        220.0,
        image=image_image_1
    )

    image_image_3 = PhotoImage(
        file=resource_path(("confirmation/image_3.png")))

    image_image_2 = PhotoImage(
        file=resource_path(("confirmation/image_2.png")))
    image_2 = conf.create_image(
        330.0,
        250.0,
        image=image_image_2,
        activeimage=image_image_3
    )

    image_image_6 = PhotoImage(
        file=resource_path(("confirmation/image_6.png")))
    image_image_5 = PhotoImage(
        file=resource_path(("confirmation/image_5.png")))
    image_5 = conf.create_image(
        130.0,
        250.0,
        image=image_image_5,
        activeimage=image_image_6
    )
    conf.tag_bind(image_5, "<Button-1>", lambda x: conf.destroy())
    conf.tag_bind(image_2, "<Button-1>", lambda x: yes())


def conf_popup_fs(window, canvas, user, MP, type, Butto, menu_Button, index):
    global image_image_1, image_image_2, image_image_3, image_image_5, image_image_6

    def yes():
        data = decryptjson(user, MP)

        if type == "editauth":
            del data["authacc"][index]
        if type == "editpass":
            del data["accounts"][index]

        encryptjson(data, user, MP)
        reset()

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
        if type == "editauth":
            from twofa import two_fa_f
            two_fa_f(window, canvas, user, MP, Butto, menu_Button)
        if type == "editpass":
            from passwords import passwords_f
            passwords_f(window, canvas, user, MP, Butto, menu_Button)

    conf = Canvas(
        canvas,
        bg="#FFFFFF",
        height=330,
        width=460,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    conf.place(x=248, y=133)

    image_image_1 = PhotoImage(
        file=resource_path(("confirmation/pass.png")))
    image_1 = conf.create_image(
        235.5,
        170.0,
        image=image_image_1
    )

    image_image_3 = PhotoImage(
        file=resource_path(("confirmation/image_3.png")))

    image_image_2 = PhotoImage(
        file=resource_path(("confirmation/image_2.png")))
    image_2 = conf.create_image(
        330.0,
        210.0,
        image=image_image_2,
        activeimage=image_image_3
    )

    image_image_6 = PhotoImage(
        file=resource_path(("confirmation/image_6.png")))
    image_image_5 = PhotoImage(
        file=resource_path(("confirmation/image_5.png")))
    image_5 = conf.create_image(
        130.0,
        210.0,
        image=image_image_5,
        activeimage=image_image_6
    )
    conf.tag_bind(image_5, "<Button-1>",
                  lambda x: conf.destroy())

    conf.tag_bind(image_2, "<Button-1>",
                  lambda x: yes())
