import json
import collections

def buildCommand(jsonFile):
    def cleanJson(obj):
        if type(obj) is str:
            return ""
        if type(obj) is int:
            return 0
        if type(obj) is list:
            return []
        if type(obj) is float:
            return 0
        for k, v in obj.items():
            obj[k] = cleanJson(v)
        return obj

    build = json.loads(jsonFile, object_pairs_hook = collections.OrderedDict)
    build = cleanJson(build)

    return json.dumps(build, sort_keys = False)
