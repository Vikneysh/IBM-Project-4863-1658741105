FROM python:3.6
# switch working directory
WORKDIR /myapp

# install the dependencies and packages in the requirements file
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install flask
RUN pip install ibm_db
# copy every content from the local file to the image
COPY . /myapp
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["app.py" ]