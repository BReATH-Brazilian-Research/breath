from breath.api_interface.queue import Queue


class Response:
    def __init__(self, sucess:bool, response_data:dict=None):
        self.sucess = sucess
        self.response_data = response_data

class Request:
    '''Stores some request info.
    '''

    def __init__(self, service_name:str, operation_name:str, request_info:dict, response_queue:Queue):
        '''Request constructor

            :param service_name: Name of requested service
            :type service_name: str

            :param operation_name: Name of requested operation
            :type operation_name: str

            :param request_info: Request parameters
            :type request_info: dict

            :param response_queue: Queue to send response
            :type response_queue: breath.api_interface.Queue
        '''
        
        self.service_name = service_name
        self.operation_name = operation_name
        self.request_info = request_info
        self.response_queue = response_queue

    def send_response(self, response:Response) -> None:
        '''Send response for the request
            
            :param response: Response data
            :type response: breath.api_interface.Response
        '''

        self.response_queue.insert(response)