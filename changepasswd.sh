NOW=$(date)
echo $NOW ":" $1 "changed password " >> useraccess.log
htpasswd -b ../../.htpasswd $1 $2
