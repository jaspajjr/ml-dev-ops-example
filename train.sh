docker build -t ml-dev-ops-training -f Dockerfile.training . && docker run -it -v$(pwd):/results ml-dev-ops-training