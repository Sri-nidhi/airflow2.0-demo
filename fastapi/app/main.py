from fastapi import FastAPI, HTTPException
from pandas_profiling import ProfileReport
from starlette.responses import RedirectResponse
from fastapi.responses import FileResponse
import pandas as pd
from sqlalchemy import create_engine
import os

from logging.config import dictConfig
import logging

import json
app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/view_dataprofiling/{file_name}")
async def show_data_profile(file_name):
    try:
        print("Fetching file from "+file_name+".html")

        return FileResponse("/"+file_name+".html")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/generate_dataprofiling/{file_name}")
async def generate_data_profile(file_name):
    try:
        AWS_REDSHIFT_HOST = "redshift-cluster-2.cmwaeomvtjzi.us-east-2.redshift.amazonaws.com"
        AWS_REDSHIFT_PASSWORD = ""
        AWS_REDSHIFT_PORT = "5439"
        AWS_REDSHIFT_LOGIN = "awsuser"
        AWS_REDSHIFT_DB = "dev"

        hostname = AWS_REDSHIFT_HOST
        portno = "5439"
        dbname = AWS_REDSHIFT_DB
        dbusername = AWS_REDSHIFT_LOGIN
        dbpassword = AWS_REDSHIFT_PASSWORD
        conn_string = 'postgresql://' + dbusername + ':' + dbpassword + '@' + hostname + ':' + portno + '/' + dbname
        print(conn_string)
        conn = create_engine(conn_string, connect_args={'connect_timeout': 10})
        print("Connection succeeded")
        df = pd.read_sql_query("select * from {}".format(file_name), conn)
        print("DF Loaded")
        profile = df.profile_report(
            title="Data profiling",
            correlations={
                "pearson": {"calculate": False},
                "spearman": {"calculate": False},
                "kendall": {"calculate": False},
                "phi_k": {"calculate": False},
                "cramers": {"calculate": False},
            },
            html={

                "style": {"primary_color": "#EBAF00",
                          "theme": "united"},
                "inline": True,

            },
        )
        profile.to_file("/" + file_name + ".html")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"status": 200, "message": "Checkout the profile generated in this link /view_dataprofiling/" + file_name}
