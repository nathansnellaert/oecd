from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_education_expenditure_source_destination")
        print(f"Uploaded {data.num_rows} rows to education_expenditure_source_destination")
        
    save_state("education_expenditure_source_destination", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
