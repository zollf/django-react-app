docker build -f terraform/Dockerfile -t dylan_test_app . 
docker tag dylan_test_app:latest 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
docker login -u AWS -p $(aws ecr get-login-password --region ap-southeast-2) 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com
docker push 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
aws ecs update-service --cluster dylan_test_app --service deploy_service --force-new-deployment > /dev/null 

IMAGES_TO_DELETE=$(aws ecr list-images --region ap-southeast-2 --repository-name dylan_test_app --filter tagStatus=UNTAGGED --query imageIds[*] --output json)
aws ecr batch-delete-image --region ap-southeast-2 --repository-name dylan_test_app --image-ids "$IMAGES_TO_DELETE" || true