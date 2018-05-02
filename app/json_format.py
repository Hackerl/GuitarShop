def models_format_json(models, key, columns=[]):
    result = {key: []}
    if columns:
        for model in models:
            result[key].append(model.to_json(columns = columns))
    else:
        for model in models:
            result[key].append(model.to_json())
    return result

def get_attr_list_from_models(models, attr):
    result = []
    for model in models:
        result.append(getattr(model, attr))
    return result