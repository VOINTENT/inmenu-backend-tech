DROP TABLE IF EXISTS test CASCADE;

CREATE TABLE test (
    id SMALLINT
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS language_seq_id CASCADE;

CREATE SEQUENCE language_seq_id START 1;

DROP TABLE IF EXISTS language CASCADE;

CREATE TABLE language (
    id SMALLINT PRIMARY KEY DEFAULT nextval('language_seq_id'),
    created_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    edited_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) NOT NULL,
    code_name varchar(10) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS account_status_seq CASCADE;

CREATE SEQUENCE account_status_seq START 1;

DROP TABLE IF EXISTS account_status CASCADE;

CREATE TABLE account_status (
    id SMALLINT PRIMARY KEY DEFAULT nextval('account_status_seq'),
    created_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    edited_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS account_main_id_seq CASCADE;

CREATE SEQUENCE account_main_id_seq START 1;

DROP TABLE IF EXISTS account_main CASCADE;

CREATE TABLE account_main(
    id INTEGER PRIMARY KEY DEFAULT nextval('account_main_id_seq'),
    created_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    edited_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    email VARCHAR(100) NOT NULL CONSTRAINT unique_account_email UNIQUE,
    name VARCHAR(100) NOT NULL,
    hash_password VARCHAR(300),
    balance INTEGER NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_confirmed BOOLEAN NOT NULL DEFAULT FALSE
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS account_session_id_seq CASCADE;

CREATE SEQUENCE account_session_id_seq START 1;

DROP TABLE IF EXISTS account_session CASCADE;

CREATE TABLE account_session(
    id BIGINT DEFAULT nextval('account_session_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    account_main_id INTEGER NOT NULL REFERENCES account_main(id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS auth_code_seq CASCADE;

CREATE SEQUENCE auth_code_seq START 1;

DROP TABLE IF EXISTS auth_code CASCADE;

CREATE TABLE auth_code(
    id BIGINT DEFAULT nextval('auth_code_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    account_main_id INTEGER UNIQUE NOT NULL REFERENCES account_main(id) ON DELETE CASCADE,
    code VARCHAR(6) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS currency_seq_id CASCADE;

CREATE SEQUENCE currency_seq_id START 1;

DROP TABLE IF EXISTS currency CASCADE;

CREATE TABLE currency (
    id SMALLINT PRIMARY KEY DEFAULT nextval('currency_seq_id'),
    created_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    edited_at TIMESTAMP with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) NOT NULL,
    short_name VARCHAR(5) NOT NULL,
    sign VARCHAR(5) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_type_id_seq CASCADE;

CREATE SEQUENCE place_type_id_seq START 1;

DROP TABLE IF EXISTS place_type CASCADE;

CREATE TABLE place_type(
    id BIGINT DEFAULT nextval('place_type_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS cuisine_type_id_seq CASCADE;

CREATE SEQUENCE cuisine_type_id_seq START 1;

DROP TABLE IF EXISTS cuisine_type CASCADE;

CREATE TABLE cuisine_type(
    id BIGINT DEFAULT nextval('cuisine_type_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS service_id_seq CASCADE;

CREATE SEQUENCE service_id_seq START 1;

DROP TABLE IF EXISTS service CASCADE;

CREATE TABLE service(
    id BIGINT DEFAULT nextval('service_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_main_id_seq CASCADE;

CREATE SEQUENCE place_main_id_seq START 1;

DROP TABLE IF EXISTS place_main CASCADE;

CREATE TABLE place_main(
    id INTEGER DEFAULT nextval('place_main_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    account_main_id INTEGER REFERENCES account_main(id) ON DELETE CASCADE,
    main_language SMALLINT REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50),
    login VARCHAR(50) CONSTRAINT unique_place_login UNIQUE,
    photo_link VARCHAR (500),
    description VARCHAR (2000),
    main_currency_id INTEGER REFERENCES currency(id) ON DELETE CASCADE,
    is_draft BOOLEAN NOT NULL,
    is_published BOOLEAN NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_place_type_id_seq CASCADE;

CREATE SEQUENCE place_place_type_id_seq START 1;

DROP TABLE IF EXISTS place_place_type CASCADE;

CREATE TABLE place_place_type(
    id INTEGER DEFAULT nextval('place_place_type_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER NOT NULL REFERENCES place_main(id) ON DELETE CASCADE,
    place_type_id INTEGER NOT NULL REFERENCES place_type(id) ON DELETE CASCADE,
    CONSTRAINT unique_place_place_type UNIQUE (place_main_id, place_type_id)
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_service_id_seq CASCADE;

CREATE SEQUENCE place_service_id_seq START 1;

DROP TABLE IF EXISTS place_service CASCADE;

CREATE TABLE place_service(
    id INTEGER DEFAULT nextval('place_service_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER NOT NULL REFERENCES place_main(id) ON DELETE CASCADE,
    service_id INTEGER NOT NULL REFERENCES service(id) ON DELETE CASCADE,
    CONSTRAINT unique_place_service UNIQUE (place_main_id, service_id)
);


-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_cuisine_type_id_seq CASCADE;

CREATE SEQUENCE place_cuisine_type_id_seq START 1;

DROP TABLE IF EXISTS place_cuisine_type CASCADE;

CREATE TABLE place_cuisine_type(
    id INTEGER DEFAULT nextval('place_cuisine_type_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER NOT NULL REFERENCES place_main(id) ON DELETE CASCADE,
    cuisine_type_id INTEGER NOT NULL REFERENCES cuisine_type(id) ON DELETE CASCADE,
    CONSTRAINT unique_place_cuisine_type UNIQUE (place_main_id, cuisine_type_id)
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_work_hours_id_seq CASCADE;

CREATE SEQUENCE place_work_hours_id_seq START 1;

DROP TABLE IF EXISTS place_work_hours CASCADE;

CREATE TABLE place_work_hours(
    id INTEGER DEFAULT nextval('place_work_hours_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER NOT NULL REFERENCES place_main(id) ON DELETE CASCADE,
    week_day VARCHAR(5) NOT NULL CONSTRAINT valid_week_day CHECK (week_day IN ('mo', 'tu', 'we', 'th', 'fr', 'sa', 'su')),
    time_start TIME,
    time_finish TIME,
    is_holiday BOOLEAN NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_location_id_seq CASCADE;

CREATE SEQUENCE place_location_id_seq START 1;

DROP TABLE IF EXISTS place_location CASCADE;

CREATE TABLE place_location(
    id INTEGER DEFAULT nextval('place_cuisine_type_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER REFERENCES place_main(id) ON DELETE CASCADE,
    full_location VARCHAR(500) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    coords POINT
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_contacts_id_seq CASCADE;

CREATE SEQUENCE place_contacts_id_seq START 1;

DROP TABLE IF EXISTS place_contacts CASCADE;

CREATE TABLE place_contacts(
    id INTEGER DEFAULT nextval('place_contacts_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER REFERENCES place_main(id) ON DELETE CASCADE,
    phone_number VARCHAR(12),
    email VARCHAR(100),
    site_link VARCHAR(200),
    vk_link VARCHAR(200),
    instagram_link VARCHAR(200),
    facebook_link VARCHAR(200)
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS menu_main_id_seq CASCADE;

CREATE SEQUENCE menu_main_id_seq START 1;

DROP TABLE IF EXISTS menu_main CASCADE;

CREATE TABLE menu_main(
    id INTEGER DEFAULT nextval('menu_main_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER REFERENCES place_main(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    photo_link VARCHAR (500)
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS menu_category_id_seq CASCADE;

CREATE SEQUENCE menu_category_id_seq START 1;

DROP TABLE IF EXISTS menu_category CASCADE;

CREATE TABLE menu_category(
    id INTEGER DEFAULT nextval('menu_category_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    menu_main_id INTEGER REFERENCES menu_main(id) ON DELETE CASCADE,
    name VARCHAR(64) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_account_role_id_seq CASCADE;

CREATE SEQUENCE place_account_role_id_seq START 1;

DROP TABLE IF EXISTS place_account_role CASCADE;

CREATE TABLE place_account_role(
    id INTEGER DEFAULT nextval('place_account_role_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_main_id INTEGER REFERENCES place_main(id) ON DELETE CASCADE,
    account_main_id INTEGER REFERENCES account_main(id) ON DELETE CASCADE,
    account_status_id SMALLINT REFERENCES account_status(id) ON DELETE CASCADE,
    UNIQUE (place_main_id, account_main_id)
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS measure_unit_id_seq CASCADE;

CREATE SEQUENCE measure_unit_id_seq START 1;

DROP TABLE IF EXISTS measure_unit CASCADE;

CREATE TABLE measure_unit(
    id INTEGER DEFAULT nextval('measure_unit_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(20) NOT NULL,
    short_name VARCHAR(10) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS dish_main_id_seq CASCADE;

CREATE SEQUENCE dish_main_id_seq START 1;

DROP TABLE IF EXISTS dish_main CASCADE;

CREATE TABLE dish_main(
    id INTEGER DEFAULT nextval('dish_main_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(100) NOT NULL,
    photo_link VARCHAR(500) NOT NULL,
    description VARCHAR(1000) NOT NULL,
    menu_main_id INTEGER NOT NULL REFERENCES menu_main(id) ON DELETE CASCADE,
    menu_category_id INTEGER NOT NULL REFERENCES menu_category(id) ON DELETE CASCADE,
    measure_unit_id INTEGER NOT NULL REFERENCES measure_unit(id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS dish_measure_id_seq CASCADE;

CREATE SEQUENCE dish_measure_id_seq START 1;

DROP TABLE IF EXISTS dish_measure CASCADE;

CREATE TABLE dish_measure(
    id INTEGER DEFAULT nextval('dish_measure_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    dish_main_id INTEGER NOT NULL REFERENCES dish_main(id) ON DELETE CASCADE,
    price_value INTEGER NOT NULL,
    measure_value INTEGER NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS cuisine_type_translate_id_seq CASCADE;

CREATE SEQUENCE cuisine_type_translate_id_seq START 1;

DROP TABLE IF EXISTS cuisine_type_translate CASCADE;

CREATE TABLE cuisine_type_translate(
    id INTEGER DEFAULT nextval('cuisine_type_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    cuisine_type_id INTEGER NOT NULL REFERENCES cuisine_type(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS place_type_translate_id_seq CASCADE;

CREATE SEQUENCE place_type_translate_id_seq START 1;

DROP TABLE IF EXISTS place_type_translate CASCADE;

CREATE TABLE place_type_translate(
    id INTEGER DEFAULT nextval('place_type_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    place_type_id INTEGER NOT NULL REFERENCES place_type(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS service_translate_id_seq CASCADE;

CREATE SEQUENCE service_translate_id_seq START 1;

DROP TABLE IF EXISTS service_translate CASCADE;

CREATE TABLE service_translate(
    id INTEGER DEFAULT nextval('service_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    service_id INTEGER NOT NULL REFERENCES place_type(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS currency_translate_id_seq CASCADE;

CREATE SEQUENCE currency_translate_id_seq START 1;

DROP TABLE IF EXISTS currency_translate CASCADE;

CREATE TABLE currency_translate(
    id INTEGER DEFAULT nextval('currency_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    currency_id INTEGER NOT NULL REFERENCES currency(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- -----------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS dish_measures_translate_id_seq CASCADE;

CREATE SEQUENCE dish_measures_translate_id_seq START 1;

DROP TABLE IF EXISTS dish_measures_translate CASCADE;

CREATE TABLE dish_measures_translate(
    id INTEGER DEFAULT nextval('currency_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    dish_measure_id INTEGER NOT NULL REFERENCES dish_measure(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- ------------------------------------------------------------------------------

DROP SEQUENCE IF EXISTS measure_unit_translate_id_seq CASCADE;

CREATE SEQUENCE measure_unit_translate_id_seq START 1;

DROP TABLE IF EXISTS measure_unit_translate CASCADE;

CREATE TABLE measure_unit_translate(
    id INTEGER DEFAULT nextval('currency_translate_id_seq') PRIMARY KEY,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    edited_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    measure_unit_id INTEGER NOT NULL REFERENCES measure_unit(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    short_name VARCHAR(50) NOT NULL
);