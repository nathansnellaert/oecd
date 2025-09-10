from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_PE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patient_experiences")
        print(f"Uploaded {data.num_rows} rows to patient_experiences")
        
    save_state("patient_experiences", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
