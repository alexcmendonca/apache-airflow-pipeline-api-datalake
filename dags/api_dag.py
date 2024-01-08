import sys
sys.path.insert(0, '/home/alexmend/Documents/airflow')
from airflow.models import DAG
from datetime import datetime, timedelta
from operators.api_operator import ApiOperator
from os.path import join
from airflow.utils.dates import days_ago

with DAG(
        dag_id = 'ApiDAG', 
        start_date = days_ago(2),
        schedule_interval = '@daily'
        ) as dag:
        TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
        query = "datascience"
        to = ApiOperator(file_path=join('datalake/api_datascience',
                                    'extract_date={{ ds }}',
                                    'datascience_{{ ds_nodash }}.json'),
                                    query=query, 
                                    start_time='{{ data_interval_start.strftime("%Y-%m-%dT%H:%M:%S.00Z") }}', 
                                    end_time='{{ data_interval_end.strftime("%Y-%m-%dT%H:%M:%S.00Z") }}', 
                                    task_id='twitter_datascience')