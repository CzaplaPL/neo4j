build:
	docker-compose build

console:
	docker-compose run base bash

down:
	docker-compose down

list-containers:
	docker ps