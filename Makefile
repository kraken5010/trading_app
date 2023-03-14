up:
	uvicorn main:app --reload

db:
	docker run -p 5434:5432 --name pg_trading -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:13.3

db-test:
	docker run -p 6000:5432 --name pg_trading_test -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:13.4

celery run:
	celery -A tasks.tasks:celery worker --loglevel=INFO

celery web interface:
	celery -A tasks.tasks:celery flower
