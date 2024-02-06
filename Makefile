ENV=local
include ./secrets/$(ENV)/.env

ifeq ($(ENV), prod)
	DOMAIN=$(BASE_DOMAIN)
else
	DOMAIN=$(ENV).$(BASE_DOMAIN)
endif

push_secrets:
	aws s3 sync ./secrets/$(ENV) s3://$(S3_BUCKET)/$(APP_NAME)/backend/$(ENV)

pull_secrets:
	aws s3 sync s3://$(S3_BUCKET)/$(APP_NAME)/backend/$(ENV) ./secrets/$(ENV)

use_secrets:
	cp ./secrets/$(ENV)/.env ./.

down:
	docker-compose down

build: use_secrets
	docker-compose build

up: build
	docker-compose up -d

unit_tests: up
	docker-compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/unit/

some_unit_tests: up
	docker-compose exec -T backend pytest -s ./tests/unit/$(TEST_PATH)

integration_tests: up
	 docker-compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/integration/

some_integration_tests: up
	docker-compose exec -T backend pytest -s ./tests/integration/$(TEST_PATH)

tests: up
	docker-compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/unit ./tests/integration

tag: build
	docker tag $(APP_NAME):latest $(APP_NAME):$(ENV)

deploy: tag
	docker save --output ./deploy/files/app $(APP_NAME):latest
	ansible-playbook -i deploy/inventory/$(ENV) deploy/tasks/notification.yml --extra-vars "domain=$(DOMAIN) slack_token=$(SLACK_TOKEN)"
	ansible-playbook -i deploy/inventory/$(ENV) deploy/tasks/deploy.yml --extra-vars "server_username=$(SERVER_USERNAME) domain=$(DOMAIN) slack_token=$(SLACK_TOKEN)"
	rm ./deploy/files/app

setup_infrastructure:
	ansible-playbook -i deploy/inventory/$(ENV) deploy/tasks/setup_infrastructure.yml --extra-vars "email=$(EMAIL) server_username=$(SERVER_USERNAME) domain=$(DOMAIN)"

configure_aws:
	aws configure set aws_access_key_id $(AWS_ACCESS_KEY_ID) && \
	aws configure set aws_secret_access_key $(AWS_SECRET_ACCESS_KEY)
