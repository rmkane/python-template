# Python Template

Here is an example module called `pycli` that creates a CLI executable.

## Docker

- Build: `docker build -t pycli-dev .`
- Run: `docker run -it --rm -v ${PWD}:/app --name pycli-dev-container pycli-dev`
- Execute: `docker exec -it pycli-dev-container bash`
- Stop Container: `docker stop pycli-dev-container`
- List Images: `docker images -f reference=pycli-dev`
- List Containers: `docker ps -f name=pycli-dev-container`
- Prune Images: `docker images --filter=reference='pycli-dev' --format "{{.ID}}" | xargs docker rmi`
- Prune Containers: `docker ps -a --filter=name='pycli-dev-container' --format "{{.ID}}" | xargs docker rm`
