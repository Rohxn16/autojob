import os
from dotenv import load_dotenv
"""
Uses the resume contexted keywords generated to search for job roles:
"""
import requests
load_dotenv()

class Jobfinder:

    def __init__(self):
        self.url:str = "https://api.theirstack.com/v1/jobs/search"
        self.headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('KEY')}"
        }


    def search_jobs(self,keyword):
        """
        Returns the top 5 jobs for the given keyword
        """
        body = {
        "page": 0,
        "limit": 5,  # We only want the top 5
        "job_title_or": [keyword],
        "job_country_code_or": ["IN"],
        "posted_at_max_age_days": 7,
        "order_by": [{"field": "date_posted", "desc": True}] # Get the newest ones first
        }

        try:
            # We use json=body instead of data=body to let requests handle the encoding
            response = requests.post(self.url, json=body, headers=self.headers)
            response.raise_for_status() # Check for errors
            
            data = response.json()
            
            # TheirStack usually returns a list of jobs under a 'data' or similar key
            # Based on their docs, it returns a list directly or inside a 'jobs' object
            jobs = data.get('data', []) 
            
            results = []
            for job in jobs:
                results.append({
                    "title": job.get("job_title"),
                    "company": job.get("company_name"),
                    "url": job.get("url"),
                    "date": job.get("date_posted")
                })
                
            return results

        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs for {keyword}: {e}")
            return []

if __name__ == '__main__':
    finder = Jobfinder()
    res = finder.search_jobs('Python')
    print(res)