from tkinter import *
from confirmation import conf_popup_f
from launch import resource_path
from jsonenc import encryptjson, decryptjson


def is_valid_credit_card(card_number, cvc):
    # Remove any spaces or non-digit characters from card number
    card_number = ''.join(filter(str.isdigit, card_number))

    # Check if the card number has a valid length
    if len(card_number) != 16:
        return False

    # Perform Luhn algorithm checksum
    digits = list(map(int, card_number))
    for i in range(14, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    checksum = sum(digits) % 10
    if checksum != 0:
        return False

    # Check if the CVC is a 3-digit number
    if not cvc.isdigit() or len(cvc) != 3:
        return False

    return True


def popup_f(window, canvas, user, MP, type, Butto, menu_Button, index):
    global entry_1, entry_2, entry_3, entry_4, entry_5, entry_6
    global blur, saveeditb, saveeditbh, saveeditbc, pop, trashb, trashbh, trashbc, popback
    data = decryptjson(user, MP)

    def savepass():
        global invalid_log
        name = entry_1.get()
        number = entry_2.get()
        date = entry_3.get()
        cvc = entry_4.get()
        owner = entry_5.get()
        location = entry_6.get()

        if name != "" and date != "" and is_valid_credit_card(number, cvc):

            enties = {"name": name, "number": number, "date": date,
                      "cvc": cvc, "owner": owner, "location": location}
            if type == "add":
                try:
                    data["creditcard"].append(enties)
                except:
                    data["creditcard"] = []
                    data["creditcard"].append(enties)

            if type == "edit":
                data["creditcard"][index] = enties
            encryptjson(data, user, MP)
            reset()
        elif is_valid_credit_card(number, cvc):
            try:
                canvas.delete(invalid_log)
            except:
                pass
            invalid_log = canvas.create_text(
                490.0,
                42.0,
                anchor="center",
                text="Enter name and expiry date",
                fill="#6B68DE",
                font=("ZenKakuGothicAntique Regular", 20 * -1))
            canvas.after(3000, lambda: canvas.delete(invalid_log))
        else:
            try:
                canvas.delete(invalid_log)
            except:
                pass
            invalid_log = canvas.create_text(
                480.0,
                42.0,
                anchor="center",
                text="Invalid card",
                fill="#6B68DE",
                font=("ZenKakuGothicAntique Regular", 20 * -1))
            canvas.after(3000, lambda: canvas.delete(invalid_log))

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
        y=85.0,
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
        y=160.0,
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
        y=235.0,
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
        x=321.0,
        y=307.0,
        width=315.0,
        height=37.0
    )

    entry_5 = Entry(
        canvas,
        bd=0,
        bg="#EBEBEB",
        fg="#424242",
        highlightthickness=0,
        font=("ZenKakuGothicAntique Regular", 16 * -1)
    )
    entry_5.place(
        x=321.0,
        y=382.0,
        width=315.0,
        height=37.0
    )

    entry_6 = Entry(
        canvas,
        bd=0,
        bg="#EBEBEB",
        fg="#424242",
        highlightthickness=0,
        font=("ZenKakuGothicAntique Regular", 16 * -1)
    )
    entry_6.place(
        x=321.0,
        y=456.0,
        width=315.0,
        height=37.0
    )
    blur = PhotoImage(file=resource_path("cardpopup/image_0.png"))
    back = canvas.create_image(
        480,
        300,
        image=blur)
    if type == "edit":
        popback = PhotoImage(file=resource_path("cardpopup/editcard.png"))
        card = data["creditcard"][index]
        name = card.get("name")
        number = card.get("number")
        date = card.get("date")
        cvc = card.get("cvc")
        owner = card.get("owner")
        location = card.get("location")
        entry_1.insert(0, name)
        entry_2.insert(0, number)
        entry_3.insert(0, date)
        entry_4.insert(0, cvc)
        try:
            entry_5.insert(0, owner)
        except:
            pass
        try:
            entry_6.insert(0, location)
        except:
            pass

    if type == "add":
        popback = PhotoImage(file=resource_path("cardpopup/newcard.png"))
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

    savedit = canvas.create_image(
        481,
        540,
        image=saveeditb,
        activeimage=saveeditbh)

    def on_hold(image_id, c):
        canvas.itemconfig(image_id, image=c,
                          activeimage=c)

    def on_release(image_id, window, user, b, h):

        canvas.itemconfig(image_id, image=b,
                          activeimage=h)
        if image_id == savedit:
            savepass()

        if image_id == trash:
            conf_popup_f(window, canvas, user, MP, type,
                         Butto, menu_Button, index)

    if type == "edit":
        trash = canvas.create_image(
            680,
            45,
            image=trashb,
            activeimage=trashbh)
        canvas.tag_bind(trash, "<Button-1>", lambda x: on_hold(trash, trashbc))
        canvas.tag_bind(trash, "<ButtonRelease-1>",
                        lambda x: on_release(trash, window, user, trashb, trashbh))

    canvas.tag_bind(savedit, "<Button-1>",
                    lambda x: on_hold(savedit, saveeditbc))
    canvas.tag_bind(savedit, "<ButtonRelease-1>",
                    lambda x: on_release(savedit, window, user, saveeditb, saveeditbh))

    canvas.tag_bind(back, "<Button-1>", lambda x: reset())
