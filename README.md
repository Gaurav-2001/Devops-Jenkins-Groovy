# Using Jenkins by Groovy code also Deploying the web services using Jenkins-K8S

## Aim
Create container image that’s has Jenkins installed  using dockerfile  Or You can use the Jenkins Server on RHEL 8/7 </br>
When we launch this image, it automatically starts Jenkins service in the container.</br>
Create a seed job for the groovy code. The groovy code must launch two jobs - Job1 and job2 </br>
Job1: launch the web-services from the yaml file with the services been exposed and the deployment been mounted to the main directory</br>
Job2: if the job1 fails inform the developer with the proper email about the failure</br>
Create an buildpipeline using the groovy code. About the job1 and job2</br>

# Blog URL : [Here](https://thesocialcomment.com/project/full/Using-Jenkins-by-Groovy-code-also-Deploying-the-web-services-using-Jenkins-K8S?pid=5f278a8ca561f35485d3f83a)
