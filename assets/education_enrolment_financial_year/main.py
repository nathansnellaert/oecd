from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN_ENR@DF_UOE_FIN_ENR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_education_enrolment_financial_year")
        print(f"Uploaded {data.num_rows} rows to education_enrolment_financial_year")
        
    save_state("education_enrolment_financial_year", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
