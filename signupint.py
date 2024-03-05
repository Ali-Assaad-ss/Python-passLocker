from tkinter import *
import create_user
from launch import resource_path


def login_(window):
    from loginint import loginint_f
    loginint_f(window)


def signupint_f(window):
    global image_image_1, image_image_2, image_image_3, image_image_4, image_image_5, image_image_6

    def signup_button():
        global invalid_log
        canvas.itemconfig(image_4, image=image_image_6,
                          activeimage=image_image_5)
        user_input = entry_1.get()
        MP_input = entry_2.get()
        if user_input == "" or MP_input == "":
            try:
                canvas.delete(invalid_log)
            except:
                pass
            invalid_log = canvas.create_text(
                180.0,
                480.0,
                anchor="nw",
                text="Enter username and password",
                fill="#c25d5d",
                font=("ZenKakuGothicAntique Regular", 16 * -1))
            canvas.after(2000, lambda: canvas.delete(invalid_log))
        else:
            if create_user.createuser(user_input, MP_input):
                try:
                    canvas.delete(invalid_log)
                except:
                    pass
                invalid_log = canvas.create_text(
                    215.0,
                    480.0,
                    anchor="nw",
                    text="account created,log in",
                    fill="#1f4a15",
                    font=("ZenKakuGothicAntique Regular", 16 * -1))
                canvas.after(2000, lambda: canvas.delete(invalid_log))
                canvas.after(1000, lambda: login_(window))
            else:
                try:
                    canvas.delete(invalid_log)
                except:
                    pass
                invalid_log = canvas.create_text(
                    230.0,
                    480.0,
                    anchor="nw",
                    text="username taken",
                    fill="#c25d5d",
                    font=("ZenKakuGothicAntique Regular", 16 * -1))
                canvas.after(2000, lambda: canvas.delete(invalid_log))

    _list = window.winfo_children()

    for item in _list:
        item.destroy()

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=565,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=resource_path(("login-signup/signup/image_1.png")))
    image_1 = canvas.create_image(
        400.0,
        282.0,
        image=image_image_1
    )

    image_image_3 = PhotoImage(
        file=resource_path(("login-signup/signup/image_3.png")))

    image_image_2 = PhotoImage(
        file=resource_path(("login-signup/signup/image_2.png")))
    image_2 = canvas.create_image(
        537.6044921875,
        27.125,
        image=image_image_2,
        activeimage=image_image_3
    )
    image_image_4 = PhotoImage(
        file=resource_path(("login-signup/signup/image_4.png")))
    image_image_5 = PhotoImage(
        file=resource_path(("login-signup/signup/image_5.png")))
    image_image_6 = PhotoImage(
        file=resource_path(("login-signup/signup/image_6.png")))

    image_4 = canvas.create_image(
        291.0,
        439.0,
        image=image_image_6,
        activeimage=image_image_5
    )
    entry_1 = Entry(
        canvas,
        bd=0,
        bg="#F1F4FE",
           fg="#424242",
           highlightthickness=0,
           font=(16.0)
    )
    entry_1.place(
        x=105.0,
        y=221.0,
        width=375.0,
        height=45.0
    )

    entry_2 = Entry(
        canvas,
        bd=0,
        bg="#F1F4FE",
        fg="#424242",
        highlightthickness=0,
        font=(16.0)
    )

    entry_2.place(
        x=105.0,
        y=315.0,
        width=375.0,
        height=45.0
    )

    canvas.tag_bind(image_4, "<Button-1>", lambda x: canvas.itemconfig(image_4,
                    image=image_image_4, activeimage=image_image_4))
    canvas.tag_bind(image_4, "<ButtonRelease-1>", lambda x: signup_button())

    canvas.tag_bind(image_2, "<Button-1>", lambda x: login_(window))
