FROM python:3.11-alpine
RUN apk add --no-cache gcc musl-dev libffi-dev
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
