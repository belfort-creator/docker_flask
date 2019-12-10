FROM rcarmo/ubuntu-python:3.7-onbuild-amd64
# for a flask server
EXPOSE 5000
EXPOSE 80
COPY . /
WORKDIR /
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]