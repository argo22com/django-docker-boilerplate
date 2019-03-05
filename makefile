image = project:latest
run-dev:
	docker-compose up --build -d

cli:
	docker-compose exec app sh

build:
	docker build -t $(image) -f .docker/app/Dockerfile .

push:
	docker push $(image)
