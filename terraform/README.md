# Deployment
Uses AWS ECS and ECR

# ECR
```bash
703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app
```

# Manually pushing to ECR
Build and tag docker image
```bash
docker build -f Dockerfile -t dylan_test_app . 
docker tag dylan_test_app:latest 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
```

Login docker to aws
```bash
docker login -u AWS -p $(aws ecr get-login-password --region ap-southeast-2 --profile dylanio) 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com
```

Push from docker to ECR
```bash
docker push 703161335764.dkr.ecr.ap-southeast-2.amazonaws.com/dylan_test_app:latest
```

# Update ECS Task
```bash
aws ecs update-service --cluster dylan_test_app --service deploy_service --force-new-deployment --profile dylanio --region ap-southeast-2      
```