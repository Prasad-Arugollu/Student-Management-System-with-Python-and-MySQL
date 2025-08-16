
# Student Management System with Python and MySQL 🚀

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)

A simple Student Management System built with Python and MySQL, providing a graphical user interface (GUI) for managing student records. 📚

## 📌 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How to Use](#-how-to-use)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Important Links](#-important-links)
- [Footer](#-footer)


## 📝 Description

This project is a desktop application developed in Python using Tkinter for the GUI and MySQL for database management. It allows users to efficiently manage student records, including adding, searching, updating, deleting, viewing, and exporting student information. 💻

## ✨ Features

- **Login Functionality**: Secure access with username and password verification. 🔐
- **Student Data Management**: Add, search, delete, update, and view student records. 🧑‍🎓
- **Database Connectivity**: Uses MySQL to store and manage student information. 🗄️
- **GUI**: User-friendly interface built with Tkinter and ttkthemes. 🎨
- **Animated Slider**: Dynamic title display for an enhanced user experience. 💡
- **Real-time Clock**: Displays the current date and time. ⏰
- **Export to CSV**: Export student data to a CSV file. 📊

## 🛠️ Tech Stack

- **Language**: Python 🐍
- **GUI Toolkit**: Tkinter
- **Theming**: ttkthemes
- **Database**: MySQL ⚙️
- **Libraries**: pymysql, pandas, PIL (Pillow)

## ⚙️ Installation

1.  **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2.  **Install Required Libraries**: Use pip to install the necessary libraries. Open your terminal and run:

    ```bash
    pip install tkinter pillow ttkthemes pymysql pandas
    ```

3.  **Setup MySQL Database**: 
    - Install MySQL on your system.
    - Create a database named `student_management_system`.
    - Create table named `student` with these columns:
    ```
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    class VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    address VARCHAR(255) NOT NULL
    ```

4.  **Update Database Connection**: Modify the `sms.py` file to include your MySQL credentials.
    ```python
    # for users use this logins
    host = 'localhost'
    user = 'root'
    password = '1234'
    ```
    Update the host, user, and password.

## 💻 Usage

1.  **Run the Login**: Execute the `login.py` script to start the application.
    ```bash
    python login.py
    ```

2.  **Login Credentials**: Use the default credentials to log in:
    -   **Username**: `admin`
    -   **Password**: `admin`

3.  **Connect to Database**: In the main application window, click the "Connect to Database" button and provide your database credentials in the popup window.
4.  **Manage Students**: Use the buttons on the left frame to add, search, update, delete, view, and export student records. 🚀

## 💡 How to Use

This Student Management System can be used in educational institutions to efficiently manage student data. Here are a few real-world use cases:

-   **Record Keeping**: Maintain an organized record of student information, including personal details, contact information, and academic details. 🏫
-   **Data Retrieval**: Quickly search and retrieve student records based on various criteria. 🔍
-   **Reporting**: Export student data for generating reports and analytics. 📈
-   **User Access Control**: Secure the system with login functionality, ensuring that only authorized personnel can access and modify student data. 🛡️




 # 🧭 How to Use (Step-by-Step)

## 1) Launch the App  
1. Start the server/application.  
2. Open the app in your browser (e.g., `http://localhost:5000`).  

<img width="1795" height="836" alt="Screenshot 2025-08-16 153802" src="https://github.com/user-attachments/assets/a70adc99-e68b-4393-9637-8a82482aa9cf" />


---

## 2) Log In  
1. Enter **username** and **password**.  
2. Click **Login** to access the dashboard.  

<img width="1796" height="831" alt="Screenshot 2025-08-16 111207" src="https://github.com/user-attachments/assets/2427e4cd-0ae8-4b82-8590-9dc2891aec61" />
 

---

## 3) Dashboard Overview  
1. Connect to Database
2. Get the Database connection by filing the fields( **Hostname**, **Username** and **Password**)

<img width="1795" height="829" alt="Screenshot 2025-08-16 111318" src="https://github.com/user-attachments/assets/718d5cdb-4521-4df4-ab73-18c3011064f7" />



---

## 4) Add a New Student  
1. Go to **Add Student**  
2. Fill fields like **ID**, **Name**, **Mobile Number**, **Email**, **Age**, **Class**, **Gender**, **Address**.   
3. Click **Add Student**.  
4. Confirm success and that the new student appears in the list.  

<img width="1800" height="826" alt="Screenshot 2025-08-16 154748" src="https://github.com/user-attachments/assets/e782e565-ec39-47ca-ab25-c9f515d401a4" />


---


## 5) Search Students  
1. In the list view, type a **ID** or **Name** in the search bar.  
2. Confirm results filter correctly.  

<img width="1794" height="820" alt="Screenshot 2025-08-16 155335" src="https://github.com/user-attachments/assets/631dcc31-5863-4329-8bbb-8fb2acc4cafe" />


---

## 6) Delete a Student (with Confirmation)  
1. Click **Delete student** 
2. Confirm the **Are you sure?** modal.  
3. Verify the record is removed.  



---


## 7) Update a Student  
1. click **Update Student** 
2. Modify fields.  
3. Click **Update** and verify the changes.  

<img width="1792" height="829" alt="Screenshot 2025-08-16 152702" src="https://github.com/user-attachments/assets/bb6c50f5-292c-40c9-9827-867407373e35" />


---

## 8) View Student Details  
1. Click a  **View student** action to open a detailed profile.  
2. Review personal info, contact, and academic data.  

<img width="1790" height="827" alt="Screenshot 2025-08-16 160219" src="https://github.com/user-attachments/assets/d76d8792-ecc5-42d8-91b8-1817bbd6ff69" />

---

## 9) Reports / Export (If Present)  
1. Go to **Reports**.  
2. Click **Export** → **CSV/Excel/PDF**.  

<img width="1788" height="837" alt="Screenshot 2025-08-16 160339" src="https://github.com/user-attachments/assets/9a0bb9b6-cdb9-4f5a-a405-c5bbbf89181d" />

---

<img width="1808" height="828" alt="Screenshot 2025-08-16 160407" src="https://github.com/user-attachments/assets/93f631cd-0d1f-4808-9134-26a4ee25a952" />

 



## 📂 Project Structure

```
Student-Management-System-with-Python-and-MySQL/
├── login.py          # Login module
├── sms.py            # Main application module
├── README.md         # Project documentation
└── students.png      # Logo (optional) if you want to add a logo for the app.
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository. 🍴
2.  Create a new branch for your feature or bug fix. 🌿
3.  Make your changes and commit them. ✍️
4.  Push your changes to your fork. 📤
5.  Submit a pull request. ✅

## 📜 License

This project has no license.

## 🔗 Important Links

-   This project repository: [Student-Management-System-with-Python-and-MySQL](https://github.com/Prasad-Arugollu/Student-Management-System-with-Python-and-MySQL)


**Student-Management-System-with-Python-and-MySQL** - [https://github.com/Prasad-Arugollu/Student-Management-System-with-Python-and-MySQL](https://github.com/Prasad-Arugollu/Student-Management-System-with-Python-and-MySQL)

⭐️ Give a star if you like the project!

   Fork the repository to contribute and make it better! 🛠️
</footer>
