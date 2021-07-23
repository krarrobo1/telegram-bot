def get_resource_name(uri):
    resource = uri.split("#")[-1]
    clean = ''.join([i for i in resource if not i.isdigit()])
    return clean
