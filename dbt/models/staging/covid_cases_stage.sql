{{
  config(
    post_hook=after_commit("delete from {{ source('covid_raw_data', 'covid_cases') }}")
  )
}}

with source as (
  select
    *
  from {{ source('covid_raw_data', 'covid_cases') }} where state_unionterritory is not null
),
covid_source as (
  select
    cast(date as date) as date_recorded,
    time as time_recorded,
    state_unionterritory as states,
    cured,
    deaths,
    confirmed
  from source
)

select * from covid_source