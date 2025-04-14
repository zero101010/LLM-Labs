#!/bin/bash
set -e

ollama create zero101010/mario-model -f ./Modelfile

# ollama show --modelfile llama3.2:3b >> ./ModelfileLamma3.2

ollama run zero101010/mario-model