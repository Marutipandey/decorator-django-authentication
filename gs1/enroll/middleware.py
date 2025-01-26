# myapp/middleware.py

class LogRequestMiddleware:
    def __init__(self, get_response):
        # get_response को प्राप्त करना जो अगले middleware या view को कॉल करता है
        self.get_response = get_response

    def __call__(self, request):
        # रिक्वेस्ट के HTTP मेथड और URL पाथ को लॉग करना
        method = request.method  # जैसे GET, POST, आदि
        path = request.path      # जैसे /home/, /about/ आदि

        # कंसोल पर इनको प्रिंट करना (यह लॉगिंग का साधारण तरीका है)
        print(f"Request Method: {method}, Path: {path}")

        # रिक्वेस्ट को अगले स्टेप (views) पर भेजना
        response = self.get_response(request)

        # रिस्पॉन्स भेजने से पहले कस्टम हेडर जोड़ना
        response['X-Custom-Header'] = 'This is a custom header'

        # रिस्पॉन्स लौटाना
        return response
