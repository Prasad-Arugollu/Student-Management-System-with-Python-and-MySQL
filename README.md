
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

## <footer>

-   Author: [Prasad-Arugollu](https://github.com/Prasad-Arugollu)
-   Contact: (Provide Contact Details If Available)

**Student-Management-System-with-Python-and-MySQL** - [https://github.com/Prasad-Arugollu/Student-Management-System-with-Python-and-MySQL](https://github.com/Prasad-Arugollu/Student-Management-System-with-Python-and-MySQL)

⭐️ Give a star if you like the project!

   Fork the repository to contribute and make it better! 🛠️
</footer>
