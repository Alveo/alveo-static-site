import re
import sys
import os
import shutil


image_re = r'!\[(.*)\]\(http://[a-z.]+/wp-content/uploads/(.*)\)'

# match links within the site
link_re = r'\[(.*)\]\(http://[a-z.]+/(.*)/ "(.*)"\)'

link_no_title_re = r'\[(.*)\]\(http://[a-z.]+/(.*)/\)'

tag_re = r'</?[^>]+>'


def process(filename):
    backup = filename + '.bak'

    shutil.copy(filename, backup)

    with open(filename, 'w') as output: 
        with open(backup) as fd:
            for line in fd:
                line = line.replace('</div>', '\n\n')
                line = re.sub(link_re, r'[\1](/\2 "\3")', line)
                line = re.sub(link_no_title_re, r'[\1](/\2)', line)
                line = re.sub(image_re, r'![\1](assets/files/\2)', line)
                line = re.sub(tag_re, '', line)
                if line.startswith('id:'):
                    continue
                if line.startswith('guid:'):
                    continue
                output.write(line)


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        print('Processing', filename)
        process(filename)