# To confirm if your AWS credentials are correct, test them locally:
1. brew install awscli  # For macOS
2. aws configure
    •	Enter your AWS_ACCESS_KEY_ID
	•	Enter your AWS_SECRET_ACCESS_KEY
	•	Enter your AWS_REGION
3. aws s3 ls s3://your-bucket-name --region your-region   # to test your bucket connection
	•	Example: aws s3 ls s3://tryon-frontend --region us-east-1
4. Manually Invalidate Cloudfront
	•	aws cloudfront create-invalidation --distribution-id YOUR_CLOUDFRONT_ID --paths "/*"
