# Use the slim Python 3.10 image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt into the container
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /code/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run database migrations (optional)
RUN python manage.py migrate

# Command to run the Django development server
CMD python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000
