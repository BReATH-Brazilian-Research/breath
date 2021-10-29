from breath.api_interface.queue import Queue


class Response:
    def __init__(self, sucess:bool, response_data:dict=None):
        self.sucess = sucess
        self.response_data = response_data

class Request:
    '''Stores some request info.
    '''

    def __init__(self, requested_service:str, request_info:dict, response_queue:Queue):
        '''Request constructor

            :param requested_service: Name of requested service
            :type requested_service: str

            :param request_info: Request explanation
            :type request_info: dict

            :param response_queue: Queue to send response
            :type response_queue: breath.api_interface.Queue
        '''
        
        self.requested_service = requested_service
        self.request_info = request_info
        self.response_queue = response_queue

    def send_response(self, response:Response) -> None:
        '''Send response for the request
            
            :param response: Response data
            :type response: breath.api_interface.Response
        '''

        self.response_queue.insert(response)