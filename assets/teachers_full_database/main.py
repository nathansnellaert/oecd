from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_TEACH_DB")
    
    if data.num_rows > 0:
        upload_data(data, "teachers_full_database")
        print(f"Uploaded {data.num_rows} rows to teachers_full_database")
        
    save_state("teachers_full_database", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
