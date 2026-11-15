# Git Mobile 隐私政策

**生效日期：2026 年 11 月 15 日　　最后更新：2026 年 11 月 15 日**

Git Mobile 会在你的手机上运行一个 Git 服务端，把仓库交给同一网络里的设备访问；你也可以把它当作客户端去连接别的 Git 服务器，或开启 AI 助手。这些功能决定了哪些信息留在手机、哪些会发给别人。本政策逐项说明。

你可以通过下列标题了解我们的做法。如有疑问，请通过文末方式联系我们。

---

## 目录

- [我们是谁](#我们是谁)
- [本政策涵盖什么](#本政策涵盖什么)
- [我们不索取的信息](#我们不索取的信息)
- [应用在你的设备上处理的信息](#应用在你的设备上处理的信息)
- [应用使用的权限](#应用使用的权限)
- [局域网服务与访问者信息](#局域网服务与访问者信息)
- [客户端连接与远程服务器](#客户端连接与远程服务器)
- [AI 功能（可选，仅管理员）](#ai-功能可选仅管理员)
- [诊断信息](#诊断信息)
- [信息的共享](#信息的共享)
- [信息的安全](#信息的安全)
- [保留与删除](#保留与删除)
- [你的权利](#你的权利)
- [处理的法律依据](#处理的法律依据)
- [儿童和个人数据](#儿童和个人数据)
- [不出售、不共享](#不出售不共享)
- [政策变更](#政策变更)
- [与我们联系](#与我们联系)

## 我们是谁

Git Mobile（下称「本应用」）是一款 Android 平台的本地 Git 服务端兼客户端，由 Git Mobile 的独立开发者提供，通过 Google Play 分发。

我们不是云服务提供者：我们不运营接收你仓库、账号或审计记录的服务器。本政策所述的处理，绝大多数发生在你的设备上。你可以通过 Google Play 商品页「开发者联系信息」中公布的邮箱与我们联系。

## 本政策涵盖什么

本政策说明应用在你的设备上处理哪些信息、哪些信息会离开设备、出于什么目的，以及你拥有哪些选择。它适用于 Android 版本。

本政策只在线上提供，应用内不保存副本：你打开的就是当前这一版，不会读到随安装包一起变旧的版本。

它不涵盖以下情形：你把仓库克隆到电脑之后，电脑上的处理；你自行配置的 AI 服务提供方（Provider）对数据的处理；你通过本应用访问的第三方 Git 服务器；以及系统浏览器、分享面板等系统组件自身的行为。

## 我们不索取的信息

本应用没有云端账号，不需要注册或登录我们的服务。应用内的管理员与成员账号只存在于你的手机里，用于控制谁能访问你手机上的仓库。

我们不索取你的姓名、邮箱地址、电话号码或通讯地址，也不收集你的联系人、短信与通话记录、照片与视频、日历、精确位置或广告标识符。

应用内没有广告，没有接入分析、崩溃上报、社交登录或行为追踪类的第三方 SDK。我们不做用户画像，不依据你的使用行为做定向推荐，也不进行自动化决策。你的仓库内容不会被我们用于训练模型，也不会被上传给我们。

## 应用在你的设备上处理的信息

**仓库与 Git 数据。** 你创建或导入的仓库保存在应用私有目录（`files/repos`），包括对象、引用、提交历史与工作区。它们只存在你的手机上；只有你开启服务并授予访问权限后，同一网络里的设备才能通过网络读取或推送。你可以把某个仓库设为「允许匿名只读」，此时同网设备无需账号即可克隆它——公开范围由你决定。

**服务端账号、成员与授权。** 首次初始化会创建管理员账号；你可以添加成员并授予仓库权限。用户名、经 argon2 哈希后的密码、授权关系保存在应用私有数据库（`files/turso/audit.db`）。密码明文不落盘。成员使用密码登录你的服务端，校验只发生在这台手机上。

**审计日志。** 服务运行时会记录：时间、用户名、仓库名、动作（例如登录、引用发现、拉取、推送）、结果、客户端 IP 地址与 HTTP 方法。用途是让你在管理台或应用内看到谁访问了什么、失败发生在哪一步。保留条数可配置，也可以一键清空。这些记录包含**访问者**的 IP 地址，属于他人的信息，详见「局域网服务与访问者信息」。

**HTTPS 证书与 SSH 密钥。** 开启 HTTPS 时，自签证书与私钥在本机生成并保存在应用私有目录；应用会展示证书指纹，供客户端核对。开启实验性 SSH 访问时，主机密钥与你在管理台授权的公钥保存在 `files/ssh.json`。私钥不会离开手机。

**客户端登录凭据。** 当你把本应用当作客户端连接别的服务器时，应用会保存服务器地址、用户名、备注、使用次数与最近使用时间（这些是明文），以及密码或 SSH 私钥（**只以 Android Keystore 加密后的密文保存，明文不落盘**）。解密只在需要登录时进行；开启应用锁时，进入应用需先解锁，设备具备系统认证能力时，查看与使用已保存凭据还需再通过一次系统认证。

**同步任务与设置。** 你发起的同步或克隆任务，其标题、详情、时间与结果保存在私有目录（最多 200 条）。端口、TLS、网络范围、保活、语言、主题、应用锁、AI 配置等设置同样保存在私有目录。

**AI 对话与语义索引。** 对话记录保存在私有目录（`files/ai_chat.json`，最多 50 条），语义索引的向量保存在本机。发送给 AI Provider 的内容见「AI 功能」。

**诊断报告。** 只有你点击「导出诊断报告」时才会生成。内容包括应用版本、私有目录路径、服务状态、证书指纹、审计条数等配置摘要，**不包含密码、令牌或仓库对象内容**。生成后通过系统分享面板交给你选择的 App，或复制到剪贴板。

## 应用使用的权限

每一项权限都只在对应功能被使用时才起作用。拒绝某项可选权限，不会让基础功能整体不可用。

**网络。** `INTERNET` 用于：在本机监听 Git 服务、作为客户端连接你指定的服务器、调用你配置的 AI 服务。

**网络状态。** `ACCESS_NETWORK_STATE` 用于读取当前网络连接状态，以便提示该访问哪个地址、当前是仅本机还是局域网范围。应用不读取流量内容。

**前台服务。** `FOREGROUND_SERVICE` 与 `FOREGROUND_SERVICE_SPECIAL_USE` 用于让 Git 服务在后台常驻（运行在独立的 `:server` 进程），并在通知栏显示运行状态与「停止服务」。

**通知。** `POST_NOTIFICATIONS` 用于显示上述前台服务通知。拒绝后服务仍可运行，但你看不到通知与快捷停止入口。

**生物识别。** `USE_BIOMETRIC` 用于可选的指纹或人脸解锁。生物特征由 Android 系统比对，应用只收到成功或失败，拿不到任何特征数据。

**唤醒锁。** `WAKE_LOCK` 仅在你开启「屏幕常亮」或「Wi-Fi 高性能」等保活选项时持有。

**电池优化。** `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` 用于引导你把应用加入电池优化白名单，必须由系统对话框确认。拒绝不影响基础功能。

**存储。** 应用不申请存储权限。仓库与导出文件都在应用私有目录；分享单个文件时，通过系统 FileProvider 对该文件做一次性授权。

## 局域网服务与访问者信息

启动服务后，应用默认监听所有网络接口（可在设置中切换为「仅本机」），同一网络内的设备可以访问登录页与仓库。仓库默认需要账号与授权；你也可以把某个仓库设为「允许匿名只读」，此后同网设备无需账号即可克隆它——公开范围由你决定，开启前请确认仓库内容是否适合公开。

应用不做外网穿透，也不做任何中继。若你通过路由器端口映射、公网 IP 或内网穿透把服务暴露到互联网，暴露范围与风险由你决定。建议只在可信网络中使用，并优先开启 HTTPS。

审计日志会记录访问者的 IP 地址与访问动作。你作为这个服务端的运营者，应自行确保对成员与访问者的告知，并按最小必要原则使用这些记录；你可以随时清空日志或调低保留条数。

默认的 HTTP 是明文传输，同一网络内的中间设备可能看到传输内容。应用提供自签 HTTPS，客户端可以核对证书指纹后再连接。

## 客户端连接与远程服务器

当你在客户端页填写服务器地址时，应用会把该地址与你的登录凭据发往这台服务器以完成认证。这台服务器可能是另一台运行 Git Mobile 的手机、你自建的 Git 服务，或他人提供的服务。它对数据的处理适用其运营者的政策，不在本政策范围内。

应用不会把你的凭据发往我们，因为我们没有这样的服务器。

## AI 功能（可选，仅管理员）

AI 功能默认关闭，且只对管理员开放；成员账号没有入口，服务端会对非管理员请求返回 403。

你需要自行填写 OpenAI 兼容的接口地址、模型与 API Key。请求由手机直接发往你填写的地址，不经过我们。

开启后，有两类内容会离开手机：

- **语义索引**：应用把仓库文本按固定规则切块（每块约 1200 字符、保留行号），发送给你配置的嵌入模型（Embedding Provider），用于生成向量；
- **AI 助手**：应用把你的对话内容与工具结果（可能包含仓库内容）发送给你配置的对话模型（Chat Provider）。

AI Provider 可能按其自身政策记录、留存这些内容或用于改进其服务，具体取决于你选择的 Provider。请在使用前查阅其隐私政策；敏感仓库不要开启语义索引。

API Key 只以 Keystore 密文保存在手机，由后台服务解密后调用。我们无法看到它，也无法代你在 Provider 侧撤销，请在你自己的 Provider 账户中管理密钥与额度。

如果你不配置任何 Provider，应用不会发起 AI 请求。

## 诊断信息

应用内没有自建的统计或崩溃上报能力。

由于应用通过 Google Play 分发，Google 会在系统层面收集应用质量数据，也就是 Android vitals：崩溃次数与堆栈、无响应（ANR）事件、启动耗时、耗电与内存占用、权限授予与拒绝的情况，以及发生这些问题时的应用版本、Android 版本、设备型号与国家/地区。这些数据由 Google Play 直接收集，不需要应用内嵌任何代码，也不经过我们；我们只能通过 Play 管理中心看到聚合结果，看不到具体某个用户的记录。

这部分收集由 Google 作为独立的控制者进行，受 Google 自身隐私政策约束。你可以在设备的「设置 → Google → 使用情况和诊断信息」中关闭共享。

应用内的「导出诊断报告」完全由你主动触发，内容见「应用在你的设备上处理的信息」。

## 信息的共享

我们不出售、不出租、不交换你的信息，也不为广告或跨应用追踪而共享。

只有以下四类出口：

1. **你授权或邀请的局域网设备**：在你开启服务时，它们可以通过网络访问你授权给它们的仓库；
2. **你配置的 AI Provider**：在你开启语义索引或 AI 助手时，相关内容会发送到该地址；
3. **系统分享面板的接收方**：在你导出诊断报告或审计记录时，由你选择交给哪个 App；
4. **Google Play 的平台级质量数据**：作为分发渠道的系统能力，见「诊断信息」。

除此之外，我们不与任何第三方共享你的信息。你的仓库、账号、审计日志与凭据不会被上传到我们的服务器——我们没有这样的服务器。

## 信息的安全

应用私有目录受 Android 应用沙箱保护，其他应用无法读取。

服务端密码以 argon2 哈希保存；客户端的密码与 SSH 私钥以 Android Keystore 加密后的密文保存，明文不落盘。

应用提供可选的应用锁（6 位 PIN，设备支持时可配合指纹或人脸）。启用后，进入应用需要先解锁。请理解：应用锁是本地防护，防护强度取决于设备与你的设置；设备被 root、被完整备份或被他人物理接触时，本地数据的可读性会下降。

设备不具备系统认证能力时（例如未设置锁屏的设备），应用会退化为不要求系统认证。这类设备上请不要保存高价值凭据。

建议你：只在可信局域网开启服务；优先使用 HTTPS 并在客户端核对指纹；不要把管理员密码交给不信任的人；定期清空审计日志；为设备设置锁屏。

如果你的设备开启了 Android 系统备份，应用私有目录可能被纳入系统备份，由系统与你登录的云账户处理。我们无法访问该备份，也无法代你删除，请在系统设置与云账户中管理。

## 保留与删除

只要你保留本应用，你的信息就留在你的设备上。我们不保留副本。

卸载应用会删除私有目录中的仓库、账号、审计日志、凭据、设置与 AI 记录。系统备份中的副本需要在系统或云账户中另行删除。

应用内提供逐项删除：删除仓库、删除成员或撤销授权、清空审计日志、清空 AI 对话、删除已保存的凭据、移除 AI 配置。

界面与后台服务所需的运行状态只存在于内存中，退出应用后释放。

## 你的权利

根据你所在地区的法律（例如 GDPR、CCPA/CPRA 或《中华人民共和国个人信息保护法》），你可能拥有下列权利：访问我们持有的与你有关的信息、要求更正不准确的信息、要求删除、限制或反对处理，以及要求以可携带的形式获取这些信息。

由于你的信息只存在于你的设备上、我们没有任何副本，这些权利可以直接行使：

- **访问与更正**：在应用内查看并修改仓库、成员、授权与全部设置；
- **删除**：卸载应用即删除全部本地数据；也可以在应用内逐项删除；
- **撤回同意**：随时在系统设置中撤销任何已授予的权限，撤销后对应功能停止工作，其余功能不受影响；关闭 AI 或删除 AI 配置后，应用不再发起相应请求。

如果你认为我们的处理违反了数据保护法律，你有权向你的居住地、工作地或涉嫌侵权行为发生地的监管机构提出投诉。你也可以先联系我们，我们会尽力直接解决。

## 处理的法律依据

在适用《通用数据保护条例》（GDPR）的情况下，我们依据以下基础处理信息：

- **履行合同**（第 6(1)(b) 条）：提供你请求的 Git 服务、保存你的设置、按你的操作同步仓库、在你授权时向局域网设备提供访问；
- **你的同意**（第 6(1)(a) 条）：可选权限（通知、生物识别、电池优化白名单）、AI 功能、诊断报告导出。你可以随时撤回，撤回不影响此前处理的合法性。

我们不以「合法利益」为依据进行广告、画像或行为分析，因为本应用不做这些事。

## 儿童和个人数据

本应用不面向 13 岁以下儿童，我们也不会有意收集他们的信息。

由于应用不向开发者收集个人信息，家长无需为孩子使用本应用做额外设置。但如果你让孩子用本应用运行服务端并邀请他人访问，相关账号与审计数据由设备所有者管理，请自行评估是否合适。

## 不出售、不共享

按《加州消费者隐私法》及其修正案（CCPA/CPRA）对「出售」与「共享」的定义，我们不出售、也不共享个人信息。本应用没有广告，也没有接入用于广告或画像的分析 SDK；我们不从你的信息中获取任何商业收益。

## 政策变更

本政策如有变更，我们会更新本页内容与上方的最后更新日期。

若变更影响信息的处理方式，我们会在生效之前于应用内或商店页面说明，而不是仅更新日期。

## 与我们联系

关于本政策或你的信息，可通过 Google Play 商品页「开发者联系信息」中公布的开发者邮箱与我们联系。

---

**Summary (English)**: This policy explains how Git Mobile handles your information. Git Mobile is a local Git server and client for Android, published by its independent developer, who does not operate any backend that receives your repositories, accounts or audit records. The app has no cloud account and does not ask for your name, email address, phone number or postal address. Repositories live in the app's private storage (`files/repos`); the local admin and member accounts, argon2-hashed passwords and repository grants live in the app's private database (`files/turso/audit.db`); the audit log records time, user, repository, action, result, the visiting client's IP address and HTTP method, and can be cleared or capped. When used as a client, the app stores server address and username in plain text and stores passwords or SSH private keys only as Android Keystore ciphertext. HTTPS certificates and the SSH host key are generated and kept on the device. When the server is running it listens on all interfaces by default (a loopback-only mode is available), and devices on the same network that pass authentication can read or push to the repositories you grant. The app performs no port forwarding or relay; exposing the service to the internet is your decision. Optional AI features are admin-only and off by default: you supply an OpenAI-compatible endpoint and API key, requests go directly from your phone to that endpoint, semantic indexing sends chunked repository text to your embedding provider, and the assistant sends your conversation and tool results (which may include repository content) to your chat provider; those providers process the content under their own policies. The app contains no advertising, analytics, crash-reporting or tracking SDK. Because it is distributed through Google Play, Google collects Android vitals at platform level as an independent controller; you can turn that off in Settings → Google → Usage & diagnostics. The in-app diagnostic report is generated only when you tap Export, contains configuration facts such as version, private path, service state and certificate fingerprint, never passwords, tokens or repository objects, and leaves the app only through the system share sheet you choose. Data is not sold or shared as defined by the CCPA/CPRA. Legal bases under the GDPR are performance of the service you requested (Article 6(1)(b)) and your consent for optional permissions, AI features and diagnostic export (Article 6(1)(a)), which you can withdraw at any time. Uninstalling the app deletes its local data; system backups, if enabled on your device, are managed by Android and your cloud account, not by us.
