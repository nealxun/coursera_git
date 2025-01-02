### A list of completed open source courses
- 2023-01-01 Python cursh course.
- 2023-02-01 Speaking and presenting poise.
- 2023-04-01 Using python to interact with the operating system.
- 2023-05-01 ChatGPT promoting engineering.
- 2023-07-01 Speaking and Presenting Conversation_Starters.
- 2023-11-01 Generative AI for Everyone.
- 2023-12-01 AI for public health.
- 2023-12-01 Speaking and preseting pitches and persuasion.
- 2024-03-01 Sequence timeseries and prediction.
- 2024-04-01 Speaking and presenting tact.
- 2024-05-01 Forecasting skills: see the future before it happens.
- 2024-06-01 Prompting engineering for ChatGPT.
- 2024-08-01 AI python for beginners.


### Basic git operations
+ In Visual studio code, click explore, then open a folder, this will be the work directory and you can initiate a git project.
+ In Visual studio code, terminal -> new terminal, to open a command line window.
+ In the terminal, use `git config --list` to see the configuration.
+ In the terminal, use `git init` to initialize a project.
+ In the terminal, staging files: `git add FILENAME`, make a commit: `git commit -m “commit message”`. Use `git add .` to add all the files.
  - To amend the previous commit message, use `git commit --amend -m "an updated commit message"`.
+ To create a remote.
  - First create a repo in GitHub.
  - Pushing to GitHub.
    + Add a remote, `git remote add origin YOUR URL`. (make sure to select the https one).
    + Git push, `git push -u origin main` (first time push), `git push --all` (push all the branches), `git push origin master` (push your master branch to your origin server).
+ To work with remote.
  - Show the remote, `git remote -v`.
  - Get data from your remote, `git fetch <remote name, i.e origin>`. This will only download the data.
  - Sync from your remote, `git pull <remote name>`. This will fetch and then merge that remote branch into your current branch.
  - See more information about a remote, `git remote show <remote>`.
+ To contribute to an existing project.
  - First fork the project, it will take to your own project page.
  - Clone a git repo, `git clone <url>`. Then change the work directory accordingly.
  - Check out a new branch, `git checkout -b <new branch name>`.
  - Push to remote, `git push origin <new branch name>`.
  - Open the pull request on github.
+ To show commit history, `git log --pretty=oneline`.
+ To delete the most recent commit, `git reset --hard HEAD~1`.
+ To undo a reset, `git reset --hard <sha1 of desired commit>`. Use `git reflog` to get the sha1.

### Basic python operations
+ Bulk commenting, use `cmd+/`.
