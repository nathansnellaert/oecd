from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_EDU@DF_EMP")
    
    if data.num_rows > 0:
        upload_data(data, "employment_by_education_level")
        print(f"Uploaded {data.num_rows} rows to employment_by_education_level")
        
    save_state("employment_by_education_level", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
