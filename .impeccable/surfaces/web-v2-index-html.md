---
version: 1
slug: "web-v2-index-html"
primary_target: "web/v2/index.html"
related_targets: ["web/v2/app.css","web/v2/app.js"]
---

# 小麦设备界面（web/v2）

Scope: 设备上的全部界面，模式 Operate。用户在 1–2 米外靠语音使用，偶尔走近点屏幕。竖屏 800×1280 和横屏 1280×800 都是正式形态。接口、事件和功能不变。

## Direction contract

THESIS: 底色始终是黑，小麦的颜色和形状就是状态，隔着房间就能读出它在听、在想还是在说（机主 2026-11-12 决定：不再整屏换色，响铃除外）。拒绝这一类产品常见的深色渐变加发光球体，也拒绝一堆卡片和胶囊。

OWN-WORLD: 瑞士国际主义海报的纪律：无渐变、无阴影、无描边卡片；黑 #111110、纸白 #F4F3EE、黄 #FFC800、钴蓝 #5A73FF（黑底上提亮）、朱红 #F03C14、麦色 #E8983A。角色是纯平圆润色块加两道斜白眼，无嘴，同一时刻只有它带状态色。主屏浮块（消息气泡、提示条、浮层）用圆角，与胶囊控件同族。大号等线数字，左对齐，所有时间右对齐等宽。

STORY: 家人抬眼就知道设备状态和下一件要响的事；开口就能用；要改设置时走近，在纸白页上一次看清一组。

FIRST VIEWPORT: 竖屏待机：黑底，顶部模型入口和设置，巨大时钟左对齐占满宽度，下方小麦与唤醒词并排，再下是倒计时和闹钟行。对话时：上方小麦和大字状态，中间是回答，底部是控件。横屏：左栏小麦、状态和控件，右栏时钟或对话。签名动作：状态切换时底色不动，小麦眨一下眼换形换色；眼睛在平面色块上滑动，像在转头。

FORM: 自有候选第 4 位，瑞士海报式的色场。seed:f9df036115bfeb55。
Raises: 破坏性操作四周留白、默认只有描边（来自开发者控制台）；时间和时长一律右对齐等宽（来自磁带内封）；倒计时条长度表示剩余时间（来自舞谱）；模型页整格排列、当前项反色（来自同人展目录）；切换果断、不做渐变（来自纯黑白）。

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Constraints

只动画 transform 和 opacity；不用 backdrop-filter、大模糊阴影或渐变；高频声音驱动的部件保持很小。形象轮廓自绘，不照描 Grok 的图形。

## Unresolved decisions

无。
