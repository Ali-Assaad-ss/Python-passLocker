from tkinter import *
from cardpop import popup_f
import clipboard
from launch import resource_path
from jsonenc import decryptjson


def trim(string):
    if len(string) > 7:
        result_string = string[:7]
        return (result_string+"...")
    else:
        return string


def credit_f(window, canvas, user, MP, Butto, menu_Button):

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

    global back_image, visa, visah, master, masterh

    back_image = PhotoImage(
        file=resource_path(("credit\\credit.png")))

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

    visa = PhotoImage(
        file=resource_path(("credit/visa.png")))

    master = PhotoImage(
        file=resource_path(("credit/master.png")))

    visah = PhotoImage(
        file=resource_path(("credit/visah.png")))

    masterh = PhotoImage(
        file=resource_path(("credit/masterh.png")))

    i = 100
    index = 0
    data = decryptjson(user, MP)
    cards = data.get("creditcard")
    cont.create_rectangle(0, 0, 10, 10, fill="#FFFFFF", outline="")
    if cards:
        for cc in cards:
            if index % 2 == 0:
                x = 152.5
            else:
                x = 457.5
            ccinfo = (cards[index])
            numbertext = ccinfo.get("number")
            creditcard = cont.create_image(
                x,
                i,
                image=master if numbertext.startswith("5") else visa,
                activeimage=masterh if numbertext.startswith("5") else visah)

            cont.tag_bind(creditcard, "<Button-1>", lambda x,
                          index=index: popup("edit", index))

            number = cont.create_text(
                x-100, i+30, text="**** **** **** **** "+numbertext[-4:i], fill="#FFFFFF", font=("OCR-A", 12), anchor="w")
            name = cont.create_text(
                x-100, i-50, text=trim(ccinfo["name"]), fill="#FFFFFF", font=("OCR-A", 12), anchor="nw")
            date = cont.create_text(
                x+25, i+55, text=trim(ccinfo["date"]), fill="#FFFFFF", font=("OCR-A", 11), anchor="center")
            cvc = cont.create_text(
                x+75, i, text="cvc: "+ccinfo["cvc"], fill="#FFFFFF", font=("OCR-A", 11), anchor="center")
            cont.tag_bind(number, "<Button-1>", lambda x,
                          numbertext=numbertext: clipboard.copy(numbertext))
            cont.tag_bind(date, "<Button-1>", lambda x,
                          date_=ccinfo["date"]: clipboard.copy(date_))
            cont.tag_bind(cvc, "<Button-1>", lambda x,
                          cvc_=ccinfo["cvc"]: clipboard.copy(cvc_))
            cont.configure(scrollregion=cont.bbox("all"))
            if index % 2 == 1:
                i += 170
            index += 1
    canvas.create_text(753, 64, text=index, font=(
        'Helvetica 9 bold'), fill="#A2A0ED", anchor="nw")

    scroll_y = Scrollbar(window, orient=VERTICAL, command=cont.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    window.scroll_y = scroll_y
    cont.configure(yscrollcommand=scroll_y.set)

    def _on_mousewheel(event):
        try:
            cont.yview_scroll(int(-1*(event.delta/120)), "units")
        except:
            pass

    cont.bind_all("<MouseWheel>", _on_mousewheel)

    plus = Butto(canvas, 735, 550, 12, 10, 5, 8,
                 1, 1, func=lambda: popup("add"))
    canvas.cont = cont
