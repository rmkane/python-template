# Python Template

Here is an example module called `pycli` that creates a CLI executable.

## Docker

### Dev

- Build: `docker build -f Dockerfile.dev -t pycli-dev .`
- Run: `docker run -it --rm -v ${PWD}:/app --name pycli-dev-container pycli-dev`
- Execute: `docker exec -it pycli-dev-container bash`
- Stop Container: `docker stop pycli-dev-container`
- List Images: `docker images -f reference=pycli-dev`
- List Containers: `docker ps -f name=pycli-dev-container`
- Prune Images: `docker images --filter=reference='pycli-dev' --format "{{.ID}}" | xargs docker rmi`
- Prune Containers: `docker ps -a --filter=name='pycli-dev-container' --format "{{.ID}}" | xargs docker rm`

### Build

To get the executable (18MB) out the container, run:

```shell
docker build -f Dockerfile.python -t rocky8-python311 .
docker build -f Dockerfile.build -t pycli-build .
docker run --rm -v "$(pwd)/dist:/app/dist" pycli-build
```

The executable will be located here: `dist/pycli`

- Build: `docker build -f Dockerfile.build -t pycli-build .`
- Run: `docker run -dit --name pycli-build-container pycli-build /bin/bash`
- Execute: `docker exec -it pycli-build-container /bin/bash`
- Stop Container: `docker stop pycli-build-container`
- Remove Container: `docker rm pycli-build-container`
