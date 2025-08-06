# Start from the Codespaces default image
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install required system packages for OpenCV
USER root
RUN apt-get update && apt-get install -y libgl1-mesa-glx

USER vscode
