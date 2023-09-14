# AWSUserActivityMonitoring
AWS Lambda Function for Calculating Total Time Spent on AWS.  It can be used to monitor user activity and calculate the active time spent on AWS services.

## Description

This AWS Lambda function calculates the total time spent on AWS based on event data stored in a CSV file in an S3 bucket. It takes into account user-defined inactivity time and calculates the total active time spent on AWS.

## Usage

### Prerequisites

- AWS account with necessary permissions to create and invoke Lambda functions.
- An S3 bucket with the CSV file containing event data.

### Deploying the Lambda Function

1. Create a new AWS Lambda function in your AWS account using the provided code.

2. Set up the necessary IAM permissions for your Lambda function to read the CSV file from the specified S3 bucket.

3. Modify the Lambda function code to specify your S3 bucket name and the CSV file name:

   \`\`\`python
   bucket_name = 'your-bucket-name'
   csv_file_key = 'event_history.csv'
   \`\`\`

4. Deploy the Lambda function.

### Invoking the Lambda Function

You can invoke the Lambda function either manually through the AWS Management Console or programmatically using the AWS SDKs or AWS CLI.

When invoking the Lambda function programmatically, you can also specify the inactivity time in minutes as a parameter:

\`\`\`json
{
  "inactivity_minutes": 20
}
\`\`\`

The \`inactivity_minutes\` parameter allows you to set the threshold for considering a period of inactivity. If not provided, it defaults to 20 minutes.

### Viewing the Results

The Lambda function will calculate the total time spent on AWS and return a response similar to the following:

\`\`\`
Total time spent on AWS: [total_hours] hours [total_minutes] minutes
\`\`\`

