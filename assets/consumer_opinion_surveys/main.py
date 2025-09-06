from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_CS")
    
    if data.num_rows > 0:
        upload_data(data, "consumer_opinion_surveys")
        print(f"Uploaded {data.num_rows} rows to consumer_opinion_surveys")
        
    save_state("consumer_opinion_surveys", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
