import time
import json


class RequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        log_data = {
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "run_time": time.time() - start_time
        }

        with open("log.txt", "a") as f:
            f.write(json.dumps(log_data))

        return response
