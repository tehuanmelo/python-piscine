IMAGE_NAME = python-image310
CONTAINER_NAME = python-container310

build:
	docker build -t $(IMAGE_NAME) .

force:
	docker build --no-cache -t $(IMAGE_NAME) .

run:
	docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME) bash

python:
	docker run -it --rm $(IMAGE_NAME) python

shell:
	docker run -it --rm -v "$$(pwd):/home/tehuan" $(IMAGE_NAME) bash