# Dockerfile cho Cart Service
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
COPY ../../certs/rootCA.crt /app/certs/rootCA.crt 
COPY ../../certs/server.crt /app/certs/server.crt 
COPY ../../certs/server.key /app/certs/server.key
RUN pip install Flask
EXPOSE 8080
CMD ["python", "app.py"]