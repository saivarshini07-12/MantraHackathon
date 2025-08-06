# Start from the official Python image
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install OpenCV dependencies
USER root
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Switch back to the vscode user
USER vscode
