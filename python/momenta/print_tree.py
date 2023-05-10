#!/usr/bin/python

'''
def set_node_level(node, level):
    node['level'] = level
    for sub_node in node['sub_nodes']:
        if sub_node['type'] == 'directory':
            set_node_level(sub_node, level+1)
        else:
            sub_node['level'] = level + 1
'''

def generate_prefix(level):
    prefix = ''
    while level > 0:
        prefix += '--'
        level -= 1
    return prefix

def print_node(node):
    #set_node_level(node, 0)
    _print_node(node, 0)

def _print_node(node, level):
    print('{}{}'.format(generate_prefix(level), node['name']))
    if node['type'] == 'directory':
        for sub_node in node['sub_nodes']:
            if sub_node['type'] == 'directory':
                _print_node(sub_node, level+1)
            else:
                print('{}{}'.format(generate_prefix(level+1), sub_node['name']))

def total_size(node):
    size = 0
    for sub_node in node['sub_nodes']:
        if sub_node['type'] == 'directory':
            size += total_size(sub_node)
        else:
            size += sub_node['size']
    return size


if __name__ == '__main__':
    node = {
            'name':'a',
            'type':'directory',
            'sub_nodes':[
                {
                    'name':'b',
                    'type':'file',
                    'size':10,
                },
                {
                    'name':'c',
                    'type':'directory',
                    'sub_nodes':[
                        {
                            'name':'e',
                            'type':'file',
                            'size':30,
                        },
                        {
                            'name':'f',
                            'type':'file',
                            'size':40,
                        }
                    ],
                },
                {
                    'name':'d',
                    'type':'file',
                    'size':20,
                },
            ]
        }
    print('total size: {}'.format(total_size(node)))
    print_node(node)
