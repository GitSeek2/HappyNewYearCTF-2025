# 贡献指南

😍 欢迎你的贡献，你可以为 HappyNewYearCTF 2025 做这些：

- 新增题目
- 新增基础镜像
- 修复问题
- 提出优化建议
- ...

以下内容可以帮助你理解 HappyNewYearCTF 2025 和如何贡献。

## 一、题目类别

HappyNewYearCTF 包含常见的 CTF 题目类别，包括 Web、Pwn、Reverse、Crypto、Misc，其中主要是 Web & Misc。

如果你希望加入更多题目类别或添加新的题目，欢迎提交 issue/PR。

## 二、出题流程

工作流：**fork** -> **clone** -> **branch** -> **dev** -> **push** -> **PR**。

### 1. fork 本项目

点击仓库右上角 Fork 按钮创建属于你的副本。

### 2. clone 仓库

clone 你的 fork 仓库到本地。

```bash
git clone https://github.com/<你的 GitHub 用户名>/HappyNewYearCTF.git
cd HappyNewYearCTF-2025
```

### 3. 新建分支

```bash
git checkout -b <分支名>
```

分支名建议遵循 `<题目类型>-<出题人ID>-<简短题目名>` 格式，例如 `web-zqingz-warmup`。

### 4. 创建题目

在对应题目分类目录下创建题目文件夹，文件夹下创建 `README.md` 文件，并填写题目信息，内容参考 `templates` 目录下的题目模板。

因为项目根目录下的 `.gitignore` 文件中添加了 `tmp/` 目录，所以你在 pull 本项目后可以新建 `tmp` 目录用于临时测试题目，git 将不会跟踪 `tmp` 目录下的文件。

### 5. 提交修改

提交修改到你的 fork 仓库。

```bash
git add .
git commit -m "add(<题目类型>): <题目名>"
git push origin <分支名>
```

提交信息遵循 `add (<题目类型>)：<题目名>` 格式，例如 `add(web): warmup`。

### 6. 创建 pull request

前往 GitHub 你的 Fork 仓库，

点击 `Contribute` 按钮 -> 点击 `Open pull request` 按钮，

标题（title）默认即可，描述（description）随意发挥，

最后点击 `Create pull request` 按钮，over~

## 三、题目规范

### 1. 出题动机

出题应当出于这样的动机：

- 帮助新生认识 CTF
- 帮助新生了解和学习 CTF 中**基础、常见**的知识点

坚决拒绝以下动机：

- 我来考考新生
- 让新生学习**新、难、怪**知识点
- 我最近学习到一个有意思的东西，给新生看看

### 2. 题目形式

HappyNewYearCTF 中的题目形式含以下三种，你应当根据题目类型选择对应的题目形式。

- 静态附件（一般为 Crypto，Misc，Reverse 题目）
- 静态容器（一般为 Pwn，Web 题目）
- 动态容器（一般为 Pwn，Web 题目）

### 3. 容器题目

对于 docker 容器题目，遵循空间占用最小化原则，尽量减少镜像体积，尽量使用项目 base 目录下的基础镜像进行构建。如果 base 目录下没有合适的基础镜像，可以提交 issue 或 PR。

[CSSEC::CTF](https://ctf.cssec.cc) 构建自 [GZCTF](https://github.com/GZTimeWalker/GZCTF)，因此题目需适应 GZCTF 平台的规范，动态容器的 flag 注入变量为 `GZCTF_FLAG`。

部分 Crypto、Misc、Reverse 题目，推荐使用动态容器将动态 flag 注入题目附件，然后通过 http 或 socket 下发题目附件，减少作弊可能。

### 4. 文件结构

题目应当具有合理的文件结构，你可以参考本项目 templates 目录下的题目模板。

### 5. 解题文档

题目应当具有 writeup，格式与内容没有具体要求，易读且**可以让新生读有所获**即可。建议为 markdown 格式，命名为 `WP.md` 放在题目根目录下。如果为其他格式，请转换为 pdf 格式，命名为 `WP.pdf` 放在题目根目录。如果你的 writeup 放在线上，在 `WP.md` 中给出链接即可。
