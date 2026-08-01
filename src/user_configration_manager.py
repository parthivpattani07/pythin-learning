test_settings={
    'theme':'light'
}
test_tuple=('THEME','dark')
    
    
    
def add_setting(settings_dict,kv_tuple):
    
    raw_key, value = kv_tuple
    key = raw_key.lower()
    if key in settings_dict:
        return ( f 'Setting {raw_key} already exists! Cannot add a new setting with this name.')
    settings_dict[key] = value
    return (f"Setting {key} successfully added!")

    


print(add_setting(test_settings,test_tuple))

