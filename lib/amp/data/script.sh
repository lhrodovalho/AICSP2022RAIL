find . -name "*txt" -exec sed -i -e 's/^ //g'   {} \;
find . -name "*txt" -exec sed -i -e 's/  / /g' {} \;
find . -name "*txt" -exec sed -i -e 's/ /,/g'  {} \;

# Rename all *.txt to *.csv
for file in *.txt; do 
    mv -- "$file" "${file%.txt}.csv"
done
