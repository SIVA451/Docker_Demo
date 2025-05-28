# demo/Dockerfile
FROM python:3.12-slim

# install a very small web framework
RUN pip install --no-cache-dir flask

# copy demo app
COPY app.py /app/app.py
WORKDIR /app

# expose port 5000 for the students
EXPOSE 5000

# launch the server
ENTRYPOINT ["python", "app.py"]
