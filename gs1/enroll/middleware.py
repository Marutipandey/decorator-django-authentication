
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  

    def __call__(self, request):
        print("CustomHeaderMiddleware: Request received")
        request.META['X-Custom-Request-Header'] = 'This is a custom header'
        response = self.get_response(request)
        print("CustomHeaderMiddleware: Response is being sent")
        response['X-Custom-Response-Header'] = 'This is a custom response header'
        return response
