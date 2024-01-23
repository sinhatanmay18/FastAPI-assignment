from database import sessionLocal
from models import Log


async def log_to_database(request_data, response_data, processing_time):
    db = sessionLocal()
    log_entry = Log(
        request_body=request_data["body"],
        response_body=response_data["body"],
        processing_time=processing_time
    )
    db.add(log_entry)
    db.commit()
    db.close()
