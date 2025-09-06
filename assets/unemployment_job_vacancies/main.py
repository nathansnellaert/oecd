from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_OLAB@DF_OIALAB_INDIC")
    
    if data.num_rows > 0:
        upload_data(data, "unemployment_job_vacancies")
        print(f"Uploaded {data.num_rows} rows to unemployment_job_vacancies")
        
    save_state("unemployment_job_vacancies", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
