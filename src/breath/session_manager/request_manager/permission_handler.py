from breath.api_interface.request import Request
from breath.session_manager.request_manager.request_handler import RequestHandler


class PermissionnHandler(RequestHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request:Request) -> None:
        '''Validates the request, looking for permission problems

            TODO Implementar validação de permissão
        '''
        self._send_for_next(request)