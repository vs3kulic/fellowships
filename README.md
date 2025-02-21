# Fellowships

A repository for learning Python with Django by building a web application that tracks battles and outcomes within a fantasy-themed setting.

---

## **Features**
- **Battle Tracking**: Record battles between players and opponents, along with their outcomes (e.g., Win, Loss).
- **Data Storage**: Uses a relational database to store battle data, including players, opponents, timestamps, and outcomes.
- **Django Framework**: Built using Django, a powerful Python web framework for rapid development.
- **Dynamic Web Interface**: Includes templates for displaying data and interacting with the application.
- **Admin Panel**: Manage data using Django's built-in admin interface.

---

## **Tech Stack**
- **Backend**: Python (Django framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)
- **Environment Management**: Virtual environment (`venv`)

---

## **Setup Instructions**

### Prerequisites
1. Install Python 3.9 or higher.
2. Install `pip` (Python's package manager).
3. Install `virtualenv` for creating isolated environments.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/vs3kulic/fellowships.git
   cd fellowships
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and navigate to `http://127.0.0.1:8000`.

---

## **Usage**
1. Access the main page to view or add battle outcomes.
2. Use the admin interface (`/admin`) to manage players, opponents, and outcomes.
3. Explore the database schema to understand how data is structured.

---

## **Database Schema**
The application includes two primary tables:
1. **`app_character`**: Stores information about characters (e.g., players and opponents).
2. **`app_battleoutcome`**: Tracks battle results with fields like:
   - `player`: The character initiating the battle.
   - `opponent`: The opposing character.
   - `outcome`: The result of the battle (e.g., Win or Loss).
   - `timestamp`: The time when the battle occurred.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed information about your changes.

---

## **Issues**
If you encounter any bugs or have feature requests, please open an issue in the GitHub repository.

---

## **License**
This project is licensed under the MIT License.

---

## **Acknowledgments**
Special thanks to contributors and resources that supported this learning project!
