build:
	docker-compose build

up:
	docker-compose up -d

import:
	docker-compose exec neo4j cypher-shell -f=foodmart-import.cyp

console:
	docker-compose run base bash

down:
	docker-compose down

list-containers:
	docker ps