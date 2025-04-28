# Personal Task Manager (To-Do App)

A simple and intuitive to-do list application built using Flask and SQLite. This app enables users to efficiently create, update, and delete tasks, helping them stay organized and productive.

## Features
- Add new tasks with ease.
- Update existing tasks, including marking tasks as complete.
- Delete tasks that are no longer needed.
- Persistent storage with SQLite to save your tasks.

## Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (for basic styling)

## Prerequisites
Before running the app locally, ensure you have the following installed:
- Python 3.9 or higher
- pip (Python package installer)

## How to Run Locally

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Kirankumarvel/todo-app.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd todo-app
    ```

3. **Set Up a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**:
    ```bash
    python app.py
    ```

6. **Access the Application**:
    Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure
```
todo-app/
├── app.py             # Main application file
├── templates/         # HTML templates for the app
├── static/            # Static files (CSS, JS, images)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
├── LICENSE            # License file
└── taskdb.db          # SQLite database file (auto-generated)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

## Contact
If you have any questions or suggestions, feel free to reach out:
- GitHub: [Kirankumarvel](https://github.com/Kirankumarvel)

---

Happy task managing! 🎉
``` 
