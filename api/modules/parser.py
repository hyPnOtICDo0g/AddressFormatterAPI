from flask import jsonify

def dupe_remove(fields):
    temp=[]
    add_str = [ele.strip(' ') if type(ele) == str else str(ele) for ele in fields]
    fields=['NA' if (nan=='' or nan==None) else nan for nan in add_str][::-1]
    for ele in fields:
        if ele is None or ele=='' or ele not in temp:
            temp.append(ele)
        else:
            temp.append('NA')
    return temp[::-1]

# handle missing 'trailing' fields (v1 api)
def formatter(fields):
    count = 9-len(fields)
    if count<9 and count!=0:
        for i in range(count):
            fields.append(None)
    return dupe_remove(fields)

def json_details(fields):
    try:
        json_data=({
            "building": fields[0],
            "street": fields[1],
            "locality": fields[2],
            "landmark": fields[3],
            "vtc": fields[4],
            "sub_district": fields[5],
            "district": fields[6],
            "state": fields[7],
            "pincode": fields[8]
        })
    except IndexError:
        json_data=({
            "null": "null"
        })
    return json_data

# v1 api takes a raw string as input
def v1(json_input):
    try:
        fields = formatter(json_input['raw'].strip().split(','))
    except KeyError:
        return { "invalid": "Wrong Format." }
    return jsonify(json_details(fields))

# v2 api takes split field json data
def v2(json_input):
    dummy_addr=['','','','','','','','','',]
    missing_fields = dict.fromkeys(set(json_details(dummy_addr))-set(json_input), 'NA')
    keys = list(json_input)
    fields = dupe_remove(list(json_input.values()))
    return jsonify({**dict(zip(keys, fields)), **missing_fields})
