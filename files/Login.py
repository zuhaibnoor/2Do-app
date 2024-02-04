from PIL import Image
from customtkinter import *
from CTkMessagebox import CTkMessagebox

# function for checking whether there is already a user logged in
def check_loginStatus():
    with open("login_status.txt") as file:
        info = file.read()
        info = eval(info)
        if info == '':
            return 0
        else:
            login(info[0], info[1])


#login function, passed as command to login button in run.py under mainmenu()
def login(root, frame, user_name, pwd):    

    # The file opening function is placed under try block incase the given usrname does not exist
    try:
        with open(f"files/users/{user_name.get()}.txt") as file:
            file = file.read()
            file = eval(file)

            if file[user_name.get()] == pwd.get():
                
                username = str(user_name.get())
                frame.destroy()

                #----------------------------------frames-----------------------------------------
                #Setting up a new parent frame
                parent_frame = CTkFrame(root)
                parent_frame.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

                parent_frame_bg=CTkImage(Image.open("images/img.jpg"), size = (900,650))
                parent_frame_bg_label=CTkLabel(parent_frame, image = parent_frame_bg)
                parent_frame_bg_label.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

                #setting 2 child frames inside the parent_frame containing the UI components and 2do list repectively
                child_frame1 = CTkFrame(parent_frame, fg_color="#221a2e", border_color="#9e59f7", border_width=2, corner_radius=10)
                child_frame1.place(relx = 0.18, rely = 0.5, relwidth = 0.3, relheight = 0.85, anchor = CENTER)
                
                username_label = CTkLabel(child_frame1, text = "Current User:\n" + username, font = CTkFont(size = 20))
                username_label.place(relx = 0.5, rely = 0.08, anchor = CENTER)

                child_frame2 = CTkFrame(parent_frame, fg_color="#221a2e", border_color= "#9e59f7", border_width = 2, corner_radius= 10)
                child_frame2.place(relx = 0.67, rely = 0.5 ,relwidth = 0.6, relheight = 0.85 ,anchor = CENTER)

                # setting up a scrollframe inside the child frame2 that will hold the to do list
                scroll_frame = CTkScrollableFrame(child_frame2, fg_color = "#16101D")
                scroll_frame.place(relx = 0.5, rely = 0.45, relwidth= 0.9, relheight = 0.75, anchor = CENTER)
                
                # entry for entering the items in the list
                list_entry = CTkEntry(child_frame2, placeholder_text="Enter task", height=35, corner_radius = 20)
                list_entry.place(relx = 0.5, rely = 0.88,relwidth = 0.7, anchor = CENTER )

                #--------------------------------buttons----------------------------------------

                # logout button
                logout_button_img = CTkImage(Image.open("images/logout_icon.png"), size=(40,40))
                logout_button = CTkButton(child_frame1, text = "   Logout   ", image = logout_button_img, fg_color="#16111F",hover_color="#49484a", width =85, height = 40, font=CTkFont(size=14) )
                logout_button.place(relx = 0.5, rely = 0.2, anchor = CENTER)

                # Add button
                add_button_img = CTkImage(Image.open("images/add_icon.png"), size = (40,40))
                add_button = CTkButton(child_frame1, text = "     Add    ", image = add_button_img, font=CTkFont(size=14), fg_color= "#006026", hover_color="#008836")
                add_button.place(relx = 0.5, rely =0.77, anchor = CENTER)

                # delete button
                delete_button_img = CTkImage(Image.open("images/delete_icon.png"), size = (40,40))
                delete_button = CTkButton(child_frame1, text = "   Delete   ", image = delete_button_img,font=CTkFont(size=14), fg_color="#7A0303", hover_color="#9E0000")
                delete_button.place(relx = 0.5, rely = 0.9, anchor = CENTER)

            else:
                CTkMessagebox(icon = "cancel", title = "Error!", message="Incorrect password!")
                pwd.delete(0,END)
                
    except:
        # if no user is found
        CTkMessagebox(icon = "cancel", title="Error!", message="No such username found!")

#test
# root = CTk()
# root.geometry("500x500")

# scrol = CTkScrollableFrame(root, height= 250, width=250)
# scrol.place(relx = 0.5, rely = 0.5,anchor  = CENTER)

# root.mainloop()