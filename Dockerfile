FROM python:3.9-slim

WORKDIR /app

COPY env/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "inference/app.py"]
