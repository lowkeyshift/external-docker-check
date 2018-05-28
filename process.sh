#!/bin/bash

( echo "cat <<EOF >/etc/datadog-agent/conf.d/http_check.d/conf.yaml";
cat /etc/datadog-agent/conf.d/http_check.d/template.yaml;
echo "EOF";
) >temp.yml
. temp.yml
