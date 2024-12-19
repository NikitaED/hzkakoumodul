def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),  
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))], 
        'module': obj.__mod__,  
    }
    return info


number_info = introspection_info(42)
print(number_info)
