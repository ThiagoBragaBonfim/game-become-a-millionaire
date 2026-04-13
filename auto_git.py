import os

commit = input("Informe o texto do commit: ")

os.system("git status")
os.system("git add .")
os.system("git status")
os.system(f'git commit -m "{commit}"')
# os.system("git push")