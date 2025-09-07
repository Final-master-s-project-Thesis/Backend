def dict_by_id(obj_list, id_field, id_value):
    obj = next((o.__dict__ for o in obj_list if getattr(o, id_field) == id_value), None)
    if obj:
        obj.pop(id_field, None)
    return obj