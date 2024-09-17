# touch command equivalent for CMD  

In a bash shell it's easy to create a new empty file with: 

```bash
$ touch new_empty_file.txt
$ ls
new_empty_file.txt
```
A similar thing can be achieved in Windows command prompt (CMD) with this 
[hack](https://stackoverflow.com/questions/30011267/create-an-empty-file-on-the-commandline-in-windows-like-the-linux-touch-command/72160305#72160305).
It does throw an error but it creates the empty file anyway.

```shell
> .>new_empty_file.txt
'.' is not recognized as an internal or external command,
operable program or batch file.
> dir

 Volume in drive C is OSDisk
 Volume Serial Number is ...

 Directory of C:\...\

17/09/2024  08:12    <DIR>          .
17/09/2024  08:12    <DIR>          ..
17/09/2024  08:12                 0 new_empty_file.txt
```
So basically you just replace `touch` with `.>`