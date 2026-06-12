# SQL Questions
# Use SQLite-compatible SQL unless your instructor specifies another database.
# Q1. Data exploration
# Show the first 10 records from the main fact table.

Select * from main_fact_table_5000_rows limit 10;

# Q2. Data validation
# Confirm that the main fact table contains exactly 5,000 rows.

Select count(*) from main_fact_table_5000_rows;

# Q3. DISTINCT
# List every distinct delivery_status in the fact table.

Select distinct(delivery_status) from main_fact_table_5000_rows;

# Q4. ORDER BY / LIMIT
# Show the 15 largest records by disbursed_amount_usd.

Select disbursed_amount_usd as 15_largest_records
from main_fact_table_5000_rows
order by disbursed_amount_usd desc limit 15;

# Q5. AND / OR
# Find 2025 records that are Delayed or In Progress and have High or Critical risk.

SELECT *
FROM main_fact_table_5000_rows
WHERE fiscal_year = 2025
AND (delivery_status = 'Delayed' OR delivery_status = 'In Progress')
AND (risk_level = 'High' OR risk_level = 'Critical');

# Q6. BETWEEN / IN
# Find Health and Education program records reported in the first half of 2024.

SELECT *
FROM main_fact_table_5000_rows
WHERE program_id IN (203, 204)
AND STR_TO_DATE(reporting_month, '%d-%m-%Y')
BETWEEN '2024-01-01' AND '2024-06-30';

# Q7. LIKE
# Find 2025 Food Security project records using the project_code pattern.

Select *
from main_fact_table_5000_rows
where fiscal_year = 2025
and project_code like "FOOD%";

# Q8. COUNT
# Count how many records are marked Completed.

Select count(*) as completed_delivery
from main_fact_table_5000_rows
where delivery_status = "completed";

# Q9. SUM / AVG
# Calculate total allocated budget, total disbursed amount, and average disbursed amount for completed records.

Select sum(allocated_budget_USD) as total_allocated_budget,
sum(disbursed_amount_usd) as total_disbursed_amount,
avg(disbursed_amount_usd) as avg_disbursed_amount
from main_fact_table_5000_rows
where delivery_status = 'completed';

# Q10. MIN / MAX / AVG
# Find the minimum, maximum, and average reporting lag days for all records.

select min(reporting_lag_days) as minimum_reporting_lag_day,
max(reporting_lag_days) as maximum_reporting_lag_day,
avg(reporting_lag_days) as average_reporting_lag_day
from main_fact_table_5000_rows;

# Q11. GROUP BY
# Show total disbursement by fiscal year.

