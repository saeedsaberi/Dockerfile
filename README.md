# Docker Scrapyd Scrapy Crawler - Mailan-Spider App

This repository is a spider Python application that can be "Dockerized".
It comes with a step-by-step guide on "Dockerizing" a Python application in Mac OS X. You will learn about Scrapy, Scrapd, Docker, and Boot2Docker.
The mailan-spider app will be distributed as a docker image.


## Quick Start

Assuming you have docker installed and configured, run this command to download the image and launch a new container running the spider crawler.
```bash
$ docker run -it -p 8080:8080 iammai/mailan-spider
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
* Boot2Docker
 * a lightweight Linux distribution made specifically to run Docker containers
 * Like many developers, I am on Mac OS X. Since Docker uses features only available to Linux, the machine must be running on a Linux kernel. Hence, Boot2docker VM (Virtual Machine) for Mac OS X solves our problem!




## Guide

This guide will walk you step-by-step on how to dockerize the mailan-spider application.
You will learn
* how to run your a mailan-spider crawl using Scrapy
* how to use Boot2Docker on your Mac OS X
* how to use Scrapyd to schedule crawls and manage them
* how to deploy your image to your DockerHub

1. Clone this repository

  ```bash
  $ git clone git@github.com/saeedsaberi/docker-crawler
  ```


    * To install  virtualenv
    ```bash
     $  docker build -t crawler_test -f Dockerfile ./
	 $  docker run crawler_test -p 8080:8080
    ```



2. You can test that your Scrapy installation works with the mailan-spider by running the crawler locally on your machine.
   Make sure you are on the level with scrapy.cfg.
   - This particular mailan-spider will go to http://www.docker.com and http://www.google.com and crawl for images on the page and one page link below the page
    * Installing Scrapy in your virtual environment
    ```bash
     (venv)$ cd docker-scrapy-crawler
     (venv)$ scrapy crawl ssaberi -o output.json -a start_urls=http://www.docker.com,http://www.google.com

    ```

 3.


    ```bash

	$	curl -X POST 'http://localhost:8080' -H "Content-Type: application/json"
		--data start_urls=http://www.docker.com,http://www.google.com

    ```
    ```bash

    $ curl -X GET http://localhost:8080/status/047500fa-37e3-4a80-a9fe-fdda1e6f1150
    ```
    ```bash

	$ curl -X GET http://localhost:8080/result/047500fa-37e3-4a80-a9fe-fdda1e6f1150
    ```
