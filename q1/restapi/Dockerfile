FROM python:3.13.14
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY restapi/ .
EXPOSE 10000
CMD ["python", "my_rest_api.py"]