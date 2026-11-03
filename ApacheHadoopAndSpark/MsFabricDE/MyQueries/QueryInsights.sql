SELECT start_time, login_name, command
FROM queryinsights.exec_requests_history 
WHERE start_time >= DATEADD(MINUTE, -60, GETUTCDATE());

SELECT last_run_command, number_of_runs, median_total_elapsed_time_ms, last_run_start_time
FROM queryinsights.long_running_queries
WHERE number_of_runs > 1
ORDER BY median_total_elapsed_time_ms DESC;


SELECT last_run_command, number_of_runs, number_of_successful_runs, number_of_failed_runs
FROM queryinsights.frequently_run_queries
ORDER BY number_of_runs DESC;
