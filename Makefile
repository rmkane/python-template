APP_NAME = pycli
VENV_DIR = .venv
ACTIVATE_CMD = . $(VENV_DIR)/bin/activate
SRC_DIR = src
TEST_DIR = tests
TARGET_DIRS = build dist $(APP_NAME).egg-info
CACHE_DIRS = .pytest_cache .mypy_cache

.PHONY: help setup develop install uninstall build test format lint clean clean-all venv deactivate

help: # Show this help message
	@awk 'BEGIN {FS = ":.*?#"} /^[a-zA-Z_-]+:.*?#/ {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: # Create virtual environment and install pip and build
	python -m venv $(VENV_DIR)
	$(ACTIVATE_CMD) && pip install --upgrade pip build

develop: # Install development dependencies
	$(ACTIVATE_CMD) && pip install -e .[dev]

install: # Install the project
	$(ACTIVATE_CMD) && pip install .

uninstall: # Uninstall the project
	$(ACTIVATE_CMD) && pip uninstall -y $(APP_NAME)

build: # Build the project
	$(ACTIVATE_CMD) && python -m build
	$(ACTIVATE_CMD) && pyinstaller --name $(APP_NAME) $(SRC_DIR)/$(APP_NAME)/cli.py

test: # Run tests
	$(ACTIVATE_CMD) && pytest $(TEST_DIR)

format: # Format the code
	$(ACTIVATE_CMD) && isort $(SRC_DIR)
	$(ACTIVATE_CMD) && black $(SRC_DIR)

lint: # Lint the code
	$(ACTIVATE_CMD) && black --check $(SRC_DIR)
	$(ACTIVATE_CMD) && mypy $(SRC_DIR)

clean: # Clean all generated files
	@echo Cleaning all generated files...
	@for dir in $(TARGET_DIRS); do \
		rm -rf $$dir; \
	done
	@for dir in $(CACHE_DIRS); do \
		rm -rf $$dir; \
	done
	@find $(SRC_DIR) -type d -name "__pycache__" -exec rm -rf {} +

clean-all: clean # Clean the project and remove the virtual environment
	@echo Deactivating the virtual environment...
	@$(ACTIVATE_CMD) && deactivate
	@echo Cleaning the virtual environment...
	@rm -rf $(VENV_DIR)

venv: # Show how to activate the virtual environment
	@echo To activate the virtual environment, run:
	@echo $(ACTIVATE_CMD)

deactivate: # Deactivate the virtual environment
	@echo Deactivating the virtual environment...
	@$(ACTIVATE_CMD) && deactivate
