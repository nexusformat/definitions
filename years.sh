
git ls-tree --name-only -r HEAD > all-files.txt
for i in $(cat all-files.txt); do grep -l 'Copyright.*NIAC' $i; done > all-niac.txt
for i in $(cat all-niac.txt); do msg=$(grep 'Copyright.*NIAC' $i | sed -E -e 's/.* ([12][0-9]{3,})-.*/\1/'); echo "$i $msg"; done > e-years.txt
for i in $(cat all-niac.txt); do msg=$(git log --follow --diff-filter=A --find-renames=65% --pretty=format:"%cs" -- $i | tail -1 | cut -d- -f1); echo "$i $msg"; done > n-years.txt
