docker build -f Dockerfile -t dylan_test_app . 
docker tag dylan_test_app:latest 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
docker login -u AWS -p $(aws ecr get-login-password --region ap-southeast-2) 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com
docker push 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
aws ecs update-service --cluster dylan_test_app --service deploy_service --force-new-deployment --profile dylanio --region ap-southeast-2    