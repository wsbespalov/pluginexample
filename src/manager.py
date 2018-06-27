import os
import sys
import re
import importlib

plugin_dir = 'plugins'

def load_plugins():
    py_search_regexp = re.compile('.py$', re.IGNORECASE)
    plugin_files = filter(py_search_regexp.search,
                          os.listdir(
                              os.path.join(
                                  os.path.dirname(__file__),
                                  plugin_dir)))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, plugin_files)
    importlib.import_module(plugin_dir)
    modules = []
    for plugin in plugins:
        if not plugin.startswith('__'):
            modules.append(importlib.import_module(plugin, package=plugin_dir))

    return modules

pls = load_plugins()

for loaded_plugin in pls:
    print('load plugin object: {}'.format(loaded_plugin))
    loaded_plugin.run()
