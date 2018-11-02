'''
Created on Sep 14, 2018

@author: agagaleza
'''
import requests
import logging

class Singleton(object):
    _instances = {}
    def __new__(class_, *args, **kwargs):  # @NoSelf
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]
    
class RequestConfigManager(object):
    __metaclass__ = Singleton
    '''
    classdocs
    '''
    basic_config = {}
    http_request_header = {}
    http_request_body = {}
    http_request_url_query_param = {}
    multipart_data ={}
#     logger = logging.getLogger(__name__)
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.configure_logger()
    
    def set_basic_url(self, basic_url):
        self.basic_config['basic_url'] = basic_url
    
    def get_basic_url(self):
        return self.basic_config['basic_url']   
    
    def set_http_content_type(self, header_content_type):
        self.http_request_header['Content-Type'] = header_content_type
    
    def get_http_content_type(self):
        return self.http_request_header['Content-Type']      
    
    def set_http_accept_type(self, header_accept_type):
        self.http_request_header['accept'] = header_accept_type
    
    def get_http_accept_type(self):
        return self.http_request_header['accept']   
    
    def set_endpoint(self, api_endpoint):
        self.basic_config['api_endpoint'] = api_endpoint
    
    def get_endpoint(self):
        return self.basic_config['api_endpoint']       
       
    def get_http_request_body(self):
        return self.http_request_body

    def clear_http_request_body(self):
        self.http_request_body.clear()

    def clear_http_request_header(self):
        self.http_request_header.clear()
               
    def set_get_response_full(self, url_temp):
        self.basic_config['response_full'] = requests.get(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         data=self.http_request_body) 

#         print("GET url is " + str(url_temp))
#         print("body : ")
#         print(self.http_request_body)
#         print("header is " + str(self.http_request_header))
#         print("query param is " + str(self.http_request_url_query_param))
            
    def set_post_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config['response_full'] = requests.post(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 
#         print("post url is " + str(url_temp))
#         print("body : ")
#         print(self.http_request_body)
#         print("header is " + str(self.http_request_header))
#         print("query param is " + str(self.http_request_url_query_param))

    def set_post_uploadimage_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
#         self.clear_http_request_header()
        self.basic_config['response_full'] = requests.post(url_temp,files=self.multipart_data) 
#         print("TEXT: " + self.basic_config['response_full'].text)
#         print("post upload image is is " + str(url_temp))
#         print("files : ")
#         print(self.http_request_body)
#         print("multipart : ")
#         print(self.multipart_data)
#         print("header is " + str(self.http_request_header))
#         print("query param is " + str(self.http_request_url_query_param))
#          
    def set_delete_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config['response_full'] = requests.delete(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 
#         print("url is " + str(url_temp))
#         print("body : ")
#         print(self.http_request_body)
#         print("header is " + str(self.http_request_header))
#         print("query param is " + str(self.http_request_url_query_param))

    def set_put_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config['response_full'] = requests.put(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 
#         print("put url is " + str(url_temp))
#         print("body : ")
#         print(self.http_request_body)
#         print("header is " + str(self.http_request_header))
#         print("query param is " + str(self.http_request_url_query_param))
                        
    def get_response_full(self):
        return self.basic_config['response_full']  

    def get_response_full_json(self):
        return self.basic_config['response_full'].json()     
    
    def set_expected_response_code(self, expected_response_code):
        self.basic_config['expected_response_code'] = expected_response_code
    
    def get_expected_response_code(self):
        return self.basic_config['expected_response_code']  
    
    def set_expected_response_content_type(self, expected_response_content_type):
        self.basic_config['expected_response_content_type'] = expected_response_content_type
    
    def get_expected_response_content_type(self):
        return self.basic_config['expected_response_content_type']  
    
    def get_response_full_status_code(self):
        return self.basic_config['response_full'].status_code   
    
    def get_response_full_content_type(self):
        print (self.basic_config['response_full'].headers['Content-Type'])
        
        return self.basic_config['response_full'].headers['Content-Type']
    
    def set_http_request_body_with_pet_details(self, pet):
        self.http_request_body['id'] = pet.get_pet_id()
#         print(pet.get_pet_id())
        self.http_request_body['name'] = pet.get_pet_name()
        self.http_request_body['photoUrls'] = pet.get_pet_photoUrls()
        self.http_request_body['status'] = pet.get_pet_status()

    def set_http_request_body_with_pet_photo(self, pet):
        self.clear_http_request_body()

        self.multipart_data = {
            'file': (pet.get_pet_photo(), open('./' + pet.get_pet_photo(), 'rb'), 'image/jpeg'),
           }
    def configure_logger(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

