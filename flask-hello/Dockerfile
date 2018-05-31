FROM python:2.7
LABEL maintainer="fangfu123<39209557@qq.com>"
RUN pip install flask
COPY app.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]

