
CREATE_SCHEMA_STG = """
CREATE SCHEMA IF NOT EXISTS staging;
"""
CREATE_SCHEMA_CUR = """
CREATE SCHEMA IF NOT EXISTS curated;
"""
CREATE_SCHEMA_DM = """
CREATE SCHEMA IF NOT EXISTS datamart;
"""



CREATE_COVID_CASES_STAGING = """
CREATE TABLE IF NOT EXISTS staging.covid_cases (
	test_date varchar(256) NOT NULL,
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);
"""

COVID_STATEWISE_TESTING_STAGING = """
CREATE TABLE IF NOT EXISTS staging.state_tests (
	artistid varchar(256) NOT NULL,
	name varchar(256),
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);
"""


CREATE_COVID_CASES_CURATED = """
CREATE TABLE IF NOT EXISTS curated.covid_cases (
	test_date varchar(256) NOT NULL,
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);
"""

COVID_STATEWISE_TESTING_CURATED = """
CREATE TABLE IF NOT EXISTS curated.state_tests (
	artistid varchar(256) NOT NULL,
	name varchar(256),
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);
"""

COVID_STATEWISE_TESTING_DATAMART = """
CREATE TABLE IF NOT EXISTS curated.state_tests (
	artistid varchar(256) NOT NULL,
	name varchar(256),
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);
"""

create_schemas = [CREATE_SCHEMA_STG, CREATE_SCHEMA_CUR, CREATE_SCHEMA_DM]
create_staging_tables = [CREATE_COVID_CASES_STAGING, COVID_STATEWISE_TESTING_STAGING]
create_curated_tables = [CREATE_COVID_CASES_CURATED, COVID_STATEWISE_TESTING_CURATED]
create_datamart_tables = [COVID_STATEWISE_TESTING_DATAMART]