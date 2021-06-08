--{% set columns = ["date", "state", "negative", "positive", "totalsample"]  %}
{{
  config(
    post_hook=after_commit("delete from {{ source('covid_raw_data', 'state_tests') }}")
  )
}}

with source as (
  select
    *
  from {{ source('covid_raw_data', 'state_tests') }} where
  (
    date is not null and
    state is not null and
    negative is not null and
    positive is not null and
    totalsamples is not null

  )
),
covid_source as (
  select
    cast(date as date) as date_record,
    state,
    negative,
    positive,
    totalsamples
  from source
)

select * from covid_source