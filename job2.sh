p=$(kubectl get service/httpd -o jsonpath="{.spec.ports[0].nodePort}")
exit_code=$(curl -o /dev/null -s -w "%{http_code}" http://192.168.99.100:$p)
if [ $exit_code == 200 ]
then
exit 0
else
python3 /task6_code/mail.py
exit 1
fi
