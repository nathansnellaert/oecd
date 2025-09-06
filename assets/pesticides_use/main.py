from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGPEST")
    
    if data.num_rows > 0:
        upload_data(data, "pesticides_use")
        print(f"Uploaded {data.num_rows} rows to pesticides_use")
        
    save_state("pesticides_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
