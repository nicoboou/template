# Repository Template

Repository to be reused for any project requiring well structured & partitioned files

## Directories

- **src Folder**: The source code folder! However, in languages that use headers (or if you have a framework for your application) don’t put those files in here.
- **test Folder**: Unit tests, integration tests… go here.
- **.config Folder**: It should local configuration related to configuration of project files.
- **.build Folder**: This folder should contain all scripts related to build process (PowerShell, Docker compose…).
- **dep Folder**: This is the directory where all your dependencies should be stored.
- **doc Folder**: The documentation folder
- **static Folder**: For all static resources in your project. For example, images.
- **tools Folder**: Convenience directory for your use. Should contain scripts to automate tasks in the project, for example, build scripts, rename scripts. Usually contains .sh, .cmd files for example.
- **.vscode Folder**: Config dir for local VS Code IDE
- **.github Folder**: Config dir for Github & Gitlab CI-CD
