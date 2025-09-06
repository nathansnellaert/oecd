from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_CLS")
    
    if data.num_rows > 0:
        upload_data(data, "class_size")
        print(f"Uploaded {data.num_rows} rows to class_size")
        
    save_state("class_size", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
