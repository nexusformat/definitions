#!/bin/bash

# Define folders to check
folders=("applications" "base_classes" "contributed_definitions")

# Get the current year
current_year=$(date +'%Y')

# List of authors whose starting date can be updated
allowed_authors=(
  "Andrea Albino"
  "aalbino2"
  "andreaa93"
  "ca-palma"
  "Carola Emminger"
  "cmmngr"
  "Florian Dobener"
  "domna"
  "Lukas Pielsticker"
  "lukaspie"
  "Laurenz Rettig"
  "rettigl"
  "Marie Yao"
  "Markus Kühbach"
  "atomprobe-tc"
  "kuehbachm"
  "markus.kuehbach"
  "mkuehbach"
  "Ron"
  "Ron Hildebrandt"
  "Rubel"
  "RubelMozumder"
  "Sandor Brockhauser"
  "sanbrock"
  "Sherjeel Shabih"
  "Tommaso-Pincelli"
  "Tommaso"
  "Yichen"
)


# Iterate over each folder
for folder in "${folders[@]}"; do
  # Iterate over each XML file in the folder
  for file in "$folder"/*.xml; do
    # Skip if no XML files are found
    [[ -e "$file" ]] || continue

    # Get the first commit year and author for the file
     first_commit_info=$(git log --diff-filter=A --follow --name-status --date=short --pretty=format:'%ad %an' -- "$file" | head -n 1)

    # Extract the first commit year and author
    first_commit_year=$(echo "$first_commit_info" | awk '{print $1}' | cut -d '-' -f 1)
    first_author=$(echo "$first_commit_info" | cut -d ' ' -f 2-)

    # Check if we got a valid year (if no commits are found, skip the file)
    if [ -z "$first_commit_year" ]; then
      continue
    fi

    # Extract the existing copyright from the file
    old_copyright=$(grep -oE "Copyright \(C\) [0-9]{4}-[0-9]{4}" "$file" | head -n 1)

    # Extract the existing start and end years
    old_start_year=$(echo "$old_copyright" | cut -d ' ' -f 3 | cut -d '-' -f 1)
    old_end_year=$(echo "$old_copyright" | cut -d ' ' -f 3 | cut -d '-' -f 2)

    # Default: assume start year is unchanged
    start_year_changed="No"

    # Determine whether to update the start year
    if [[ " ${allowed_authors[@]} " =~ " ${first_author} " ]]; then
      if [[ "$old_start_year" != "$first_commit_year" ]]; then
        start_year_changed="Yes"
        old_start_year="$first_commit_year"  # Update the start year
      fi
    else
      echo "Keeping old start year for $file (Original author: $first_author)"
    fi

    # Update the end year to current year
    new_copyright="Copyright (C) $old_start_year-$current_year"

    # Replace copyright in the file
    sed -i "s/Copyright (C) [0-9]\{4\}-[0-9]\{4\}/$new_copyright/" "$file"

    # Print summary
    echo "File: $file"
    echo "Old copyright: $old_copyright"
    echo "New copyright: $new_copyright"
    echo "Start year changed: $start_year_changed"
    echo "--------------------------------------"
  done
done
