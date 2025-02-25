# Sample Django Project

This is a sample Django project. Follow the steps below to set up the project on your local machine.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Steps to Set Up the Project

1. **Clone the repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/manikanta-taashee/sample_django_project.git
   cd sample_django_project/
   ```

2. **Create a virtual environment**  
   Create a virtual environment to manage dependencies:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**  
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**  
   Install the required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations (if necessary)**  
   If the project has any database migrations, run the following command:
   ```bash
   python manage.py migrate
   ```

6. **Run the Django development server**  
   Start the development server:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**  
   Once the server is running, open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

Now you should have the Django app running locally!

## Additional Information

- Make sure to deactivate the virtual environment when you're done:
  ```bash
  deactivate
  ```

- If you encounter any issues, please check the project's documentation or open an issue.