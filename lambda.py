import csv
import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Replace 'your-bucket-name' and 'event_history.csv' with your S3 bucket and file name
    bucket_name = 'your-bucket-name'
    csv_file_key = 'event_history.csv'

    # Set the inactivity time in minutes as a parameter
    inactivity_minutes = event.get('inactivity_minutes', 20)  # Default to 20 minutes if not provided

    total_time = 0
    last_event_time = None

    try:
        # Download the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=csv_file_key)
        csv_data = response['Body'].read().decode('utf-8').splitlines()

        # Parse CSV data
        reader = csv.DictReader(csv_data)
        
        for row in reader:
            event_time = row['Event time']
            event_name = row['Event name']
            
            try:
                event_datetime = datetime.fromisoformat(event_time[:-1])  # Remove 'Z' from the end
            except ValueError:
                continue  # Skip rows with invalid datetime format
            
            if last_event_time is not None:
                time_difference = (last_event_time - event_datetime).total_seconds()
                print(time_difference)
                if time_difference > 0:  # Ensure we don't add negative time differences
                    if time_difference <= inactivity_minutes * 60:  # Convert inactivity_minutes to seconds
                        total_time += time_difference
                    else:
                        total_time += inactivity_minutes * 60  # Add inactivity_minutes for the inactive period
            
            last_event_time = event_datetime
    
        # Convert total_time to hours and minutes for display
        total_time_minutes = total_time / 60
        total_hours = int(total_time_minutes // 60)
        total_minutes = int(total_time_minutes % 60)

        return {
            'statusCode': 200,
            'body': f'Total time spent on AWS: {total_hours} hours {total_minutes} minutes'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
