 
ifdef OS
	docker_build = docker compose up -d --build
	docker_down = docker compose down
else
	docker_build = sudo docker compose up -d --build
	docker_down = sudo docker compose down
endif

build:
	$(docker_build) 
	

down:
	$(docker_down)

logs:
	sudo docker compose logs

web:
	sudo docker compose build web
	sudo docker compose up -d web
 