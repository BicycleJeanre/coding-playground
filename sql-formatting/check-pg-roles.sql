
SELECT DISTINCT
    role_name,
    object_type,
    object_name,
    privilege_type,
    privilege,
    inherited_from
FROM (
    SELECT rolname AS role_name, 
           'Database' AS object_type,
           datname AS object_name, 
           'Database-Level' AS privilege_type,
           CASE 
               WHEN pg_catalog.has_database_privilege(rolname, datname, 'CONNECT') THEN 'CONNECT'
               WHEN pg_catalog.has_database_privilege(rolname, datname, 'CREATE') THEN 'CREATE'
               WHEN pg_catalog.has_database_privilege(rolname, datname, 'TEMP') THEN 'TEMP'
               ELSE NULL
           END AS privilege,
           CASE 
               WHEN pg_catalog.has_database_privilege(rolname, datname, 'CONNECT') AND 
                    pg_catalog.has_database_privilege('public', datname, 'CONNECT') THEN 'PUBLIC'
               ELSE NULL
           END AS inherited_from
    FROM pg_catalog.pg_database
    CROSS JOIN pg_catalog.pg_roles
    WHERE (pg_catalog.has_database_privilege(pg_roles.rolname, pg_database.datname, 'CONNECT')
           OR pg_catalog.has_database_privilege(pg_roles.rolname, pg_database.datname, 'CREATE')
           OR pg_catalog.has_database_privilege(pg_roles.rolname, pg_database.datname, 'TEMP'))
      AND pg_database.datname NOT IN ('template0', 'template1')
    UNION ALL
    SELECT rolname AS role_name, 
           'Cluster' AS object_type,
           NULL AS object_name,
           'Cluster-Level' AS privilege_type,
           CASE
               WHEN rolsuper THEN 'SUPERUSER; ' ELSE '' END ||
           CASE
               WHEN rolcanlogin THEN 'LOGIN; ' ELSE '' END ||
           CASE
               WHEN rolcreaterole THEN 'CREATE ROLE; ' ELSE '' END ||
           CASE
               WHEN rolcreatedb THEN 'CREATE DATABASE; ' ELSE '' END ||
           CASE
               WHEN rolreplication THEN 'REPLICATION; ' ELSE '' END ||
           CASE
               WHEN rolinherit THEN 'INHERIT; ' ELSE '' END AS privilege,
           COALESCE(inherited_from_roles.inherited_from, 'Direct') AS inherited_from
    FROM pg_catalog.pg_roles
    LEFT JOIN (SELECT roleid AS role_oid, member AS member_oid, rolname AS inherited_from
               FROM pg_catalog.pg_auth_members
               JOIN pg_catalog.pg_roles AS inherited_roles ON pg_auth_members.roleid = inherited_roles.oid) AS inherited_from_roles
        ON pg_roles.oid = inherited_from_roles.member_oid
    WHERE (rolcanlogin OR rolsuper OR rolcreaterole OR rolcreatedb OR rolreplication OR rolinherit)
    UNION ALL
    SELECT grantee AS role_name, 
           CASE 
               WHEN ns.nspname IS NOT NULL AND cls.relname IS NULL THEN 'Schema'
               WHEN cls.relname IS NOT NULL THEN 'Table'
               ELSE 'Other'
           END AS object_type,
           CASE 
               WHEN ns.nspname IS NOT NULL AND cls.relname IS NULL THEN ns.nspname
               WHEN cls.relname IS NOT NULL THEN ns.nspname || '.' || cls.relname
               ELSE NULL
           END AS object_name,
           'Object-Level' AS privilege_type, 
           privilege_type AS privilege, 
           grantor AS inherited_from
    FROM pg_catalog.pg_namespace ns
    LEFT JOIN pg_catalog.pg_class cls ON ns.oid = cls.relnamespace
    LEFT JOIN information_schema.role_table_grants grants 
           ON grants.table_schema = ns.nspname AND grants.table_name = cls.relname
) privileges
WHERE role_name NOT LIKE 'pg_%'
  AND object_name NOT LIKE 'information_schema.%'
  AND object_name NOT LIKE 'pg_catalog.%'
ORDER BY role_name, object_type, object_name, privilege_type;