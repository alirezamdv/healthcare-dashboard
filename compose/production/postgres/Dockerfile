FROM postgres:12.3
ENV POSTGISV 2.5
COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  postgresql-$PG_MAJOR-postgis-$POSTGISV \
  postgresql-$PG_MAJOR-postgis-$POSTGISV-scripts \
  postgresql-$PG_MAJOR-pgrouting \
  postgresql-$PG_MAJOR-pgrouting-scripts \
  postgresql-server-dev-$PG_MAJOR \
  && apt-get purge -y --auto-remove postgresql-server-dev-$PG_MAJOR make unzip


# set time zone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./compose/production/postgres/maintenance/initdb-postgis.sh /docker-entrypoint-initdb.d/init.sh
