rm -rf log.jtl
rm -rf jmeter-output
jmeter -n -t jmeter-realworld.jmx -l log.jtl -e -o jmeter-output


