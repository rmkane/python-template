@echo off

:: Variables
set APP_NAME=pycli

set VENV_DIR=.venv
set VENV_ACTIVATE=%VENV_DIR%\Scripts\activate
set VENV_DEACTIVATE=%VENV_DIR%\Scripts\deactivate

set SRC_DIR=src
set TEST_DIR=tests

set TARGET_DIRS=build dist %APP_NAME%.egg-info
set CACHE_DIRS=.pytest_cache .mypy_cache

:: Create virtual environment
if "%1" == "setup" (
    python -m venv %VENV_DIR%
    call %VENV_ACTIVATE%
    python -m pip install --upgrade pip build
    goto :eof
)

:: Install development dependencies
if "%1" == "develop" (
    call %VENV_ACTIVATE%
    python -m pip install -e .[dev]
    goto :eof
)

:: Install the project
if "%1" == "install" (
    call %VENV_ACTIVATE%
    python -m pip install .
    goto :eof
)

:: Unnstall the project
if "%1" == "uninstall" (
    call %VENV_ACTIVATE%
    python -m pip uninstall -y %APP_NAME%
    goto :eof
)

:: Build the project
if "%1" == "build" (
    call %VENV_ACTIVATE%
    python -m build
    python -m PyInstaller --name %APP_NAME% %SRC_DIR%\%APP_NAME%\cli.py
    goto :eof
)

:: Run tests
if "%1" == "test" (
    call %VENV_ACTIVATE%
    python -m pytest %TEST_DIR%
    goto :eof
)

:: Format the code
if "%1" == "format" (
    call %VENV_ACTIVATE%
    python -m isort %SRC_DIR%
    python -m black %SRC_DIR%
    goto :eof
)

:: Lint the code
if "%1" == "lint" (
    call %VENV_ACTIVATE%
    python -m black --check %SRC_DIR%
    python -m mypy %SRC_DIR%
    goto :eof
)

:: Clean the project
if "%1" == "clean" (
    echo Cleaning all generated files...
    for %%d in (%TARGET_DIRS%) do (
        rmdir /s /q %%d 2>nul
    )
    for %%d in (%CACHE_DIRS%) do (
        rmdir /s /q %%d 2>nul
    )
    for /d /r %SRC_DIR% %%d in (__pycache__) do (
        @if exist "%%d" rmdir /s /q "%%d" 2>nul
    )
    goto :eof
)

:: Clean the project and remove the virtual environment
if "%1" == "clean-all" (
    call "%~f0" clean
    echo Deactivating the virtual environment...
    call %VENV_DEACTIVATE%
    echo Cleaning the virtual environment...
    rmdir /s /q %VENV_DIR% 2>nul
    goto :eof
)

:: Activate the virtual environment
if "%1" == "activate" (
    echo To activate the virtual environment, run:
    echo %VENV_ACTIVATE%
    goto :eof
)

:: Deactivate the virtual environment
if "%1" == "deactivate" (
    echo Deactivating the virtual environment...
    call %VENV_DEACTIVATE%
    goto :eof
)

goto :eof
