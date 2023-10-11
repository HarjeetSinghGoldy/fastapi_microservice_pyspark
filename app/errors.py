from fastapi import HTTPException

def handle_data_not_found_error(data_id):
    raise HTTPException(status_code=404, detail=f"Data with ID {data_id} not found")

def handle_user_not_found_error(user_id):
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

def handle_internal_server_error():
    raise HTTPException(status_code=500, detail="Internal Server Error")

class DataNotFoundError(Exception):
    def __init__(self, data_id):
        self.data_id = data_id
        super().__init__(f"Data with ID {data_id} not found")

class UserNotFoundError(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found")