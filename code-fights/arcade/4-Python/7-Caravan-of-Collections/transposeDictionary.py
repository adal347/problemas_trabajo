def transposeDictionary(scriptByExtension):
    return sorted([[value, key] for key, value in scriptByExtension.items()])
