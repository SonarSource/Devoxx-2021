from db_wrapper import ConnectionWrapper

def fetch_value(value_id: str):
    wrapper = ConnectionWrapper()
    value_obj = wrapper.get_single(value_id)
    wrapper.cleanup(True)
    return value_obj

def fetch_first_value():
    wrapper = ConnectionWrapper()
    wrapper.cleanup()
    return wrapper.get_single(1)
