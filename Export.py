import inspect
from Object import *
from typing import Callable


def export(name=None):
    if callable(name):
        name.export = True
        name.export_name = name.__name__
        return name

    def export_proper(obj):
        obj.export = True
        obj.export_name = obj.__name__ if name is None else name
        return obj
    return export_proper


def get_functions_to_export(container, prototype=None):
    functions_to_export = []
    for name, obj in inspect.getmembers(container, inspect.isfunction):
        if hasattr(obj, 'export') and getattr(obj, 'export') == True:
            functions_to_export.append((obj.export_name, obj, prototype))
    return functions_to_export


def get_functions_to_export_from_module(module):
    functions_to_export = get_functions_to_export(module)
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if hasattr(obj, 'export') and getattr(obj, 'export'):
            prototype = getattr(obj, 'export_name')
            functions_to_export += get_functions_to_export(obj, prototype)

    return functions_to_export


def lora_function_args_signature_from_python(func, prototype=None):
    lora_function_sig_args = []
    sig = inspect.signature(func)
    for name, param in sig.parameters.items():
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else None
        lora_type = ObjectType.ANY
        if param_type == str:
            lora_type = ObjectType.STRING
        elif param_type in (int, float):
            lora_type = ObjectType.NUMBER
        elif param_type == Callable:
            lora_type = ObjectType.CALLBACK
        elif param_type == bool:
            lora_type = ObjectType.BOOLEAN
        elif param_type == list:
            lora_type = ObjectType.ARRAY
        elif param_type == tuple:
            lora_type = ObjectType.TUPLE
        lora_function_sig_args.append(lora_type)
    return lora_function_sig_args
