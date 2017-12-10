FROM python:rc-alpine3.6

WORKDIR twitter_fetch

COPY twitter_fetch /twitter_fetch/

RUN pip install elasticsearch &&\
    pip install tweepy 

CMD ["python","index.py"]