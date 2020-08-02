if kubectl get deployment | grep httpd
then
echo "server is already running"
else
kubectl create -f httpd_dep1.yml
sleep 30
POD=$(kubectl get pod -l app=httpd -o jsonpath="{.items[0].metadata.name}")
kubectl cp /task6_code/*.html $POD:/usr/local/apache2/htdocs/
fi
