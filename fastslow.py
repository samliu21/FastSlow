import sys
import os
from Executor import Executor


in_file = open('in', 'w+')
slow_out = open('slow.out', 'w+')
fast_out = open('fast.out', 'w+')


def end_program():
    in_file.close()
    slow_out.close()
    fast_out.close()


def main(args):
    if len(args) < 5:
        print('A generator, two solutions, and the number of cases is required')
        return 1

    _, gen_file, slow_file, fast_file, T = args
    

    gen = Executor(gen_file)
    slow = Executor(slow_file)
    fast = Executor(fast_file)

    for i in range(int(T)):
        gen.run(stdout=in_file)
        in_file.seek(0)
        slow.run(stdin=in_file, stdout=slow_out)
        in_file.seek(0)
        fast.run(stdin=in_file, stdout=fast_out)
        slow_out.seek(0)
        fast_out.seek(0)

        if slow_out.read() != fast_out.read():
            print('Failed on case', i + 1, 'of', T, '\n')
            print('INPUT')
            os.system('cat in')
            print('\nSLOW OUTPUT')
            os.system('cat slow.out')
            print('\nFAST OUTPUT')
            os.system('cat fast.out')
            print('\nDIFFERENCE')
            os.system('diff -c slow.out fast.out')
            end_program()
            sys.exit()

    end_program()
    sys.exit()


main(sys.argv)


