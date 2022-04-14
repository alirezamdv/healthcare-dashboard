FROM python:3.8-slim
COPY ./smile_api/pysmile.txt .
COPY ./smile_api/requirements.txt .
RUN pip install -r pysmile.txt
RUN pip install -r requirements.txt
COPY ./smile_api/ .


CMD [ "uvicorn" , "--host", "0.0.0.0","--reload", "--port", "5000", "app.main:app" ]
