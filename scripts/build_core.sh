#!/usr/bin/env bash
set -euo pipefail

# Build the core Java module with Maven.
# Assumes Maven (mvn) is on PATH and Java 17+ is installed.

mvn -f core/pom.xml package
