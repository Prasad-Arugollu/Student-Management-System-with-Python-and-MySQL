from tkinter import *
from tkinter import ttk, messagebox,filedialog
import time
import ttkthemes
import pymysql
import pandas

# ------------------- CONFIG ------------------- #
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 700
LEFT_FRAME_WIDTH = 300
RIGHT_FRAME_WIDTH = 820
FRAME_HEIGHT = 600

TITLE_TEXT = "Student Management System"
SLIDER_SPEED = 300
CLOCK_REFRESH = 1000
BG_COLOR = "#d4e6f1"  # unified background color

# ------------------- CLOCK ------------------- #
def update_clock():
    current_date = time.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")
    datetime_label.config(text=f"    Date: {current_date}\n  Time: {current_time}")
    datetime_label.after(CLOCK_REFRESH, update_clock)

# ------------------- SLIDER ------------------- #
slider_text = ''
slider_index = 0

def animate_slider():
    global slider_text, slider_index
    if slider_index >= len(TITLE_TEXT):
        slider_index = 0
        slider_text = ''
    slider_text += TITLE_TEXT[slider_index]
    slider_label.config(text=slider_text)
    slider_index += 1
    slider_label.after(SLIDER_SPEED, animate_slider)

# ------------------- DB CONNECTION ------------------- #
def connecting_database():
    def connect():
        global mycursor, con
        host = 'localhost'
        user = 'root'
        password = '1234'

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect:\n{e}", parent=pop_up)
            return
        
        try:
            mycursor.execute("CREATE DATABASE student_management_system")
        except:
            pass

        try:
            mycursor.execute("USE student_management_system")
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    mobile_number VARCHAR(20) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    class VARCHAR(50) NOT NULL,
                    gender ENUM('Male', 'Female') NOT NULL,
                    address VARCHAR(255) NOT NULL
                )
            """)
            pop_up.destroy()
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            deletestudentButton.config(state=NORMAL)
            updatestudentButton.config(state=NORMAL)
            viewstudentsButton.config(state=NORMAL)
            exportstudentsButton.config(state=NORMAL)
            exitButton.config(state=NORMAL)



        except Exception as e:
            messagebox.showerror("Error", f"Database setup failed:\n{e}", parent=pop_up)

    pop_up = Toplevel()
    pop_up.grab_set()
    pop_up.title("Database Connection")
    pop_up.geometry("470x300+720+230")
    pop_up.resizable(False, False)
    pop_up.configure(bg=BG_COLOR)  # same as main bg

    Label(pop_up, text="Hostname:", font=('Times New Roman', 15, 'bold'), bg=BG_COLOR).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    Label(pop_up, text="Username:", font=('Times New Roman', 15, 'bold'), bg=BG_COLOR).grid(row=1, column=0, padx=20, pady=10, sticky="w")
    Label(pop_up, text="Password:", font=('Times New Roman', 15, 'bold'), bg=BG_COLOR).grid(row=2, column=0, padx=20, pady=10, sticky="w")

    hostname_entry = Entry(pop_up, font=('Times New Roman', 20, 'bold'))
    hostname_entry.grid(row=0, column=1, padx=10, pady=10)
    

    username_entry = Entry(pop_up, font=('Times New Roman', 20, 'bold'))
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    

    password_entry = Entry(pop_up, font=('Times New Roman', 20, 'bold'), show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    password_entry.insert(0, "")

    connect_button = ttk.Button(pop_up, text="Connect", width=10, command=connect)
    connect_button.grid(row=3, column=0, columnspan=2, pady=20)

def add_student():
    def add_data():
        if id_entry.get() == "" or name_entry.get() == "" or mobile_entry.get() == "" or email_entry.get() == "" or age_entry.get() == "" or class_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=add_window)
            return
        else:
            try:
                query = "INSERT INTO student values(%s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(query, (id_entry.get(), name_entry.get(), mobile_entry.get(), email_entry.get(), age_entry.get(), class_entry.get(), gender_combo.get(), address_entry.get()))
                con.commit()
                if messagebox.askyesno("Confirm","Student added successfully, Do you want to clear the form?", parent=add_window):
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    mobile_entry.delete(0, END)
                    email_entry.delete(0, END)
                    age_entry.delete(0, END)
                    class_entry.delete(0, END)
                    gender_combo.set("")
                    address_entry.delete(0, END)
                else:
                    pass
                add_window.destroy()
            except:
                messagebox.showerror("Error", "ID Cannot be repeated", parent=add_window)
                return


            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for row in fetched_data:
                datalist = list(row)
                student_table.insert("", "end", values=datalist)

    add_window = Toplevel()
    add_window.title("Add Student")
    add_window.resizable(False, False)
    add_window.grab_set()
    # ID
    id_label = Label(add_window, text="ID:", font=('Times New Roman', 20, 'bold'))
    id_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    id_entry = Entry(add_window, font=('Times New Roman', 20))
    id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Name
    name_label = Label(add_window, text="Name:", font=('Times New Roman', 20, 'bold'))
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    name_entry = Entry(add_window, font=('Times New Roman', 20))
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Mobile Number
    mobile_label = Label(add_window, text="Mobile Number:", font=('Times New Roman', 20, 'bold'))
    mobile_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    mobile_entry = Entry(add_window, font=('Times New Roman', 20))
    mobile_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Email
    email_label = Label(add_window, text="Email:", font=('Times New Roman', 20, 'bold'))
    email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    email_entry = Entry(add_window, font=('Times New Roman', 20))
    email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Age
    age_label = Label(add_window, text="Age:", font=('Times New Roman', 20, 'bold'))
    age_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    age_entry = Entry(add_window, font=('Times New Roman', 20))
    age_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Class
    class_label = Label(add_window, text="Class:", font=('Times New Roman', 20, 'bold'))
    class_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    class_entry = Entry(add_window, font=('Times New Roman', 20))
    class_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Gender
    gender_label = Label(add_window, text="Gender:", font=('Times New Roman', 20, 'bold'))
    gender_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    gender_combo = ttk.Combobox(add_window, font=('Times New Roman', 20), values=["Male", "Female"], state="readonly")
    gender_combo.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Address
    address_label = Label(add_window, text="Address:", font=('Times New Roman', 20, 'bold'))
    address_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    address_entry = Entry(add_window, font=('Times New Roman', 20))
    address_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")
# Place this before your add_student_button line:
    style = ttk.Style(add_window)
    style.configure('Add.TButton', font=('Times New Roman', 15, 'bold'))

# Create the button:
    add_student_button = ttk.Button(add_window, text="Add Student", style='Add.TButton', width=20,command  = add_data)
    add_student_button.grid(row=8, column=0, columnspan=2, pady=20)
    
def search_student():
    def search_data():
        query = "SELECT * FROM student WHERE id=%s OR name=%s OR mobile_number=%s OR email=%s OR age=%s OR class=%s OR gender=%s OR address=%s"
        mycursor.execute(query, (id_entry.get(), name_entry.get(), mobile_entry.get(), email_entry.get(), age_entry.get(), class_entry.get(), gender_combo.get(), address_entry.get()))
        student_table.delete(*student_table.get_children())
        results = mycursor.fetchall()
        for row in results:
            student_table.insert("", "end", values=row)
        search_window.destroy()

    search_window = Toplevel()
    search_window.title("Search Student")
    search_window.resizable(False, False)
    search_window.grab_set()

    # ID
    id_label = Label(search_window, text="ID:", font=('Times New Roman', 20, 'bold'))
    id_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    id_entry = Entry(search_window, font=('Times New Roman', 20))
    id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Name
    name_label = Label(search_window, text="Name:", font=('Times New Roman', 20, 'bold'))
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    name_entry = Entry(search_window, font=('Times New Roman', 20))
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Mobile Number
    mobile_label = Label(search_window, text="Mobile Number:", font=('Times New Roman', 20, 'bold'))
    mobile_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    mobile_entry = Entry(search_window, font=('Times New Roman', 20))
    mobile_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Email
    email_label = Label(search_window, text="Email:", font=('Times New Roman', 20, 'bold'))
    email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    email_entry = Entry(search_window, font=('Times New Roman', 20))
    email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Age
    age_label = Label(search_window, text="Age:", font=('Times New Roman', 20, 'bold'))
    age_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    age_entry = Entry(search_window, font=('Times New Roman', 20))
    age_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Class
    class_label = Label(search_window, text="Class:", font=('Times New Roman', 20, 'bold'))
    class_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    class_entry = Entry(search_window, font=('Times New Roman', 20))
    class_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Gender
    gender_label = Label(search_window, text="Gender:", font=('Times New Roman', 20, 'bold'))
    gender_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    gender_combo = ttk.Combobox(search_window, font=('Times New Roman', 20), values=["Male", "Female"], state="readonly")
    gender_combo.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Address
    address_label = Label(search_window, text="Address:", font=('Times New Roman', 20, 'bold'))
    address_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    address_entry = Entry(search_window, font=('Times New Roman', 20))
    address_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")
# Place this before your search_student_button line:
    style = ttk.Style(search_window)
    style.configure('Search.TButton', font=('Times New Roman', 15, 'bold'))

# Create the button:
    search_student_button = ttk.Button(search_window, text="Search Student", style='Search.TButton', width=20,command  = search_data)
    search_student_button.grid(row=8, column=0, columnspan=2, pady=20)
    
def delete_student():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?", parent=root):
        indexing = student_table.focus()
        content = student_table.item(indexing)
        content_id = content['values'][0]
        query = "DELETE FROM student WHERE id = %s"
        mycursor.execute(query, (content_id,))
        con.commit()
        query = 'SELECT * FROM student'
        mycursor.execute(query)
        results = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for row in results:
            student_table.insert("", "end", values=row)

def view_students():
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    results = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for row in results:
        student_table.insert("", "end", values=row)
        
def update_student():
    def update_data():
        query = "UPDATE student SET name=%s, mobile_number=%s, email=%s, age=%s, class=%s, gender=%s, address=%s WHERE id=%s"
        mycursor.execute(query, (name_entry.get(), mobile_entry.get(), email_entry.get(), age_entry.get(), class_entry.get(), gender_combo.get(), address_entry.get(), id_entry.get()))
        con.commit()
        messagebox.showinfo("Updated", "Student updated successfully", parent=update_window)
        update_window.destroy()
        view_students()

    update_window = Toplevel()
    update_window.title("Update Student")
    update_window.resizable(False, False)
    update_window.grab_set()

    # ID
    id_label = Label(update_window, text="ID:", font=('Times New Roman', 20, 'bold'))
    id_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    id_entry = Entry(update_window, font=('Times New Roman', 20))
    id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Name
    name_label = Label(update_window, text="Name:", font=('Times New Roman', 20, 'bold'))
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    name_entry = Entry(update_window, font=('Times New Roman', 20))
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Mobile Number
    mobile_label = Label(update_window, text="Mobile Number:", font=('Times New Roman', 20, 'bold'))
    mobile_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    mobile_entry = Entry(update_window, font=('Times New Roman', 20))
    mobile_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Email
    email_label = Label(update_window, text="Email:", font=('Times New Roman', 20, 'bold'))
    email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    email_entry = Entry(update_window, font=('Times New Roman', 20))
    email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Age
    age_label = Label(update_window, text="Age:", font=('Times New Roman', 20, 'bold'))
    age_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    age_entry = Entry(update_window, font=('Times New Roman', 20))
    age_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Class
    class_label = Label(update_window, text="Class:", font=('Times New Roman', 20, 'bold'))
    class_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    class_entry = Entry(update_window, font=('Times New Roman', 20))
    class_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Gender
    gender_label = Label(update_window, text="Gender:", font=('Times New Roman', 20, 'bold'))
    gender_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    gender_combo = ttk.Combobox(update_window, font=('Times New Roman', 20), values=["Male", "Female"], state="readonly")
    gender_combo.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Address
    address_label = Label(update_window, text="Address:", font=('Times New Roman', 20, 'bold'))
    address_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    address_entry = Entry(update_window, font=('Times New Roman', 20))
    address_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")
# Place this before your search_student_button line:
    style = ttk.Style(update_window)
    style.configure('Search.TButton', font=('Times New Roman', 15, 'bold'))

# Create the button:
    update_student_button = ttk.Button(update_window, text="Update Student", style='Search.TButton', width=20,command  = update_data)
    update_student_button.grid(row=8, column=0, columnspan=2, pady=20)

    indexing = student_table.focus()
    content = student_table.item(indexing)
    content_id = content['values']
    id_entry.insert(0, content_id[0])
    name_entry.insert(0, content_id[1])
    mobile_entry.insert(0, content_id[2])
    email_entry.insert(0, content_id[3])
    age_entry.insert(0, content_id[4])
    class_entry.insert(0, content_id[5])
    gender_combo.set(content_id[6])
    address_entry.insert(0, content_id[7])
    
def export_students():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = student_table.get_children()
    new_list = []
    for index in indexing:
        content = student_table.item(index)
        data_list = content['values']
        new_list.append(data_list)

    table = pandas.DataFrame(new_list, columns=["ID", "Name", "Mobile Number", "Email", "Age", "Class", "Gender", "Address"])
    table.to_csv(url, index=False)

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root):
        root.destroy()
    else:
        pass
# ------------------- MAIN WINDOW ------------------- #
root = ttkthemes.ThemedTk()
root.set_theme("aquativo")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
root.title(TITLE_TEXT)
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Clock
datetime_label = Label(root, font=('Times New Roman', 20, 'bold'), bg=BG_COLOR)
datetime_label.place(x=10, y=10)
update_clock()

# Slider
slider_label = Label(root, text="", font=('Times New Roman', 30, 'bold'), width=30, anchor="center", bg=BG_COLOR)
slider_label.place(x=(WINDOW_WIDTH // 2) - 250, y=0)
animate_slider()

# Connect Button
connect_database = ttk.Button(root, text="Connect to Database", command=connecting_database)
connect_database.place(x=1060, y=20)

# Style
style = ttk.Style()
style.configure("TButton", font=('Times New Roman', 15, 'bold'), anchor="center")
style.configure("Treeview.Heading", font=('Times New Roman', 14, 'bold'))
style.configure("Treeview", rowheight=40, font=('Times New Roman', 15))

# Left Frame
left_frame = Frame(root, bg=BG_COLOR)
left_frame.place(x=50, y=90, width=LEFT_FRAME_WIDTH, height=WINDOW_HEIGHT - 90)

try:
    logo_image = PhotoImage(file="students.png")
    logo_label = Label(left_frame, image=logo_image, bg=BG_COLOR)
    logo_label.grid(row=0, column=0, pady=20)
except Exception:
    logo_label = Label(left_frame, text="No Logo", font=('Times New Roman', 14), bg=BG_COLOR)
    logo_label.grid(row=0, column=0, pady=20)


addstudentButton = ttk.Button(left_frame, text="Add Student", width=25, state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, padx=10, pady=15)

searchstudentButton = ttk.Button(left_frame, text="Search Student", width=25, state=DISABLED, command=search_student)
searchstudentButton.grid(row=2, column=0, padx=10, pady=15)

deletestudentButton = ttk.Button(left_frame, text="Delete Student", width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, padx=10, pady=15)

updatestudentButton = ttk.Button(left_frame, text="Update Student", width=25, state=DISABLED, command=update_student)
updatestudentButton.grid(row=4, column=0, padx=10, pady=15)

viewstudentsButton = ttk.Button(left_frame, text="View Students", width=25, state=DISABLED, command=view_students)
viewstudentsButton.grid(row=5, column=0, padx=10, pady=15)

exportstudentsButton = ttk.Button(left_frame, text="Export Students", width=25, state=DISABLED, command=export_students)
exportstudentsButton.grid(row=6, column=0, padx=10, pady=15)

exitButton = ttk.Button(left_frame, text="Exit", width=25, state=DISABLED, command=exit_app)
exitButton.grid(row=7, column=0, padx=10, pady=15)

# Right Frame
right_frame = Frame(root)
right_frame.place(x=LEFT_FRAME_WIDTH + 100, y=90, width=RIGHT_FRAME_WIDTH, height=FRAME_HEIGHT)

scroll_x = Scrollbar(right_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(right_frame, orient=VERTICAL)

student_table = ttk.Treeview(
    right_frame,
    columns=("ID", "Name", "Mobile Number", "Email", "Age", "Class", "Gender", "Address"),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
student_table.pack(fill=BOTH, expand=True)

headings = {
    "ID": 100,
    "Name": 200,
    "Mobile Number": 200,
    "Email": 250,
    "Age": 100,
    "Class": 150,
    "Gender": 150,
    "Address": 300
}

for col_name, col_width in headings.items():
    student_table.heading(col_name, text=col_name)
    student_table.column(col_name, width=col_width,anchor="center")

student_table.config(show='headings')



# Run App
root.mainloop()
