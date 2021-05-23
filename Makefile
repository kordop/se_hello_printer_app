USERNAME=kordop
SERVICE_NAME=hello-world-printer
DOCKER_IMG_NAME=$(SERVICE_NAME)
DOCKER_HUB_DEST=$(USERNAME)/$(SERVICE_NAME)
.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
lint:
	flake8 hello_world test
test:
	pytest
run:
	python main.py
docker_build:
	docker build -t ${SERVICE_NAME} .

docker_run: docker_build
	docker run \
	--name ${DOCKER_IMG_NAME}-dev \
	-p 5000:5000 \
	-d ${SERVICE_NAME}

docker_push:
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer ${DOCKER_HUB_DEST}:${TRAVIS_TAG}; \
	docker push ${DOCKER_HUB_DEST}:${TRAVIS_TAG}; \
	docker logout; 
	
test_smoke:
	curl --fail 127.0.0.1:5000