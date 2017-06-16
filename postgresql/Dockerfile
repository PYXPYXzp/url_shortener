FROM postgres:latest

ENV PGDATA /var/lib/pgsql/data/

COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]