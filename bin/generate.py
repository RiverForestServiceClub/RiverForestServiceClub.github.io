#!/usr/bin/env python

from Cheetah.Template import Template
import os
import os.path
import time

OUTPUT_DIR=".."
INPUT_DIR="."

def template_to_output(filename):
    return os.path.join(OUTPUT_DIR, filename.replace(".tmpl", ".html"))

class generator(object):
    def __init__(self):
        self.header = str(self.run_template("header.incl"))
        self.footer = str(self.run_template("footer.incl"))

    def run_template(self, path):
        last_modified = time.strftime("%d %B %Y", time.gmtime(os.path.getmtime(path)))
        t = Template(file=path)
        t.last_modified = last_modified
        return t

    def generate_file(self, root, path, filename):
        path = os.path.join(root, filename)
        print path
        print template_to_output(path)
        out = open(template_to_output(path), "w")
        out.write(self.header)
        out.write(str(self.run_template(path)))
        out.write(self.footer)

    def walk(self):

        for root, dirs, files in os.walk(INPUT_DIR):
            path = root.split('/')
            for filename in files:
                if filename.endswith(".tmpl"):
                    self.generate_file(root, path, filename)

if __name__ == '__main__':
    generator().walk()
    


