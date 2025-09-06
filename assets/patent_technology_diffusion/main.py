from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAT_DIFF@DF_PAT_DIFF")
    
    if data.num_rows > 0:
        upload_data(data, "patent_technology_diffusion")
        print(f"Uploaded {data.num_rows} rows to patent_technology_diffusion")
        
    save_state("patent_technology_diffusion", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
