from tkinter import *
import changepassword as cp
from launch import resource_path


def change_pass(window, canvas, user):

    global invalid_log
    MP = entry_2.get()
    NMP = entry_3.get()
    if NMP != "":
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        if cp.change_MP(user, MP, NMP):
            window.destroy()
            from launch import main
            main()
        else:
            invalid_log = canvas.create_text(
                480.0,
                60.0,
                anchor="center",
                text="wrong Password",
                fill="#6B68DE",
                font=("ZenKakuGothicAntique Regular", 25 * -1))
            canvas.after(3000, lambda: canvas.delete(invalid_log))

    else:
        print("enter pass")
        try:
            canvas.delete(invalid_log)
        except:
            pass
        invalid_log = canvas.create_text(
            480.0,
            60.0,
            anchor="center",
            text="Enter a Password",
            fill="#6B68DE",
            font=("ZenKakuGothicAntique Regular", 25 * -1))
        canvas.after(3000, lambda: canvas.delete(invalid_log))


def change_user(window, canvas, old_user):
    global invalid_log
    new_user = entry_1.get()
    if new_user != "" and new_user != old_user:
        if cp.change_user(old_user, new_user):
            window.destroy()
            from launch import main
            main()
        else:
            try:
                canvas.delete(invalid_log)
            except:
                pass
            invalid_log = canvas.create_text(
                480.0,
                60.0,
                anchor="center",
                text="Username taken",
                fill="#6B68DE",
                font=("ZenKakuGothicAntique Regular", 25 * -1))
            canvas.after(3000, lambda: canvas.delete(invalid_log))

    elif new_user == old_user:
        try:
            canvas.delete(invalid_log)
        except:
            pass
        invalid_log = canvas.create_text(
            480.0,
            60.0,
            anchor="center",
            text="Enter a new username",
            fill="#6B68DE",
            font=("ZenKakuGothicAntique Regular", 25 * -1))
        canvas.after(3000, lambda: canvas.delete(invalid_log))

    else:
        try:
            canvas.delete(invalid_log)
        except:
            pass
        print("enter user")
        invalid_log = canvas.create_text(
            480.0,
            60.0,
            anchor="center",
            text="Enter a username",
            fill="#6B68DE",
            font=("ZenKakuGothicAntique Regular", 25 * -1))

        canvas.after(3000, lambda: canvas.delete(invalid_log))


def account_f(window, canvas, user, Butto):
    global entry_1, entry_2, entry_3
    global back_image, visa, master

    back_image = PhotoImage(
        file=(resource_path("account\\image_1.png")))

    canvas.itemconfig(
        canvas.back, image=back_image)

    entry_1 = Entry(
        canvas,
        bd=0,
        bg="#F5F4F4",
        fg="#424242",
        highlightthickness=0,
        font=("ZenKakuGothicAntique Regular", 19 * -1)
    )
    entry_1.place(
        x=204.0,
        y=255.0,
        width=325.0,
        height=37.0
    )

    entry_2 = Entry(
        canvas,
        bd=0,
        bg="#F5F4F4",
        fg="#424242",
        highlightthickness=0,
        font=("ZenKakuGothicAntique Regular", 19 * -1)
    )
    entry_2.place(
        x=204.0,
        y=435.0,
        width=325.0,
        height=37.0
    )

    entry_3 = Entry(
        canvas,
        bd=0,
        bg="#F5F4F4",
        fg="#424242",
        highlightthickness=0,
        font=("ZenKakuGothicAntique Regular", 19 * -1)
    )
    entry_3.place(
        x=204.0,
        y=506.0,
        width=325.0,
        height=37.0
    )

    saveuserb = PhotoImage(file=resource_path("account/image_2.png"))
    saveuserbh = PhotoImage(file=resource_path("account/image_4.png"))
    saveuserbc = PhotoImage(file=resource_path("account/image_5.png"))

    saveuser = canvas.create_image(
        650,
        270,
        image=saveuserb,
        activeimage=saveuserbh)

    savepass = canvas.create_image(
        650,
        530,
        image=saveuserb,
        activeimage=saveuserbh)

    def on_hold(image_id):
        canvas.itemconfig(image_id, image=saveuserbc,
                          activeimage=saveuserbc)

    def on_release(image_id, window, user):

        canvas.itemconfig(image_id, image=saveuserb,
                          activeimage=saveuserbh)
        if image_id == saveuser:
            change_user(window, canvas, user)
        else:
            change_pass(window, canvas, user)

    canvas.tag_bind(saveuser, "<Button-1>", lambda x: on_hold(saveuser))
    canvas.tag_bind(saveuser, "<ButtonRelease-1>",
                    lambda x: on_release(saveuser, window, user))

    canvas.tag_bind(savepass, "<Button-1>", lambda x: on_hold(savepass))
    canvas.tag_bind(savepass, "<ButtonRelease-1>",
                    lambda x: on_release(savepass, window, user))
