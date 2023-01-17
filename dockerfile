FROM python:3.10.6

ADD akyg.py /

RUN pip install flask
RUN pip install flask_restful
RUN pip install pandas

CMD ["python3","./akyg.py"]
