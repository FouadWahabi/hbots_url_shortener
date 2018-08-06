# -*- coding: utf-8 -*-

def setup_routing(app, routes):
    
    for route in routes:
        # endpoint: (blueprint_instance, url_prefix)
        # rules: [('/route/', view_function), ...]
        endpoint, rules = route[0], route[1:]
        for pattern, view in rules:
            if endpoint is None:
                app.add_url_rule(pattern, view_func=view)
            else:
                endpoint[0].add_url_rule(pattern, view_func=view)
        if endpoint is not None:
            app.register_blueprint(endpoint[0], url_prefix=endpoint[1])
