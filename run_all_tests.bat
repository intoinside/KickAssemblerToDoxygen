
coverage run ./test_converter.py
coverage report -m

if exist coverage.svg del coverage.svg
coverage-badge -o coverage.svg 
