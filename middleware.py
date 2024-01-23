from fastapi import Request, Response
from logger import log_to_database
import time


async def log_requests_middleware(request: Request, call_next):
    start_time = time.time()

    request_body = await request.body()
    request_data = {
        "method": request.method,
        "url": str(request.url),
        "body": request_body.decode() if isinstance(request_body, bytes) else request_body
    }

    response = await call_next(request)

    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    response_data = {
        "status_code": response.status_code,
        "body": response_body.decode() if isinstance(response_body, bytes) else response_body
    }

    process_time = time.time() - start_time

    await log_to_database(request_data, response_data, process_time)

    return Response(content=response_body, status_code=response.status_code, media_type=response.media_type,
                    headers=dict(response.headers))