import os
import multiprocessing
import subprocess

abs_dir_path = os.path.abspath(os.path.dirname(__file__))
source_dir = os.path.join(abs_dir_path, 'Source')
result_dir = os.path.join(abs_dir_path, 'Result')

def resize_file(file_name):
    print('Process {} has started!'.format(os.getpid()))
    command = 'cp {} {}'.format(os.path.join(source_dir, file_name), os.path.join(result_dir, file_name))
    subprocess.call(command, shell=True)
    subprocess.call('sips --resampleWidth 200 {}'.format(os.path.join(result_dir, file_name)), shell=True)
    print('Process {} ends!'.format(os.getpid()))

with multiprocessing.Pool(processes=4) as pool:
    pool.map(resize_file, os.listdir(source_dir))

