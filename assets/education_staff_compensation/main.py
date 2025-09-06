from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN@DF_UOE_FIN_NATURE_STAFF")
    
    if data.num_rows > 0:
        upload_data(data, "education_staff_compensation")
        print(f"Uploaded {data.num_rows} rows to education_staff_compensation")
        
    save_state("education_staff_compensation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
