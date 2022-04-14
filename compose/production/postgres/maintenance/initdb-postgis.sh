#!/bin/sh

set -e

# Perform all actions as $POSTGRES_USER
psql postgres -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
ALTER SYSTEM SET max_connections = '150';
ALTER SYSTEM SET shared_buffers = '1GB';
ALTER SYSTEM SET effective_cache_size = '3GB';
ALTER SYSTEM SET maintenance_work_mem = '256MB';
ALTER SYSTEM SET max_worker_processes = '2';
ALTER SYSTEM SET max_parallel_workers_per_gather = '1';
ALTER SYSTEM SET max_parallel_workers = '2';
create extension postgis;
EOSQL


