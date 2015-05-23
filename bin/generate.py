#!/usr/bin/env python

from Cheetah.Template import Template
import os
import os.path
import time

OUTPUT_DIR=".."
INPUT_DIR="."

def template_to_output(filename):
    return os.path.join(OUTPUT_DIR, filename.replace(".tmpl", ".html"))

def split_path(p):
    a,b = os.path.split(p)
    return (split_path(a) if len(a) and len(b) else []) + [b]

class generator(object):
    def run_template(self, path, home):
        last_modified = time.strftime("%d %B %Y", time.gmtime(os.path.getmtime(path)))
        t = Template(file=path)
        t.last_modified = last_modified
        t.home = home
        t.no_link = "{ font-weight: bold ; text-decoration: none; pointer-events: none; cursor: default;}"
        return t

    def path_to_home(self, root):
        if len(split_path(root)) > 1:
            return os.path.join(*[".."]*(len(split_path(root))-1))
        return "."

    def generate_file(self, root, path, filename):
        path = os.path.join(root, filename)
        print "root:", root
        print "src:", path
        home = self.path_to_home(root)
        print "home", home
        print
        out = open(template_to_output(path), "w")
        header = str(self.run_template("header.incl", home))
        out.write(header)
        out.write(str(self.run_template(path, home)))
        footer = str(self.run_template("footer.incl", home))
        out.write(footer)

    def walk(self):
        for root, dirs, files in os.walk(INPUT_DIR):
            path = root.split('/')
            for filename in files:
                if filename.endswith(".tmpl") and '#' not in filename:
                    self.generate_file(root, path, filename)

if __name__ == '__main__':
    generator().walk()
    


