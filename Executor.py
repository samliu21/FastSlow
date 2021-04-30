import subprocess
import os

CPP_EXT = '.cpp'
PY_EXT = '.py'
JAVA_EXT = '.java'

class Executor:
    def __init__(self, file):
        self.file = file

        if self.file.endswith(CPP_EXT):
            self.file_root = self.file[ : -len(CPP_EXT)]
            
            compile = subprocess.run(['g++', '-std=c++17', '-O2', '-o', self.file_root, self.file])
            assert compile.returncode == 0
            
            self.exec = ['./' + self.file_root]

        elif self.file.endswith(PY_EXT):
            self.exec = ['python3', self.file]

        else:
            self.file_root = self.file[ : -len(JAVA_EXT)]

            compile = subprocess.run(['javac', self.file])
            assert compile.returncode == 0

            self.exec = ['java', self.file_root]

    def run(self, args=[], **kwargs):
        kwargs.setdefault('text', True)

        # print(self.exec + args)
        exe = subprocess.run(self.exec + args, **kwargs)

        return exe.returncode == 0

    def close(self):
        if not self.file.endswith(PY_EXT):
            os.system('rm -f ' + self.file_root)
            
