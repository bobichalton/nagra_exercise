#!/bin/bash
docker build . -t roberto/my-app:0.1.0
docker image push roberto/my-app:0.1.0