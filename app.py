from flask import Flask,render_template,jsonify
from database import engine
from sqlalchemy import text
app=Flask(__name__)

# JOBS=[
#   {
#     "id":1,
#     "title":"Data Analyst",
#     "location":"Bengaluru,India",
#     "salary":'Rs:10,00,000'
#   },
#   {
#     "id":2,
#     "title":"Frontend Engineer",
#     "location":"Bengaluru,India",
#     "salary":'Rs:10,00,000'
#   },
#   {
#     "id":3,
#     "title":"Backend Engineer",
#     "location":"Bengaluru,India",
#     "salary":'Rs:10,00,000'
#   },
# ]

def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("SELECT * from careers.jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


@app.route("/")
def helloWorld():  
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs)
  
@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)