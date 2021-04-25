import subprocess
import os

CPP_EXT = '.cpp'
PY_EXT = '.py'

class Executor:
    def __init__(self, file):
        self.file = file

        if self.file.endswith(CPP_EXT):
            self.file_root = self.file[ : -len(CPP_EXT)]
            
            compile = subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-o', self.file_root, self.file])
            assert compile.returncode == 0
            
            self.exec = ['./' + self.file_root]

        else:
            self.exec = ['python3', self.file]

    def run(self, args=[], **kwargs):
        kwargs.setdefault('text', True)

        # print(self.exec + args)
        exe = subprocess.run(self.exec + args, **kwargs)

        if self.file.endswith(CPP_EXT):
            os.system('rm -f ./' + self.file_root)
        assert exe.returncode == 0
