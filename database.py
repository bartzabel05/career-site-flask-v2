import sqlalchemy
from sqlalchemy import create_engine,text
import os

db_conn_str=os.environ['DB_CONNECTION_STRING']
# print(sqlalchemy.__version__)
engine=create_engine(
  db_conn_str,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
  result=conn.execute(text("SELECT * from careers.jobs")) #cursor
  
  jobs=[]
  for row in result.all():
    jobs.append(row._asdict())

  print(jobs)
  
  # print(type(result))
  # result_all=result.all()
  # print(type(result_all))
  # # print(result_all)
  # first_result=result_all[0]
  # print(type(first_result))
  # print(first_result)
  # first_result_dict=dict(result_all[0]) #.__dict__
  # print(type(first_result_dict))
  # print(first_result_dict)