import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
# Loading .env file for api key

def newsAPI():
    LINK = ("https://newsdata.io/api/1/latest?" 
  f"apikey={api_key}"
  "&country=us,bh,ir,bd"
  "&language=en"
  "&category=breaking,business,politics,technology,world"
  "&prioritydomain=top"
  "&image=0"
  "&domainurl=bbc.com,nytimes.com,reuters.com,aljazeera.com"
  "&removeduplicate=1"
  "&sort=source"
  "&excludefield=ai_summary,ai_org,ai_region,sentiment_stats,duplicate,sentiment,ai_tag,category,video_url,keywords,source_priority,pubdatetz,source_url"
  "&size=1") # Preparing Api params and adding api key
    response = requests.get(LINK,timeout=10) # Requesting get from api with timeout set as 10 ofc
    status = response.status_code
    data = response.json()
    return data
newsAPI()
# Adding status code, Turning response into varible data and turning the contents into json as python automatically does not turn them into json


# unpacking data from function newsapi
data = newsAPI()

def cleanoutput():
    Page = data['results'][0]
    Clean_Article ={
        "Country": Page.get("country","None"),
        "Image": Page.get("image_url","None"),
        "Title": Page.get("title","None"),
        "Description": Page.get("description","None")
    
    }
    return Clean_Article # Cleaning Api output by creating the data varible into page and then ensuring that only defined outputs are taken out

print(cleanoutput())
Clean_Article = cleanoutput() # unpacking cleaned output from function cleanoutput 






def Prediction():
    API = 'soon'
    NEWS = (Clean_Article["Description"])
    response = requests.post(API,json={"text":NEWS},timeout=14)
    result = response.json()
    print(f"{result} is my prediction")

Prediction() # posting output to Fastapi for topic prediction
