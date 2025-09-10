from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_CONSULT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_medical_consultations")
        print(f"Uploaded {data.num_rows} rows to medical_consultations")
        
    save_state("medical_consultations", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
