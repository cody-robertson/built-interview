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

migrate:
	docker compose run api alembic upgrade head

revert-migrations:
	docker compose run api alembic downgrade base

makemigrations:
	docker compose run api alembic revision --autogenerate -m "$(msg)"

init_kinesis:
	docker exec localstack_main awslocal kinesis create-stream --stream-name samplestream --shard-count 1