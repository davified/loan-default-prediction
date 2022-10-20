import os
import sys

# TODO: find a more elegant workaround than this (https://stackoverflow.com/a/59732673) for tests to find modules in src
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
