FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . .

# Installing needed packages specified in requirements.txt

EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "mlops_model.py"]
