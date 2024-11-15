def introspection_info(obj):
    
    obj_type = type(obj).__name__


    attributes = dir(obj)


    methods = [attr for attr in attributes if callable(getattr(obj, attr)) and not attr.startswith("__")]


    obj_module = str(obj.__class__.__module__)


    info = {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
        "properties": {}
    }


    if hasattr(obj, '__dict__'):
        info["properties"] = vars(obj)

    return info


class SampleClass:
 def __init__(self):
  self.attribute1 = "value1"
  self.attribute2 = 42

 def sample_method(self):
  return "Hello, World!"



sample_obj = SampleClass()


info = introspection_info(sample_obj)


for key, value in info.items():
 print(f"{key}: {value}")