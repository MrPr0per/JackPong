import os

compiler_filepath = r'D:\code\nand2tetris\n2t-software-suite\JackCompiler.bat'
current_folder = os.getcwd()
os.system(rf'{compiler_filepath} {current_folder}')
