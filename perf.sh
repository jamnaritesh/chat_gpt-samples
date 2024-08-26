#!/bin/bash
PID=<YourJavaProcessID>
for i in {1..20}
do
   jstack $PID > jstack_dump_$i.txt
   ps -L -p $PID -o pid,tid,pcpu | awk 'NR>1 {printf "%s\t0x%x\t%s\n", $1, $2, $3}' > cpu_usage_$i.txt
   sleep 1
done