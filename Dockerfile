FROM python:3.4-slim
ADD ./pyton /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["tail", "-f", "/dev/null"]
