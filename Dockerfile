FROM python

RUN mkdir -p /home/app

COPY ./app /home/app

ENV FLASK_DEBUG=True

RUN pip install -r /home/app/requirements.txt

ENTRYPOINT ["python"]

CMD ["/home/app/app.py"]