from tkinter import *
from signupint import signupint_f
from launch import resource_path

def loginint_f(window):

    def login_button():
        canvas.itemconfig(image_4, image=image_image_6,
                          activeimage=image_image_5)
        user = entry_1.get()
        Password = entry_2.get()
        from login_ import login
        user, pass_input = login(user, Password)
        if pass_input:
            from gui import dash
            dash(window, user, Password)
        else:
            invalid_log = canvas.create_text(
                180.0,
                480.0,
                anchor="nw",
                text="Invalid username or password",
                fill="#c25d5d",
                font=("ZenKakuGothicAntique Regular", 16 * -1))
            canvas.after(3000, lambda: canvas.delete(invalid_log))

    _list = window.winfo_children()

    for item in _list:
        item.destroy()

    global image_image_1, image_image_2, image_image_3, image_image_4, image_image_5, image_image_6

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
        file=resource_path(("login-signup/login/image_1.png")))
    image_1 = canvas.create_image(
        400.0,
        282.0,
        image=image_image_1
    )

    image_image_3 = PhotoImage(
        file=resource_path(("login-signup/login/image_3.png")))

    image_image_2 = PhotoImage(
        file=resource_path(("login-signup/login/image_2.png")))
    image_2 = canvas.create_image(
        537.6044921875,
        27.125,
        image=image_image_2,
        activeimage=image_image_3
    )
    image_image_4 = PhotoImage(
        file=resource_path(("login-signup/login/image_4.png")))
    image_image_5 = PhotoImage(
        file=resource_path(("login-signup/login/image_5.png")))
    image_image_6 = PhotoImage(
        file=resource_path(("login-signup/login/image_6.png")))

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
        font=(16.0),
        show="*"
    )

    entry_2.place(
        x=105.0,
        y=315.0,
        width=375.0,
        height=45.0
    )

    canvas.tag_bind(image_4, "<Button-1>", lambda x: canvas.itemconfig(image_4,
                    image=image_image_4, activeimage=image_image_4))
    canvas.tag_bind(image_4, "<ButtonRelease-1>", lambda x: login_button())

    canvas.tag_bind(image_2, "<Button-1>", lambda x: signupint_f(window))
