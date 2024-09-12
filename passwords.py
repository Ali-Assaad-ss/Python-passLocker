from tkinter import *
from popup import popup_f
import clipboard
from launch import resource_path
from jsonenc import decryptjson

NSF = (r".\assets\frame0\\")
NHSF = (r".\assets\frame1\\")
NCSF = (r".\assets\frame2\\")
CSF = (r".\assets\frame3\\")
CHSF = (r".\assets\frame4\\")
CCSF = (r".\assets\frame5\\")


def passwords_f(window, canvas, user, MP, Butto, menu_Button):
    global back_image, passbar_img, searchbi, searchbi, searchbari, searchbci, searchbchi, so, searchb, job
    so = False
    job = None

    def eye1(accs, eye, index):
        passw = accs[index]["password"]
        cont.itemconfig(
            eye, text=length(passw))

    def eye2(eye):
        cont.itemconfig(eye, text="***********")

    def copypassword(accs, index):

        passw = accs[index]["password"]
        clipboard.copy(passw)

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

    def popup(type, index=False, searchaccs=False):
        reset()
        popup_f(window, canvas, user, MP, type, Butto,
                menu_Button, index, searchaccs=searchaccs)
        


    def debounce_search(event=None):
        global job
        if job is not None:
            cont.after_cancel(job)
        job = cont.after(400, search_passwords)

    def search_passwords(event=None):  # Accept an event argument
        global job
        job = None
        query = search_entry.get().lower()

        # Clear existing password entries from the canvas
        for item in cont.find_all():
            cont.delete(item)

        # Filter and display password entries based on the search query
        i = 36
        index = 0
        data = decryptjson(user, MP)
        accs = data.get("accounts")
        if accs:
            for acc in accs:
                if query in acc["website"].lower() or query in acc["username"].lower():

                    passbar = cont.create_image(
                        306.0,
                        i,
                        image=passbar_img
                    )

                    def length(string):
                        if len(string) > 13:
                            result_string = string[:13]
                            return (result_string+"...")
                        else:
                            return string

                    website = cont.create_text(21, i, text=length(acc["website"]), fill="#7370F4", font=(
                        'Helvetica 10 bold'), anchor="w")
                    userl = cont.create_text(221, i, text=length(acc["username"]), fill="#7370F4", font=(
                        'Helvetica 9 bold'), anchor="center")
                    passwo = cont.create_text(
                        366, i, text="************", fill="#7370F4", font=('Helvetica 9 bold'), anchor="center")

                    eye = Butto(cont, 489, i, 9, 1, 1, 7, 7, 7, func=lambda passwo=passwo, index=index: eye1(accs,
                                                                                                             passwo, index), func2=lambda passwo=passwo: eye2(passwo))

                    copy = Butto(cont, 530, i, 10, 2,
                                 func=lambda index=index: copypassword(accs, index))
                    edit = Butto(cont, 575, i, 11, 3,
                                 func=lambda index=index: popup("editpass", index))

                    i += 55
                index += 1

        cont.configure(scrollregion=cont.bbox("all"))

    searchbi = PhotoImage(file=resource_path("assets\\frame0\\searcho.png"))
    searchbhi = PhotoImage(file=resource_path("assets\\frame0\\searchoh.png"))

    searchbci = PhotoImage(file=resource_path(
        "assets\\frame0\\searchc.png"))
    searchbchi = PhotoImage(file=resource_path(
        "assets\\frame0\\searchch.png"))
    searchbari = PhotoImage(file=resource_path(
        "assets\\frame0\\bar.png"))
    searchb = canvas.create_image(
        190, 554, image=searchbi, activeimage=searchbhi)

    def search(event):
        print("go")
        global searchbari, searchbci, searchbchi, search_entry, so, searchbar, searchb

        if so == False:
            canvas.delete(searchb)

            searchbar = canvas.create_image(
                307, 554, image=searchbari)
            searchb = canvas.create_image(
                190, 550, image=searchbci, activeimage=searchbchi)
            canvas.tag_bind(searchb, "<Button-1>", search)

            search_entry = Entry(
                canvas,
                font=("ZenKakuGothicAntique Regular", 13),
                width=17,
                borderwidth=0,
                highlightthickness=0
            )

            # Bind the search_passwords function to the KeyRelease event
            search_entry.bind(
                "<KeyRelease>",debounce_search)
            search_entry.place(x=210, y=538)
            so = True
        else:
            canvas.delete(searchbar)
            canvas.delete(searchb)
            search_entry.destroy()
            searchb = canvas.create_image(
                190, 554, image=searchbi, activeimage=searchbhi)
            canvas.tag_bind(searchb, "<Button-1>", search)
            so = False

    canvas.tag_bind(searchb, "<Button-1>", search)

    back_image = PhotoImage(
        file=resource_path((NSF+"image_1.png")))

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

    i = 36
    index = 0
    data = decryptjson(user, MP)
    accs = data.get("accounts")
    if accs:
        for acc in accs:

            passbar = cont.create_image(
                306.0,
                i,
                image=passbar_img
            )

            def length(string):
                if len(string) > 13:
                    result_string = string[:13]
                    return (result_string+"...")
                else:
                    return string

            website = cont.create_text(21, i, text=length(acc["website"]), fill="#7370F4", font=(
                'Helvetica 10 bold'), anchor="w")
            userl = cont.create_text(221, i, text=length(acc["username"]), fill="#7370F4", font=(
                'Helvetica 9 bold'), anchor="center")
            passwo = cont.create_text(
                366, i, text="************", fill="#7370F4", font=('Helvetica 9 bold'), anchor="center")

            eye = Butto(cont, 489, i, 9, 1, 1, 7, 7, 7, func=lambda passwo=passwo, index=index: eye1(accs,
                                                                                                     passwo, index), func2=lambda passwo=passwo: eye2(passwo))

            copy = Butto(cont, 530, i, 10, 2,
                         func=lambda index=index: copypassword(accs, index))
            edit = Butto(cont, 575, i, 11, 3,
                         func=lambda index=index: popup("editpass", index))
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
                 1, func=lambda: popup("pass"))
    canvas.cont = cont
