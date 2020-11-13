import os

import numpy as np
import pandas as pd

import bibtexparser

def bibtex_to_md(input_dir,
                 output_dir=None,
                 style='MLA',
                 sort='date',
                 ascend=False):

    if output_dir is None:
        output_dir = os.path.splitext(input_dir)[0] + '.md'

    with open(input_dir, 'r') as bibtex:
        bibtex_list = bibtexparser.load(bibtex).entries
        md = ''

        if style == 'MLA':
            for idx, i in enumerate(bibtex_list):
                try:
                    entry = '{}. "{}". *{}*, {}.{} ({}): {}'.format(
                        i['author'],
                        i['title'].replace('{', '').replace('}', ''),
                        i['journal'] if 'journal' in i else '',
                        i['volume'] if 'volume' in i else '',
                        i['number'] if 'number' in i else '',
                        i['year'] if 'year' in i else '',
                        i['pages'] if 'pages' in i else ''
                    )
                    if 'url' in i:
                        entry = '[{}]({})'.format(entry, i['url'].split(' ')[0])
                    md += '{}. '.format(idx + 1)
                    md += entry
                    md += '\n'
                except:
                    print('Incomplete field')
    
    print(md)
    with open(output_dir, 'w') as output:
        output.write(md)

                
        

if __name__ == '__main__':
    bibtex_to_md('./ref.bib')