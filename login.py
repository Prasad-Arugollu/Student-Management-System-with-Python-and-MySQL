from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

# ==============================
# CONFIGURATION
# ==============================
WINDOW_SIZE = "1280x700+0+0"
APP_BG_IMG = "background.jpg"
LOGO_IMG = "logo.png"
USER_ICON = "user.png"
PASS_ICON = "password.png"
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

# ==============================
# FUNCTIONS
# ==============================
def login():
    """Validate login credentials."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Both fields are required")
        return

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        window.destroy()  # Close the login window
        # Import or load main app here
        import sms
    else:
        messagebox.showerror("Error", "Invalid username or password")

def toggle_password():
    """Toggle password visibility."""
    if show_pass_var.get():
        password_entry.config(show="")
        show_pass_cb.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_pass_cb.config(text="Show Password")

def load_image(path, size=None):
    """Load image safely, resize if size tuple is given."""
    if not os.path.exists(path):
        return None
    img = Image.open(path)
    if size:
        img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# ==============================
# MAIN WINDOW
# ==============================
window = Tk()
window.geometry(WINDOW_SIZE)
window.title("Login")
window.resizable(False, False)

# Background Image
bg_img = load_image(APP_BG_IMG)
if bg_img:
    Label(window, image=bg_img).place(x=0, y=0)
else:
    window.config(bg="lightgray")

# Login Frame
login_frame = Frame(window, bg ="#F8F9FA", relief=GROOVE)
login_frame.place(x=570, y=150)

# Logo
logo_img = load_image(LOGO_IMG)
if logo_img:
    Label(login_frame, image=logo_img, bg="white").grid(row=0, column=0, columnspan=2, pady=10)

# Username
user_icon = PhotoImage(file=USER_ICON) if os.path.exists(USER_ICON) else None
Label(login_frame, image=user_icon, text="Username", bg="white",
      font=("Times New Roman", 15, 'bold'), compound=LEFT, padx=5)\
    .grid(row=1, column=0, padx=10, pady=10, sticky="w")

username_entry = Entry(login_frame, font=("Times New Roman", 15), bd=3, relief=GROOVE)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Password
pass_icon = PhotoImage(file=PASS_ICON) if os.path.exists(PASS_ICON) else None
Label(login_frame, image=pass_icon, text="Password", bg="white",
      font=("Times New Roman", 15, 'bold'), compound=LEFT, padx=5)\
    .grid(row=2, column=0, padx=10, pady=10, sticky="w")

password_entry = Entry(login_frame, font=("Times New Roman", 15), bd=3, relief=GROOVE, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Show/Hide Password
show_pass_var = BooleanVar()
show_pass_cb = ttk.Checkbutton(login_frame, text="Show Password", variable=show_pass_var, command=toggle_password)
show_pass_cb.grid(row=3, column=1, sticky="w", padx=10)

# Login Button
Button(login_frame, text="Login", width=15, font=("Times New Roman", 15, 'bold'),
       bg="blue", fg="white", bd=3, cursor="hand2", command=login, relief=GROOVE)\
    .grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()
