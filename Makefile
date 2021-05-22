USERNAME=kordop
TAG=$(USERNAME)/hello-world-printer
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
	docker build -t hello-world-printer .

docker_run: docker_build
	docker run \
	--name hello-world-printer-dev \
	-p 5000:5000 \
	-d hello-world-printer

docker_push:
- |
if [ -z "${TRAVIS_TAG}" ]; then
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; 
	docker tag hello-world-printer ${TAG}:${TRAVIS_TAG};
	docker push ${TAG}:${TRAVIS_TAG};
	docker logout;
fi;