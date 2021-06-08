
CREATE_SCHEMA_STG = """
CREATE SCHEMA IF NOT EXISTS analytics;
"""

DROP_COVID_CASES_LAND = """
DROP TABLE IF EXISTS analytics.covid_cases;
"""

CREATE_COVID_CASES_LAND = """
CREATE TABLE analytics.covid_cases (
	Sno varchar(25),
	Date varchar(25),
	Time varchar(25),
	State_UnionTerritory varchar(50),
	ConfirmedIndianNational varchar(25),
	ConfirmedForeignNational varchar(25),
	Cured int,
	Deaths int,
	Confirmed int
);
"""

DROP_STATEWISE_TESTING_LAND = """
DROP TABLE IF EXISTS analytics.state_tests;
"""

CREATE_STATEWISE_TESTING_LAND = """
CREATE TABLE analytics.state_tests (
	Date varchar(25) NOT NULL,
	State varchar(50),
	TotalSamples varchar(25),
	Negative int,
	Positive int
);
"""


CREATE_COVID_CASES_STAGE = """
# CREATE TABLE IF NOT EXISTS analytics.covid_cases_crtd (
# 	test_date varchar(256) NOT NULL,
# 	location varchar(256),
# 	lattitude numeric(18,0),
# 	longitude numeric(18,0)
# );
"""

COVID_STATEWISE_TESTING_STAGE = """
# CREATE TABLE IF NOT EXISTS analytics.state_tests_crtd (
# 	artistid varchar(256) NOT NULL,
# 	name varchar(256),
# 	location varchar(256),
# 	lattitude numeric(18,0),
# 	longitude numeric(18,0)
# );
"""

COVID_STATEWISE_TESTING_DMART = """
# CREATE TABLE IF NOT EXISTS analytics.state_tests_crtd (
# 	artistid varchar(256) NOT NULL,
# 	name varchar(256),
# 	location varchar(256),
# 	lattitude numeric(18,0),
# 	longitude numeric(18,0)
# );
"""

create_schemas = [CREATE_SCHEMA_STG]
create_landing_tables = [DROP_COVID_CASES_LAND, CREATE_COVID_CASES_LAND,
                         DROP_STATEWISE_TESTING_LAND, CREATE_STATEWISE_TESTING_LAND]

