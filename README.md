# airflow2.0-demo

Slide Deck:

https://speakerdeck.com/srinidhi/getting-started-with-apache-airflow-srinidhi


## Using this Repo

This REPO contains docker compose file to setup **Apache-Airflow 2.1.0** along with other services - **postgres** and **adminer** (client tool to query postgres db).

Preqreuisites before running the docker compose

Create a VPC with CIDR - 10.0.0.0/16 and a subnet under it.
Configure the security group to accept all incoming connections
Create a redshift cluster with public visibility and disabling **use default** toggle while creating the cluster, and choose then vpc created above. 

Download the covid dataset csv from here and place them in AWS S3 bucket (Have public access to S3 Bucket)
Ensure you replace he path to your input directory in the S3ToRedshiftOperators in .py.


Connections to be added in airflow
1. AWS connection with id - **aws_id**
2. Redshift cluster with id - **redshift_land**
3. S3 connection with id - **s3_conn**

PS: The resources are created with public access since this is to try out airflow. But while deploying in production, its not a good practice to expose the aws resources publicly. 
