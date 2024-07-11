import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root@localhost/gusti_career")

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs where id = :val"),
            {"val": id}
        )
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])