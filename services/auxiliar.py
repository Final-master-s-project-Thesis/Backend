from models import Player_general, FM_dead_ball_stats, FM_goalkeeper_stats, FM_mental_stats, FM_physical_stats, FM_technical_stats

def dict_by_id(obj_list, id_field, id_value):
    obj = next((o.__dict__ for o in obj_list if getattr(o, id_field) == id_value), None)
    if obj:
        obj.pop(id_field, None)
    return obj

def apply_filters(query, filters):
    if filters.age_min is not None:
        query = query.filter(Player_general.age >= filters.age_min)
    if filters.age_max is not None:
        query = query.filter(Player_general.age <= filters.age_max)
    if filters.height_min is not None:
        query = query.filter(Player_general.height >= filters.height_min)
    if filters.height_max is not None:
        query = query.filter(Player_general.height <= filters.height_max)
    if filters.weight_min is not None:
        query = query.filter(Player_general.weight >= filters.weight_min)
    if filters.weight_max is not None:
        query = query.filter(Player_general.weight <= filters.weight_max)
    if filters.position is not None:
        query = query.filter(Player_general.position.contains(filters.position))
    if filters.market_value_max is not None:
        query = query.filter(Player_general.market_value <= filters.market_value_max)
    if filters.estimated_value_max is not None:
        query = query.filter(Player_general.estimated_value <= filters.estimated_value_max)
    if filters.salary_month_max is not None:
        query = query.filter(Player_general.salary_month <= filters.salary_month_max)
    if filters.talent_min is not None:
        query = query.filter(Player_general.talent >= filters.talent_min)

    return query