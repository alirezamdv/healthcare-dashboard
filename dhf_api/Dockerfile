FROM python:3.8-slim

COPY ./dhf_api/requirements.txt .
RUN pip install -r requirements.txt
COPY ./dhf_api/ .
CMD ["uvicorn" , "--host", "0.0.0.0","--reload", "--port", "5000", "app.main:app" ]
