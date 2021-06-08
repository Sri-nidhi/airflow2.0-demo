with curated as (
    select
    *
    from
    {{ ref('covid_cases_stage') }} a
    join
    {{ ref('state_tests_stage') }} b
    on
    a.states = b.state
    and
    a.date_recorded = b.date_record
)

select * from curated