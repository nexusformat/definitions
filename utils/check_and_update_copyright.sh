#!/bin/bash

# Set the target folder
folder="contributed_definitions"

# Get the current year
current_year=$(date +'%Y')

# List of authors whose starting date can be updated
allowed_authors=(
  "cmmngr"
  "domna"
  "Florian Dobener"
  "mkuehbach"
  "markus.kuehbach"
  "Markus Kühbach"
  "kuehbachm"
  "lukaspie"
  "Lukas Pielsticker"
  "rettigl"
  "Ron Hildebrandt"
  "Rubel"
  "RubelMozumder"
  "RubelMozumder"
  "Sandor Brockhauser"
  "sanbrock"
  "Sherjeel Shabih"
)

#!/bin/bash

# Set the target folder
folder="contributed_definitions"

# Get the current year
current_year=$(date +'%Y')

# List of authors whose starting date can be updated
allowed_authors=(
  "cmmngr"
  "domna"
  "Florian Dobener"
  "mkuehbach"
  "markus.kuehbach"
  "Markus Kühbach"
  "kuehbachm"
  "lukaspie"
  "Lukas Pielsticker"
  "rettigl"
  "Ron Hildebrandt"  
  "Rubel"
  "RubelMozumder"
  "sanbrock"
  "Sandor Brockhauser"
  "Sherjeel Shabih"

)

# Array to hold files that had the start year updated
updated_files=()

# Iterate over each XML file in the folder
for file in "$folder"/*.xml; do
  # Get the first commit year and first author for the file
  first_commit_info=$(git log --diff-filter=A --follow --date=short --pretty=format:'%ad %an' -- "$file" | head -n 1)
  
  # Extract the first commit year and author
  first_commit_year=$(echo "$first_commit_info" | cut -d ' ' -f 1 | cut -d '-' -f 1)
  first_author=$(echo "$first_commit_info" | cut -d ' ' -f 2-)

  # Check if we got a valid year (if no commits are found, skip the file)
  if [ -z "$first_commit_year" ]; then
    continue
  fi

  # Always update the copyright end year to the current year
  if grep -qE "Copyright \(C\) [0-9]{4}-[0-9]{4\}" "$file"; then
    # Update the copyright end year for all files
    sed -i "s/\(Copyright (C) \)[0-9]\{4\}-[0-9]\{4\}/\1$first_commit_year-$current_year/" "$file"
    
    # Print the update message and the new copyright
    new_copyright="$first_commit_year-$current_year"
    echo "Updated copyright end year for: $file (New copyright: $new_copyright)"
  fi

  # If the author is in the allowed list, update the copyright start year as well
  if [[ " ${allowed_authors[@]} " =~ " ${first_author} " ]]; then
    if grep -qE "Copyright \(C\) [0-9]{4}-[0-9]{4\}" "$file"; then
      # Update the copyright start year
      sed -i "s/\(Copyright (C) \)[0-9]\{4\}-[0-9]\{4\}/\1$first_commit_year-$current_year/" "$file"
      
      # Print the update message and the new copyright
      new_copyright="$first_commit_year-$current_year"
      echo "Updated copyright start and end years for: $file (New copyright: $new_copyright)"
      
      # Add to updated files list
      updated_files+=("$file (First commit by $first_author in $first_commit_year)")
    fi
  fi
done

# Print all files that had the start year updated
if [ ${#updated_files[@]} -gt 0 ]; then
  echo "Files with updated copyright start years:"
  for file in "${updated_files[@]}"; do
    echo "$file"
  done
else
  echo "No files were updated."
fi

