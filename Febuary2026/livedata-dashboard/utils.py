
def get_http_error_message(response, http_error):
    match response.status_code:
                    case 400:
                        return ("Bad request\nPlease check your input")
                    case 401:
                        return ("Unauthorized\nInvalid API key")
                    case 403:
                        return ("Forbidden\nAccess is denied")
                    case 404:
                        return ("Not found\nCity not found")
                    case 500:
                        return ("Internal Server Error\nPlease Try again later")
                    case 502:
                        return ("Bad Gateway\nInvalid response from the sever")
                    case 503:
                        return ("Servince Unavailable\nSever is down")
                    case 504:
                        return ("Gateway Timeout\nNo response from the sever")
                    case _:
                        return (f"HTTP error occured\n{http_error}")