Select fiscal_year, sum(disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows
group by fiscal_year
order by fiscal_year desc;

# Q12. GROUP BY
# Show record count and total disbursement by delivery_status.

Select delivery_status, count(*) as record_count,
sum(disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows
group by delivery_status;

# Q13. GROUP BY
# Show total beneficiaries targeted and reached by program_id.

Select program_id, sum(beneficiaries_targeted) as total_beneficiaries_targeted
from main_fact_table_5000_rows
group by program_id
order by program_id;

# Q14. HAVING
# Find country_id groups with total disbursement above 20,000,000 USD.

Select country_id, sum(disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows
group by country_id having total_disbursed_amount > 20000000;

# Q15. INNER JOIN
# List high-risk records with country name and income group.

Select c.country_id, c.country_name, m.risk_level, c.income_group, m.delivery_status
from dimension_countries c inner join main_fact_table_5000_rows m
on c.country_id = m.country_id
where risk_level = 'high';

# Q16. INNER JOIN
# Show total disbursement by SDG goal and program area.

Select p.program_id, p.program_area, p.sdg_goal,
sum(m.disbursed_amount_usd) as total_disbursed_amount
from dimension_programs p inner join main_fact_table_5000_rows m
on p.program_id = m.program_id
group by p.program_id, p.program_area, p.sdg_goal;

# Q17. Multi-table JOIN
# Show total disbursement by UN region.

Select r.region_name, Sum(m.disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows m join dimension_countries c
on m.country_id = c.country_id join dimension_regions r
on r.region_id = c.region_id
group by region_name;

# Q18. JOIN to funding sources
# Show total disbursement by funding source type.

Select f.funding_source_name, sum(m.disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows m join dimension_funding_sources f
on m.funding_source_id = f.funding_source_id
group by f.funding_source_name;

# Q19. JOIN + GROUP BY
# Show completed-record count and disbursement by income group and program area.

Select p.program_area, c.income_group, count(*) as completed_record,
sum(m.disbursed_amount_usd) as total_disbursed_amount
from main_fact_table_5000_rows m join dimension_programs p
on m.program_id = p.program_id
join dimension_countries c on m.country_id = c.country_id
where m.delivery_status = 'completed'
group by p.program_area, c.income_group;

# Q20. LEFT JOIN
# Show all countries and their fact-record count, including countries with zero records.

Select r.region_name, c.country_name, COUNT(m.country_id) AS fact_record_count
FROM dimension_countries c LEFT JOIN dimension_regions r
ON c.region_id = r.region_id LEFT JOIN main_fact_table_5000_rows m
ON c.country_id = m.country_id
GROUP BY r.region_name, c.country_id, c.country_name
ORDER BY r.region_name, c.country_name;

# Q21. LEFT JOIN
# Show all programs and the count of delayed records for each program.

SELECT p.program_name, COUNT(m.program_id) AS delayed_record_count
FROM dimension_programs p LEFT JOIN main_fact_table_5000_rows m
ON p.program_id = m.program_id AND m.delivery_status = 'Delayed'
GROUP BY p.program_id, p.program_name
ORDER BY p.program_name;

# Q22. JOIN-based KPI
# Build a region x program-area KPI table with records, allocation, disbursement, and beneficiary delivery rate.

SELECT r.region_name, p.program_area, COUNT(m.fact_id) AS total_records,
SUM(m.allocated_budget_usd) AS total_allocation, SUM(m.disbursed_amount_usd) AS total_disbursement,
ROUND((SUM(m.allocated_budget_usd) / NULLIF(SUM(m.beneficiaries_targeted), 0)) * 100, 2) AS beneficiary_delivery_rate
FROM main_fact_table_5000_rows m
JOIN dimension_countries c ON m.country_id = c.country_id
JOIN dimension_regions r ON c.region_id = r.region_id
JOIN dimension_programs p ON m.program_id = p.program_id
GROUP BY r.region_name, p.program_area
ORDER BY r.region_name, p.program_area;

# Q23. JOIN-based KPI
# Compare funding-source types by disbursement ratio and beneficiary delivery rate.

SELECT fs.source_type, COUNT(*) AS total_records, SUM(f.allocated_budget_usd) AS total_allocation,
SUM(f.disbursed_amount_usd) AS total_disbursement,
ROUND((SUM(f.disbursed_amount_usd) /
        NULLIF(SUM(f.allocated_budget_usd), 0)) * 100,2) AS disbursement_ratio,

ROUND((SUM(f.beneficiaries_reached) /
        NULLIF(SUM(f.beneficiaries_targeted), 0)) * 100,2) AS beneficiary_delivery_rate
FROM main_fact_table_5000_rows f
JOIN dimension_funding_sources fs ON f.funding_source_id = fs.funding_source_id
GROUP BY fs.source_type
ORDER BY disbursement_ratio DESC;

# Q24. HAVING with JOINs
# Find program areas with disbursement above 40,000,000 USD but beneficiary delivery rate below 0.65.

SELECT p.program_area, SUM(f.disbursed_amount_usd) AS total_disbursement,
ROUND(SUM(f.beneficiaries_reached) / NULLIF(SUM(f.beneficiaries_targeted), 0),2)
AS beneficiary_delivery_rate
FROM main_fact_table_5000_rows f
JOIN dimension_programs p ON f.program_id = p.program_id
GROUP BY p.program_area
HAVING SUM(f.disbursed_amount_usd) > 40000000
AND (SUM(f.beneficiaries_reached) / NULLIF(SUM(f.beneficiaries_targeted), 0)) < 0.65
ORDER BY total_disbursement DESC;

# Q25. Safe join audit
# Check whether joining the main fact table to all one-row-per-key dimension tables changes the row count.

SELECT (SELECT COUNT(*)
FROM main_fact_table_5000_rows) AS original_row_count,
COUNT(*) AS joined_row_count
FROM main_fact_table_5000_rows f
JOIN dimension_countries c ON f.country_id = c.country_id
JOIN dimension_regions r ON c.region_id = r.region_id
JOIN dimension_programs p ON f.program_id = p.program_id
JOIN dimension_funding_sources fs ON f.funding_source_id = fs.funding_source_id;


# Q26. Data quality
# Count missing beneficiaries_reached by delivery_status.

SELECT delivery_status,
COUNT(*) AS missing_reached_records
FROM main_fact_table_5000_rows
WHERE data_quality_flag = 'MISSING_BENEFICIARIES'
GROUP BY delivery_status
ORDER BY missing_reached_records DESC;

# Q27. Data quality
# Find records where disbursed_amount_usd is greater than allocated_budget_usd and quantify the excess.

SELECT fact_id, country_id, program_id, funding_source_id, allocated_budget_usd,
disbursed_amount_usd, (disbursed_amount_usd - allocated_budget_usd) AS excess_amount_usd
FROM main_fact_table_5000_rows
WHERE disbursed_amount_usd > allocated_budget_usd
ORDER BY excess_amount_usd DESC;

# Q28. Data quality
# Summarize data_quality_flag frequency and average reporting lag.

SELECT data_quality_flag, COUNT(*) AS flag_frequency,
ROUND(AVG(reporting_lag_days), 2) AS avg_reporting_lag
FROM main_fact_table_5000_rows
GROUP BY data_quality_flag
ORDER BY flag_frequency DESC;

# Q29. Business insight query
# Identify high-value region-program combinations with low delivery rate for management attention.

SELECT r.region_name, p.program_area,
ROUND(SUM(f.disbursed_amount_usd), 2) AS disbursed_usd,
ROUND(SUM(f.beneficiaries_reached) / NULLIF(SUM(f.beneficiaries_targeted), 0),4)
AS beneficiary_delivery_rate
FROM main_fact_table_5000_rows f
JOIN dimension_countries c
ON f.country_id = c.country_id
JOIN dimension_regions r
ON c.region_id = r.region_id
JOIN dimension_programs p
ON f.program_id = p.program_id
GROUP BY r.region_name, p.program_area
HAVING SUM(f.disbursed_amount_usd) > 30000000
AND (SUM(f.beneficiaries_reached) / NULLIF(SUM(f.beneficiaries_targeted), 0)) < 0.65
ORDER BY disbursed_usd DESC;
