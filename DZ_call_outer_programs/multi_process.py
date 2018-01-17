import os
import multiprocessing
import subprocess

def resize_file(file_name, source_dir, result_dir):
    print('Process {} has started!'.format(os.getpid()))
    command = 'cp {} {}'.format(os.path.join(source_dir, file_name), os.path.join(result_dir, file_name))
    subprocess.call(command, shell=True)
    subprocess.call('sips --resampleWidth 200 {}'.format(os.path.join(result_dir, file_name)), shell=True)
    print('Process {} ends!'.format(os.getpid()))


abs_dir_path = os.path.abspath(os.path.dirname(__file__))
source_dir = os.path.join(abs_dir_path, 'Source')
result_dir = os.path.join(abs_dir_path, 'Result')

gen = (file_name for file_name in os.listdir(source_dir))

for file_name in os.listdir(source_dir):
    p1 = multiprocessing.Process(target=resize_file, args=(file_name, source_dir, result_dir))
    p1.start()