FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pandas matplotlib scikit-learn pymongo PyQt6 sqlalchemy
EXPOSE 5000
CMD ["python", "app.py"]
