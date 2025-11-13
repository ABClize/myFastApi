# FastAPI 学习引导

> 本文档面向第一次接触 FastAPI 的学习者，帮助你迅速了解官方源码仓库的结构，并一步步搭建属于自己的示例项目。

## 1. 仓库整体结构速览

```text
fastapi/
├── applications.py     # `FastAPI` 应用类的具体实现
├── routing.py          # 路由系统与 `APIRouter`
├── dependencies/       # 依赖注入工具函数
├── params.py           # 参数声明与校验
└── ...
docs_src/               # 教程示例源码，阅读与动手实践的最佳入口
tests/                  # 官方测试用例，展示了各类框架特性
```

- **`fastapi/`**：框架核心源码。重点关注 `applications.py`（应用创建流程）和 `routing.py`（路径操作注册）。
- **`docs_src/`**：与官方文档配套的可运行示例。遇到陌生特性时先搜索此目录，通常能找到最小可运行示例。
- **`tests/`**：覆盖面非常全的自动化测试，你可以通过阅读测试了解框架的设计意图。

## 2. 推荐的学习顺序

1. **运行最小示例**：
   ```bash
   uvicorn docs_src.hello_world:app --reload
   ```
   进入 <http://127.0.0.1:8000> 体验响应效果，再访问 `/docs` 查看自动生成的交互式文档。
2. **理解应用入口**：打开 `fastapi/applications.py`，重点关注 `FastAPI` 类的初始化参数和 `include_router()` 等方法。
3. **掌握路由拆分**：阅读 `fastapi/routing.py` 中 `APIRouter` 的实现，结合 `docs_src/tutorial/bigger_applications` 示例练习模块化组织。
4. **学习依赖注入**：从 `docs_src/dependencies/` 开始，逐步过一遍函数依赖、类依赖和子依赖的写法，再回到 `fastapi/dependencies/utils.py` 看内部解析过程。
5. **探索进阶特性**：如后台任务、WebSocket、事件生命周期等，对应的示例都在 `docs_src/` 目录中。

## 3. 自主练习建议

- **搭建 CRUD Demo**：以 `docs_src/sql_databases` 为基础，自己实现一个带数据库的增删改查服务。
- **增加中间件**：尝试编写自定义中间件（可参考 `fastapi/middleware`），例如请求耗时统计。
- **编写测试**：使用 `pytest` 和 `httpx.AsyncClient` 为你的接口写测试用例，参考 `tests/` 目录的写法。

## 4. 阅读源码的小技巧

- 善用搜索：例如使用 `rg "include_router" fastapi` 快速找到相关定义。
- 对照文档：官方站点的教程与 `docs_src/` 的文件一一对应，可以边看源码边运行示例。
- 画流程图：理解请求从 `FastAPI` 入口到路由匹配、依赖解析、响应返回的整体过程，有助于掌握框架核心思想。

## 5. 后续学习方向

- **性能优化**：了解 Uvicorn、Starlette 与 FastAPI 的关系，探究异步 IO 模型。
- **部署实践**：尝试使用 Docker 或云服务部署示例项目。
- **社区资源**：关注官方 GitHub Issues、讨论区以及更新日志，了解最新功能与最佳实践。

祝你学习顺利，早日构建出属于自己的 FastAPI 应用！

## 附录：快速整理本地 Git 仓库

如果你和本指南一样，希望把官方仓库当作学习项目使用，可以按以下顺序「清理」本地 Git 分支：

1. **确认当前工作分支**：在终端运行 `git status`，保证工作区干净。
2. **覆盖 `master`**：若当前分支包含你想保留的改动，执行 `git branch -m master` 将其直接重命名为 `master`。
3. **删除多余分支**：通过 `git branch` 检查是否仍有其他本地分支，可使用 `git branch -D 分支名` 删除。
4. **同步远端（可选）**：若需要推送到远程仓库，使用 `git push origin master --force` 覆盖远端历史，并逐个删除不需要的远端分支。

> 提示：任何带有 `--force` 的操作都可能重写历史，推送前务必确认协作者不会受到影响。

