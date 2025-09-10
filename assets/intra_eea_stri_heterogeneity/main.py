from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STRI@DF_STRI_INTRAEEA_HETERO")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_intra_eea_stri_heterogeneity")
        print(f"Uploaded {data.num_rows} rows to intra_eea_stri_heterogeneity")
        
    save_state("intra_eea_stri_heterogeneity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
