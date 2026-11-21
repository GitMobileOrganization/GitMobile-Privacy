# GitMobile Privacy Policy

GitMobile 的在线隐私政策页面，托管在 GitHub Pages，供 Google Play 商店页与应用说明引用。

当前线上地址：`https://gitmobileorganization.github.io/GitMobile-Privacy/`（组织 `GitMobileOrganization`）。

## 文件

| 文件 | 说明 |
| --- | --- |
| `index.html` | 线上页面本体，中英双语，跟随系统语言，可手动切换；GitHub Pages 的入口文件 |
| `PRIVACY.md` | 中文权威文本（与页面中文部分一致），方便在 GitHub 上直接阅读和版本对比 |

## 发布到 GitHub Pages

1. 在 GitHub 新建仓库，建议命名为 `GitMobile-Privacy`（公开仓库）。
2. 把本目录下的 `index.html` 与 `PRIVACY.md` 推到 `main` 分支根目录。
3. 仓库 **Settings → Pages → Build and deployment**：Source 选 `Deploy from a branch`，Branch 选 `main`、目录选 `/ (root)`，保存。
4. 等 1–2 分钟，访问：

   `https://<你的 GitHub 用户名>.github.io/GitMobile-Privacy/`

5. 把该地址填进 Google Play 管理中心 → 应用内容 → 隐私政策。

> GitHub Pages 只认根目录的 `index.html`，所以文件名不要改。若之后绑定自定义域名，在 Pages 里填 Custom domain 并配置 DNS 即可，页面本身不需要改。

## 更新政策

1. 同时修改 `index.html` 的中文段（`<section data-lang="zh">`）与英文段（`<section data-lang="en">`），以及 `PRIVACY.md`。
2. 更新顶部「最后更新」日期（两处语言段 + `PRIVACY.md` 各一处）。
3. 提交后 GitHub Pages 会自动重新发布。

## 维护约定

- 政策描述必须与应用实际行为一致。新增会离开设备的数据路径（例如新的 AI Provider 类型、云同步、崩溃上报）时，先改政策再发版。
- 中文段是权威文本；英文段是同一内容的翻译，两者章节顺序与事实必须一致。
- 页面不引入任何第三方脚本、字体或统计代码，避免隐私政策页面自身产生额外数据收集。

## 本地预览

直接双击 `index.html` 即可在浏览器打开；语言切换与目录锚点在本地文件下同样可用。
