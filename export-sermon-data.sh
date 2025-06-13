#!/bin/bash

extract_php_var(){
  sed -n "s/define('$1', '\([^']*\)');/\1/p" wp-config.php
}

mysql -u $(extract_php_var "DB_USER") --password=$(extract_php_var "DB_PASSWORD") -D $(extract_php_var "DB_NAME") -e "
SELECT 
  s.id,
  s.title,
  s.datetime,
  s.start,
  s.end,
  p.name AS preacher,
  se.name AS series,
  sv.name AS service,
  f.name as audio
FROM wp_sb_sermons s
LEFT JOIN wp_sb_stuff f ON s.id = f.sermon_id
LEFT JOIN wp_sb_preachers p ON s.preacher_id = p.id
LEFT JOIN wp_sb_series se ON s.series_id = se.id
LEFT JOIN wp_sb_services sv ON s.service_id = sv.id
ORDER BY s.datetime DESC;
" --raw --batch
