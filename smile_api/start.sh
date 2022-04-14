#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

uvicorn --host 0.0.0.0 app.main:app
