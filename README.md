# Docker Scrapyd Scrapy Crawler - Mailan-Spider App

This repository is a spider Python application that can be "Dockerized".
It comes with a step-by-step guide on "Dockerizing" a Python application in Mac OS X. You will learn about Scrapy, Scrapd, Docker, and Boot2Docker.
The mailan-spider app will be distributed as a docker image.


## Quick Start

Assuming you have docker installed and configured, run this command to download the image and launch a new container running the spider crawler.
```bash
$ git clone https://github.com/saeedsaberi/Dockerfile.git

```bash

This will download the repo. now we should build the image and run it:

```bash
$ docker build -t crawler_test -f Dockerfile ./


$ docker run -it -p 8080:8080 ssaberi/ssaberi-spider
```

Once the image is downloaded and your container is running, run this command to schedule a spider crawl job
* This API call on the spider server will return a jobid
* Make sure to replace the ip address with the IP address of your Docker Daemon (e.g. boot2docker ip)
* You can pass in multiple URIs to the start_urls in this string format (comma separated): start_urls="http://www.docker.com,http://www.google.com"
```bash
$ curl http://192.168.59.103:6800/schedule.json -d start_urls="[http://www.docker.com,http://www.google.com,http://www.python.org]"
{"status": "ok", "jobid": "f0bda666e72111e4b7290242ac110002"}
```

Once the job is complete, to see the list of crawled images, run this command:
```bash
$ curl http://192.168.59.103:6800/items/mailan/mailan/f0bda666e72111e4b7290242ac110002.jl
```


you can schadule the crawler using the following command:

```bash

curl http://192.168.59.103:800/schedule.json -d project=spider -d spider=ssaberi -d start_urls="http://www.docker.com,http://www.google.com" -d threads=1 -d o=output.json

```

* Replace f0bda666e72111e4b7290242ac110002 with the "jobid" that is returned form the curl
* You can also to your web browser for the web ui for monitoring
   * Go to http://192.168.59.103:6800/
   * Go to http://192.168.59.103:6800/jobs
   * Make sure to replace the ip address with the IP address of your Docker Daemon (e.g. boot2docker ip)



## Basic Terminology

What is ... ?

* Scrapy
 * a framework that allows you to easily crawl web pages and extract desired information.
* Scrapyd
 * an application that allows you to manage your spiders.
 * Because Scrapyd lets you deploy your spider projects via a JSON api, you can run scrapy on a different machine than the one you are running.
 * Lets you schedule your crawls, and even comes with a web UI to see all crawls and data responses.
* Docker
 * provides a way for almost any application to run securely in an isolated container.
 The isolation of a container allows you to run many instances of your application simultaneously and on many different platforms easily.
  * Main Docker Parts
    * docker daemon: used to manage docker containers on the host it runs
    * docker CLI: used to command and communicate with the docker daemon
    * docker image index: a repository (public or private) for docker images
  * Main Docker Elements
    * docker containers: directories containing EVERYTHING (OS, server daemons, your application)
    * docker images: snapshots of containers or base OS images - images are just templates for docker containers!
    * Dockerfiles: scripts automating the building process of images


