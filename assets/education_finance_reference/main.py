from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN_ANNEX@DF_UOE_FIN_ANNEX")
    
    if data.num_rows > 0:
        upload_data(data, "education_finance_reference")
        print(f"Uploaded {data.num_rows} rows to education_finance_reference")
        
    save_state("education_finance_reference", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
