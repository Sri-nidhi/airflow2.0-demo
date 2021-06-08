
from fastapi import FastAPI, HTTPException
from pandas_profiling import ProfileReport
from starlette.responses import RedirectResponse
from fastapi.responses import FileResponse
from db_opn import loaddf

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
    except:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/generate_dataprofiling/{file_name}")
async def generate_data_profile(file_name):
    try:
        df = loaddf(file_name)
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
    except:
        raise HTTPException(status_code=404, detail="Error while generating profile")
    return {"status": 200, "message": "Checkout the profile generated in this link /view_dataprofiling/" + file_name}
