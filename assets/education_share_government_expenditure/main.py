from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN@DF_UOE_FIN_INDIC_SHARE_EDU_GOV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_education_share_government_expenditure")
        print(f"Uploaded {data.num_rows} rows to education_share_government_expenditure")
        
    save_state("education_share_government_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
