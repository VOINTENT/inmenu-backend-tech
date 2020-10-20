DROP SEQUENCE IF EXISTS log_request_seq CASCADE;

CREATE SEQUENCE log_request_seq START 1;

DROP TABLE IF EXISTS log_request CASCADE;

CREATE TABLE log_request(
    id BIGINT NOT NULL DEFAULT nextval('log_request_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    completion_time REAL,
    method TEXT,
    url TEXT,
    ip TEXT,
    status INTEGER,
    error_msg TEXT
);

-- -----------------------------------------------------------------------------