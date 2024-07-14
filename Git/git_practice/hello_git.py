#在终端文件夹位置去输入git init 去建立一个空仓库，仓库是被Git主动追踪的一组文件
# Git用来管理仓库的文件都存储在隐藏的目录.git中，不要删除，会丢失所有记录

#执行命令 git commit -m "Started project." 执行提交命令，并将"Started project."消息记录在历史记录中
#git statues 查看git仓库状态

#git log
#git log --pretty=oneline

print("Hello Git World!")
print("Hello everyone.")

print("Oh no, I broke the project!")

#放弃最后一次对git的提交
#git restore .
#会将最后一次git前的东西全部撤回，所以不知道在某行添加或修改的代码可以直接restore


#检验出以前的提交
#每次提交都会生成一个新的一长串唯一的密钥，即使你restore . 后也能查的出来
#git log --pretty=oneline
#git checkout git引用ID的前六位 ，可以是最后一次提交的，也可以是之前的提交
#检查出之前的提交，将离开分支main，即分离头指针（detached HEAD），若要回到main分支输入 git switch -
#也可以回到之前的分支去编辑，之后再去提交你的修改

print("sbsb")


#可以使用如下命令去让项目回到你想让他到达的分支
#git log --pretty=oneline
#git reset --hard "前六位提交命令引用的唯一ID"
#这样在这个ID之前的其他提交操作的ID会被全部清除掉。


#清除仓库
#可以直接打开文件浏览器将.git目录删除
#rm -rf .git/  删除该文件夹意味着删除整个仓库