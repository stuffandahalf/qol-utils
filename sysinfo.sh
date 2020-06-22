#!/bin/sh

watch "echo 'CPU Frequency'; \
	lscpu | grep MHz; echo ''; \
	sensors"

