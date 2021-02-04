FROM python:3.8.7


ADD . /usr/src/app
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
WORKDIR $APP_HOME

# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt
COPY requirements.txt ./
# Copy the project source code from the local host to the filesystem of the container at the working directory.
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
			python-dev python-pip python-setuptools \
			libffi-dev libxml2-dev libxslt1-dev \
			libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev \
			liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

# Add the dependencies to the container and install the python dependencies
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN pip install Pillow

# Expose web GUI
EXPOSE 6800

COPY . .

CMD [ "python3", "./go-spider.py" ]
