import json

source = {
    "aggregations": {
        "A": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {"key": "ADL", "doc_count": 1},
                {"key": "SDD", "doc_count": 1},
                {"key": "JJD", "doc_count": 1},
            ],
        },
        "B": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {"key": "ABC", "doc_count": 1},
                {"key": "CDE", "doc_count": 1},
                {"key": "FGH", "doc_count": 1},
            ],
        },
        "C": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [{"key": "XYX", "doc_count": 1}, {"key": "NXS", "doc_count": 1}],
        },
    }
}


convert_map = {
    "buckets": "values",
    "doc_count": "count",
    "key": "title",
}

remove_map = {"sum_other_doc_count", "doc_count_error_upper_bound"}

add_map = {"name": "Changed VAL_", "fieldName": "VAL_"}


def converting_generator(
    source_: dict, convert_map_: dict, remove_map_: set, add_map_: dict
):
    working_dict = {k: v for k, v in source_.items()}
    variable_identifier = "VAL_"

    for key, inner_dic in working_dict.items():
        inner_dic: dict
        for rm_key in remove_map_:
            try:
                inner_dic.pop(rm_key)
            except KeyError:
                pass

        for add_key, add_val in add_map_.items():
            inner_dic[add_key] = add_val.replace(variable_identifier, key)

        dumped = json.dumps(inner_dic, indent=2)

        for original, target in convert_map_.items():
            dumped = dumped.replace(original, target)

        yield json.loads(dumped)


converted = {
    "aggregation_filters": list(
        converting_generator(source["aggregations"], convert_map, remove_map, add_map)
    )
}

for inner_dict in converted["aggregation_filters"]:
    for even_inner_dict in inner_dict["values"]:
        even_inner_dict["paragraph"] = None

print(json.dumps(converted, indent=2))
