# GitHub 创建仓库 - 详细步骤

## 📋 第一步：访问 GitHub

1. **打开浏览器**，访问：https://github.com

2. **登录账号**：
   - 如果已有账号，点击右上角 "Sign in" 登录
   - 如果没有账号，点击 "Sign up" 注册（免费）

---

## 🆕 第二步：注册账号（如果没有账号）

### 注册步骤：

1. 点击 "Sign up"
2. 填写信息：
   - **Username**（用户名）：选择一个唯一的用户名，例如：`zhangsan` 或 `yourname`
   - **Email**（邮箱）：输入你的邮箱地址
   - **Password**（密码）：设置密码
3. 验证邮箱（GitHub 会发送验证邮件）
4. 完成注册

---

## ➕ 第三步：创建新仓库

### 详细步骤：

1. **登录后，点击右上角的 "+" 号**
   - 在页面右上角，你会看到一个 "+" 号
   - 点击它，会显示下拉菜单

2. **选择 "New repository"**
   - 在下拉菜单中，点击 "New repository"
   - 或者直接访问：https://github.com/new

3. **填写仓库信息**：

   **Repository name（仓库名称）**：
   - 输入：`personal-resume`（或你喜欢的名称）
   - 建议使用小写字母和连字符，例如：`personal-resume`、`my-resume`、`resume-website`

   **Description（描述）**（可选）：
   - 可以填写：`个人简历网站` 或 `Personal Resume Website`
   - 也可以留空

   **Visibility（可见性）**：
   - ✅ **选择 "Public"**（公开）
     - 这样 Vercel 可以免费部署
     - 你的代码会公开，但这是正常的（很多人都是公开的）
   - ❌ 不要选择 "Private"（私有，需要付费）

   **⚠️ 重要：不要勾选以下选项**：
   - ❌ **不要勾选** "Add a README file"
   - ❌ **不要勾选** "Add .gitignore"
   - ❌ **不要勾选** "Choose a license"
   
   **原因**：你的项目已经有这些文件了，如果勾选会冲突

4. **点击绿色的 "Create repository" 按钮**

---

## ✅ 第四步：仓库创建成功

创建成功后，你会看到一个页面，显示：

```
Quick setup — if you've done this kind of thing before
```

**不要按照这个页面的说明操作！** 因为我们已经准备好了代码。

---

## 📝 创建仓库时的注意事项

### ✅ 正确的设置：

- Repository name: `personal-resume`（或你喜欢的名称）
- Description: 可选，可以填写 `个人简历网站`
- Public: ✅ 选择公开
- README: ❌ 不勾选
- .gitignore: ❌ 不勾选
- License: ❌ 不勾选

### ❌ 常见错误：

1. **勾选了 "Add a README file"**
   - 会导致推送代码时冲突
   - 解决方法：删除仓库重新创建，或者不勾选

2. **选择了 Private**
   - 免费账号的私有仓库有限制
   - Vercel 部署公开仓库更方便

3. **仓库名称包含空格或特殊字符**
   - 建议使用：`personal-resume`、`my-resume`
   - 避免使用：`personal resume`（有空格）

---

## 🎯 创建完成后

创建完成后，你会看到仓库页面，URL 类似：
```
https://github.com/你的用户名/personal-resume
```

**记住这个 URL，下一步推送代码时会用到！**

---

## 📸 创建仓库的界面说明

当你点击 "New repository" 后，会看到这样的界面：

```
┌─────────────────────────────────────┐
│ Repository name *                   │
│ [personal-resume____________]        │
│                                     │
│ Description (optional)              │
│ [个人简历网站_______________]        │
│                                     │
│ ○ Public                            │
│   Anyone on the internet can see   │
│                                     │
│ ○ Private                           │
│   You choose who can see and commit │
│                                     │
│ ☐ Add a README file    ← 不要勾选  │
│ ☐ Add .gitignore       ← 不要勾选  │
│ ☐ Choose a license     ← 不要勾选  │
│                                     │
│        [Create repository]          │
└─────────────────────────────────────┘
```

---

## 🚀 下一步

创建仓库后：

1. **记住你的仓库名称**（例如：`personal-resume`）
2. **记住你的 GitHub 用户名**
3. **运行 `Git推送助手.bat`** 来推送代码

---

## ❓ 遇到问题？

### Q: 提示 "Repository name already exists"？
A: 这个仓库名称已被使用，换一个名称，例如：`personal-resume-2024`

### Q: 创建后看不到仓库？
A: 刷新页面，或者检查是否登录了正确的账号

### Q: 不小心勾选了 README？
A: 可以删除仓库重新创建，或者推送代码时解决冲突

---

**创建完成后告诉我，我帮你继续下一步！** 🎉

