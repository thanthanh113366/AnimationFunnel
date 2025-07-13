#!/bin/bash

# Script to compile, render and present Manim slides
# Usage: ./run_slides.sh [scene_name] [file_name]

# Default values
SCENE_NAME=${1:-"Example"}
FILE_NAME=${2:-"main.py"}

rm -rf slides/
mkdir -p slides/

uv run manim-slides render "$FILE_NAME" "$SCENE_NAME"

uv run manim-slides convert "$SCENE_NAME" "slides/${SCENE_NAME}.html"


