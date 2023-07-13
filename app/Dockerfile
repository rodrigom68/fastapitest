# initial python original image

FROM python:3.9

# Set this  current path
WORKDIR /code

# Copy this directory for the current path
COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file
RUN pip Install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the ./app directory inside the /code directory
COPY ./app /code/app

# Set the command to run the uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
