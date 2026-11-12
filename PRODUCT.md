# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

机主和家人。设备放在客厅或厨房，大多数时候人在 1–2 米外，手可能占着，环境光偏亮。主要动作是开口说话，再抬眼看一下状态或答案；走近点屏幕只发生在换模型、调设置、停闹钟这类少数时刻。

## Product Purpose

小麦是一台常驻家中的语音助手屏幕：用唤醒词「小麦小麦」开始对话，把语音交给 Hub 上由机主选择的模型回答，同时显示时间、倒计时、闹钟和提醒。成功的标准是：隔着房间能一眼看懂它现在的状态和接下来要响的事，不需要读说明。

## Positioning

自己部署的家用语音终端：一块屏幕可以在多家模型和 Claude Code、Grok Bot 这类智能体之间切换，每个模型各自保留对话；数据和更新都由机主掌握。

## Operating Context

- 联想 ThinkSmart View（CD-18781Y），面板 800×1280。设备有竖屏（800×1280）和横屏（1280×800）两种状态，两者都是正式形态，每个界面都要分别设计和验收；方向由系统视口决定，切换时对话内容不能丢。
- 触屏全屏 kiosk，无键盘、无鼠标、无悬停；音量键和语音也能调节音量、亮度等。
- 自动熄屏和睡眠时段调暗由设置控制，亮度由机主决定。

## Capabilities and Constraints

- 状态：待机、连接中、聆听、思考、回答；另有麦克风关闭、未连接、后台汇报待收听。
- 功能：唤醒词、点按说话、按住说话、打断、结束对话、文字快捷提问、切换模型、聊天记录、倒计时、闹钟、提醒、错过提醒、响铃界面、铃声选择、亮度、设备音量、闹钟音量、自动熄屏、睡眠时段、软件更新、清除记录和记忆、查看 IP、关机。
- 界面只由 `web/v2/`（HTML、CSS、原生 JS）组成，由客户端本地提供，事件和接口见 README；界面改版不改变这些接口。
- 运行环境是 Weston 上的 WebKitGTK，GPU 为 Adreno 506：除小麦的绘制外（限帧重写 SVG 路径，2026-11-08 实机测试 15 帧没有 GPU 错误）只用 `transform` 和 `opacity` 做动画，不用 `backdrop-filter`，会被声音电平高频驱动的部件要保持很小。此前出现过 GPU 残影故障（排查页见 `web/test/v2b.html`），大面积模糊阴影和大范围渐变都要谨慎。
- 只能依赖设备上已有的字体（Noto Sans CJK SC、Noto Sans Mono）或随仓库分发的字体（`web/v2/fonts/`），不能联网加载资源。机主选定：标题用得意黑（裁成子集），数字和英文用 Archivo，其余中文用 Noto。

## Brand Commitments

- 名字是「小麦」，唤醒词是「小麦小麦」。
- 机主明确要求：形象要和 Grok Bot 头像一样（机主看过 bloub 的演示后确认「就是这个样子」）。用 `web/v2/bot.js`，它打包自 [bloub](https://github.com/jeremy-prt/bloub)（MIT，代码许可不覆盖其模仿的设计，与 xAI 无关）。测量常量不要改动。是否进入公开仓库和 Release 尚未决定。Grok 的图标只用于模型列表里代表它自己。
- 各模型厂商图标保留在 `web/logos/`，用于标识对应模型。

## Evidence on Hand

- 界面演示模式：`/?demo=<idle|settings|ring|connecting|listening|thinking|speaking|chat|cut|models|volume|ptt>`，追加 `&still` 关闭动画，追加 `&theme=<black|warm|navy|paper>` 预览主题，可在没有设备时截图。
- 改版前的状态图：`web/test/orb-face-states.png`。

## Product Principles

- 隔着房间先看得懂：状态和时间不靠小字传达。
- 语音是主入口，屏幕上的控件只在需要时出现。
- 一屏只讲一件事：待机就是待机，对话就是对话。
- 所有现有功能都要保留，并且能走到。
- 不能以流畅度换视觉效果；这块 GPU 的稳定优先。

## Accessibility & Inclusion

远距离可读，大触控目标（至少 56px），状态不只靠颜色区分。
