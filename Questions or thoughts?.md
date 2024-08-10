- [ ] expt1: keep codes folder in a separate parent folder. Folder structure as below and each folder will be independent git repos (no need of subtree)
	- Two parent folders named: obsidian_notes and codes
Subfolders in each parent folder: project1, project2, project3
![](images/Questions%20or%20thoughts?%2010Aug24_03-17.excalidraw)
- [ ] expt2: keep code folder of each project as a subfolder of the project, this subfolder will be hosted as separate git repo using *subtree*.
![](images/Questions%20or%20thoughts?%2010Aug24_03-28.excalidraw)
- [?] **Comparison:**

| exp1                                                         | exp2                                                                         |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| + simple                                                     | - complex : need for subtree                                                 |
|                                                              | - subtree wont be synced automatically updated                               |
| - 3 folders for each project including quarto_webpage folder | + all folders related to a project in 1 place (except quarto_webpage folder) |
IF folders at under 2 parent folders (exp1) is not that messy, let's go for it since it is simple - git.
