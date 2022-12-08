Background: We have many large files - some up to a couple of GB. Some are image files, and some contain derived data. For efficient use of disk space, duplicates should be replaced with a hard link.

Details: For files within a user-specified directory, such as /mnt/data (/FolderParent/FolderA/), find all files that are larger than a user-specified size, such as 1 MB. (Small text files may happen to be identical, but we may not want them to be linked. For this task, allow a lower limit size threshold to be specified.) For all files larger than the threshold, search for files with the same filename in elsewhere within the directory tree. If found, and if they are not already hard links to each other, then use a system check (such as diff/md5sum) to confirm if the files are identical. If they are, make one a hard link to the other. This tool will likely heavily leverage the linux "find" command.

Output: Report how many files were consolidated, and how much disk space was saved.


FolderParent
        -FolderA
            -FileA.tiff (1 GB)
        -FolderB
            -FolderC
                -FileA.tiff
                -FileB.tiff
                -FileC.tiff
        -FolderD
            -FolderE
                -FileB.tiff
                -FolderF
                    -FileA.tiff
