FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /LastProject

COPY requirements.txt /LastProject/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /LastProject/

