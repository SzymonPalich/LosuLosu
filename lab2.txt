mkdir LAB02
cd LAB02
git init
touch README.txt
git add README.txt
git commit -m 'Dodano plik readme'
git log
touch license.txt
vi license.txt
git add license.txt
git status
git commit -m  'New commit'
vi license.txt
git add license.txt
git commit --amend
