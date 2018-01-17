import sys
import os
import subprocess

abs_dir_path = os.path.abspath(os.path.dirname(__file__))
source_dir = os.path.join(abs_dir_path, 'Source')
result_dir = os.path.join(abs_dir_path, 'Result')
print(result_dir)

print(os.path.exists(result_dir))

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

for file in os.listdir(source_dir):
    command = 'cp {} {}'.format(os.path.join(source_dir, file), os.path.join(result_dir, file))
    subprocess.call(command, shell=True)
    subprocess.call('sips --resampleWidth 200 {}'.format(os.path.join(result_dir, file)), shell=True)

