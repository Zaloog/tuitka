OPTION_TREE = {
    'Control the inclusion of modules and packages in result': [
        {
            'flag':'--include-package',
            'type': 'list',
            'default': [],
        },
        {
            'flag':'--include-modules',
            'type': 'list',
            'default': [],
        },
        {
            'flag':"--prefer-source-code",
            'type': 'bool',
            'default': True,
        }
    ],

    'Compilation choices': [
        {
            'flag':'--file-reference-choice',
            'type': 'list',
            'default': [],
            'choices': ['original', 'runtime', 'frozen'],
        },
    ],
    'Output choices': [
        {
            'flag':'--output-filename',
            'type': 'string',
            'default': '',
        },
        {
            'flag':'--output-dir',
            'type': 'path',
            'default': '',
        },
        {
            'flag':"--remove-output",
            'type': 'bool',
            'default': False,
        }
    ],


}
