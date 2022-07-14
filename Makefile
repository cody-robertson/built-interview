start:
	docker compose up --build -d

stop:
	docker compose down

restart:
	docker compose restart

run:
	docker compose run api $(cmd)

format:
	docker compose run api black .
