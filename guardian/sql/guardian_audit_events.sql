-- Guardian audit events — append-only MergeTree per ADR-019 §6.5 (TTL 5y, FCA CASS retention).
-- Apply: clickhouse-client --host=127.0.0.1 --port=9000 < guardian/sql/guardian_audit_events.sql
-- Or HTTP: curl -sS 'http://127.0.0.1:8123/?database=default' --data-binary @guardian/sql/guardian_audit_events.sql

CREATE TABLE IF NOT EXISTS guardian_audit_events
(
    event_date           Date     DEFAULT toDate(event_time_utc),
    event_time_utc       DateTime,
    request_id           String,
    subject_type         String,
    subject_id           String,
    scope                String,
    actor                String,
    prompt               String,
    verdict_result       String,
    verdict_summary      String,
    reasons_json         String,
    sources_json         String,
    loaded_domains_json  String,
    dry_run              UInt8,
    storage_backend      String
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(event_date)
ORDER BY (event_date, scope, subject_type, subject_id, request_id)
TTL event_date + INTERVAL 5 YEAR
SETTINGS index_granularity = 8192;
