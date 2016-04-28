from apps.utils.led import blink


class BlinkMiddleware(object):

    def process_request(self, request):
        blink(17)
