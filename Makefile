USERNAME=kordop
SERVICE_NAME=hello-world-printer
DOCKER_IMG_NAME=$(SERVICE_NAME)
DOCKER_HUB_DEST=$(USERNAME)/$(SERVICE_NAME)
DOCKER_LICENSE_NAME = license_finder
.PHONY: test

deps:
	pip3 install -r requirements.txt; \
	pip3 install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	pytest

run:
	python main.py

docker_build:
	docker build -t ${SERVICE_NAME} .
DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

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

docker_save:
	docker save ${DOCKER_IMG_NAME} > .docker_images/${DOCKER_IMG_NAME}.tar

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=hello_world --cov-report xml

test_xunit:
	PYTHONPATH=. py.test -s --cov=hello_world --cov-report xml --junit-xml=test_results.xml
#
#find_licenses: 
#	docker run -v $(DIR):/scan licensefinder/license_finder:6.13.0 bash -c "source ~/.profile && cd /scan && pip3 install -r requirements.txt  && license_finder report --python-version=3"

#docker run -it -v ${DIR}:/scan ${DOCKER_LICENSE_NAME} /bin/ash

#build_licenses:
#	docker build -f ${DIR}/license_finder/Dockerfile -t ${DOCKER_LICENSE_NAME} ${DIR}/license_finder