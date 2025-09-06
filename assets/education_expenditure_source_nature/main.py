from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN@DF_UOE_FIN_INDIC_SOURCE_NATURE")
    
    if data.num_rows > 0:
        upload_data(data, "education_expenditure_source_nature")
        print(f"Uploaded {data.num_rows} rows to education_expenditure_source_nature")
        
    save_state("education_expenditure_source_nature", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
