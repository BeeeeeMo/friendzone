# Install pdm
sudo apt-get install python3-venv

curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -

## install dependencies
sudo apt install python3-dev libpq-dev
pdm install

## Build docker images
docker-compose build