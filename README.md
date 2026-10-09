# Openstead Python worker starter

A small Python process with graceful SIGTERM handling. Replace `process()` in
`worker.py` with your queue consumer or background task.

Create a Background Worker on [Openstead](https://openstead.tech), set its start
command to `python worker.py`, and complete the selected service checkout. The
first deployment starts automatically after payment.

For a scheduled job, choose Cron Job, set `RUN_ONCE=1` in environment variables,
and select a schedule and timezone. The starter catalogue defaults to an hourly
job in UTC. Without `RUN_ONCE`, the process emits a heartbeat every 30 seconds.

Keep application credentials in service variables, never in repository source.
