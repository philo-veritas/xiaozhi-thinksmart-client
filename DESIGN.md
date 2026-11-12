---
name: 小麦设备界面
description: 常驻家中的语音助手屏幕：底色始终是黑，小麦的颜色和形状就是状态，隔着房间就能读懂。
colors:
  black: "#111110"
  paper: "#f4f3ee"
  yellow: "#ffc800"
  cobalt: "#5a73ff"
  wheat: "#e8983a"
  red: "#f03c14"
  eye-white: "#ffffff"
  raise: "#262523"
  warm-field: "#1a1612"
  warm-ink: "#f3ebe0"
  warm-ink2: "#ab9f90"
  warm-raise: "#2c251e"
  navy-field: "#0e1424"
  navy-ink: "#eef1f8"
  navy-ink2: "#9aa3b8"
  navy-raise: "#1d263c"
  navy-cobalt: "#8593ff"
  paper-raise: "#e3e1d8"
  paper-cobalt: "#2340e8"
  paper-yellow: "#f5b400"
  sleep-speaking: "#c9a000"
  on2-black: "#a9a8a2"
  on2-paper: "#55544f"
  line-on-black: "#ffffff26"
  line-on-paper: "#11111024"
  error-on-paper: "#b3260a"
  error-on-black: "#ff9f88"
typography:
  clock-portrait:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "18.2rem"
    fontWeight: 600
    lineHeight: 0.9
    letterSpacing: "-0.04em"
    fontFeature: "tnum"
  clock-landscape:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "15.5rem"
    fontWeight: 600
    lineHeight: 0.9
    letterSpacing: "-0.04em"
    fontFeature: "tnum"
  title-solo-portrait:
    fontFamily: "Xiaomai Title, Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "8rem"
    fontWeight: 600
    lineHeight: 1.08
  title-solo-landscape:
    fontFamily: "Xiaomai Title, Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "7rem"
    fontWeight: 600
    lineHeight: 1.08
  title-talk-portrait:
    fontFamily: "Xiaomai Title, Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "5.25rem"
    fontWeight: 600
    lineHeight: 1.08
  title-status:
    fontFamily: "Xiaomai Title, Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "4.125rem"
    fontWeight: 600
    lineHeight: 1.08
  title-sheet:
    fontFamily: "Xiaomai Title, Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "3.5rem"
    fontWeight: 600
    lineHeight: 1.1
  reply-solo:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "3rem"
    fontWeight: 500
    lineHeight: 1.38
  reply-portrait:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "2.25rem"
    fontWeight: 500
    lineHeight: 1.46
  reply-landscape:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "2rem"
    fontWeight: 500
    lineHeight: 1.46
  row-time:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "2.125rem"
    fontWeight: 600
    fontFeature: "tnum"
  row-title:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 600
  control-label:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 600
  hint:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 400
    lineHeight: 1.4
  note:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 400
    lineHeight: 1.5
  timestamp:
    fontFamily: "Archivo, Noto Sans CJK SC, Noto Sans SC, PingFang SC, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
rounded:
  none: "0"
  full: "50%"
  track: "0.5rem"
  tag: "0.5rem"
  bubble: "1.75rem 1.75rem 0.5rem 1.75rem"
  hud: "2rem"
  logo-tile: "0.875rem"
  logo-tile-large: "1.125rem"
  action-small: "1.75rem"
  control: "2.75rem"
  action-large: "3.5rem"
spacing:
  inline: "0.5rem"
  control-gap: "1.25rem"
  row: "1.5rem"
  block: "1.75rem"
  margin-landscape: "2.5rem"
  margin-portrait: "3rem"
  column-gap-landscape: "3.5rem"
  danger-gap: "3.5rem"
  top-bar: "6rem"
components:
  mic-button:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.black}"
    rounded: "{rounded.full}"
    size: "6.5rem"
  control-filled:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.black}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    height: "5.5rem"
  control-outline:
    textColor: "{colors.paper}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    height: "5.5rem"
  ring-stop:
    backgroundColor: "{colors.black}"
    textColor: "{colors.red}"
    rounded: "{rounded.action-large}"
    height: "7rem"
  sheet-button:
    textColor: "{colors.black}"
    rounded: "{rounded.none}"
    padding: "0 1.75rem"
    height: "4.5rem"
  sheet-button-armed:
    backgroundColor: "{colors.red}"
    textColor: "{colors.black}"
    rounded: "{rounded.none}"
    padding: "0 1.75rem"
    height: "4.5rem"
  tab-active:
    backgroundColor: "{colors.black}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    height: "4.5rem"
  model-cell:
    textColor: "{colors.black}"
    rounded: "{rounded.none}"
    padding: "1.5rem"
    height: "13rem"
  model-cell-active:
    backgroundColor: "{colors.black}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "1.5rem"
    height: "13rem"
  message-user:
    backgroundColor: "{colors.raise}"
    textColor: "{colors.paper}"
    rounded: "{rounded.bubble}"
    padding: "0.875rem 1.375rem"
  interrupt-tag:
    textColor: "{colors.paper}"
    rounded: "{rounded.tag}"
  toast:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.black}"
    rounded: "{rounded.action-small}"
  volume-hud:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.black}"
    rounded: "{rounded.hud}"
  missed-band:
    backgroundColor: "{colors.red}"
    textColor: "{colors.black}"
    rounded: "{rounded.none}"
---

# Design System: 小麦设备界面

## Overview

**Creative North Star: "黑场里的小麦"**

小麦放在客厅或厨房，人多半在 1 到 2 米外，手可能还占着。屏幕的底色始终是近黑，不随状态更换；状态由小麦自己表达：麦色是待机和连接，纸白是聆听，钴蓝是思考，黄是回答。小麦是屏幕上最大的色块，抬眼就能读到它的颜色和形状，再看一眼才需要读字。只有响铃会把整屏换成朱红，因为它要人马上处理。

**机主决定（2026-11-12）：** 原先每个状态整屏换色，前后配色不连贯，改为底色始终是黑，状态色只落在小麦和声波、圆点、麦克风圆环这几个小部件上；响铃保留整屏朱红。同日又决定：底色做成可切换的主题（黑、暖墨、夜蓝、纸白），由机主在设置里选。

纪律来自瑞士国际主义海报：纯平色块、大号等线数字、左对齐、细线分组、果断切换。对话屏把回答放到最大，设置走近才看，所以设置页是安静的纸白页，一次只显示一组。这一类产品常见的深色渐变加发光球体，以及一堆卡片和胶囊，都被明确拒绝。

唯一有性格的部分是角色。**机主决定**：小麦要和 Grok Bot 头像一样，用 bloub 引擎（`web/v2/bot.js`）绘制：一个形状在状态之间连续变形，两只白眼长在假想球面上，没有嘴，没有明暗。引擎里的数字来自对参考视频的逐帧测量，不是设计取值。

**Key Characteristics:**
- 底色始终是黑；小麦的颜色、轮廓和大字标题一起表达状态，不只靠颜色。
- 竖屏 800×1280 和横屏 1280×800 都是正式形态，各有自己的构图（机主决定）。
- 无阴影、无大面渐变、无描边卡片；分组靠细线、留白和反色实块。
- 除小麦的绘制外，所有动画只用 transform 和 opacity（硬件约束）。

## Colors

主屏只有一种底色：近黑。四种状态色只用于小麦本体和跟随它的小部件，朱红只用于警示，其余颜色都是文字、细线和凸起面。

### Primary：状态色，只用在小麦身上
- **麦色 Wheat** (#e8983a)：待机和连接中的小麦本体；待机页倒计时条的填充色。
- **纸白 Paper** (#f4f3ee)：聆听时的小麦本体（同时也是黑底上的文字色，见 Neutral）。
- **钴蓝 Cobalt** (#5a73ff)：思考时的小麦本体。原来的 #2340e8 在黑底上对比只有约 2.7:1，隔着房间看发闷，所以提亮到 #5a73ff（约 4.6:1）。
- **信号黄 Yellow** (#ffc800)：回答时的小麦本体；也用于待更新一行和闹钟暂停警示的实底。

### Tertiary
- **朱红 Red** (#f03c14)：响铃整屏、错过提醒色带、已确认一次的破坏性按钮、设置入口和标签页上的提醒小圆点。它只表示「有事要处理」，不用作装饰。

### Neutral
- **近黑 Black** (#111110)：主屏在所有状态下的底色，包括睡眠时段；响铃屏上的文字和小麦本体。
- **纸白 Paper** (#f4f3ee)：黑底上的文字和反色控件；设置和模型页的底。
- **凸起面 Raise** (#262523)：黑底上比底色略亮的一层，只用于用户消息气泡，让提问退到回答后面。
- **眼白 Eye White** (#ffffff)：只用于小麦的眼睛。眼睛在任何色块上都是纯白，不跟随纸白。
- **次要文字**：黑底用暖灰 (#a9a8a2)，纸白页用深灰 (#55544f)。
- **细线**：黑底 (#ffffff26)，纸白页 (#11111024)。
- **错误文字**：纸白页用暗红 (#b3260a)，睡眠时段的黑页用浅红 (#ff9f88)。
- **睡眠时段的小麦**：聆听用暖灰 (#a9a8a2)，回答用调暗的黄 (#c9a000)，免得大面积纸白或亮黄照亮房间；其余状态和白天相同。

### 状态配色

| 状态 | 底色 | 文字 | 小麦本体 | 声波、圆点、麦克风圆环 |
| --- | --- | --- | --- | --- |
| 待机 | black | paper | wheat | — |
| 连接中 | black | paper | wheat（彗星形） | — |
| 聆听 | black | paper | paper | paper |
| 思考 | black | paper | cobalt | cobalt |
| 回答 | black | paper | yellow | yellow |
| 响铃 | red（整屏覆盖） | black | black | — |

### 主题

主屏的底色可以在设置里换成四种之一，换了马上生效（瞬切，不做过渡）。主题只换底色、文字、细线、凸起面，以及个别为了对比度要调整的小麦颜色；状态的对应关系、响铃的整屏朱红和纸白的设置页都不变。

| 主题 | 底色 | 文字 | 次要文字 | 凸起面 | 小麦颜色的调整 | 睡眠时段 |
| --- | --- | --- | --- | --- | --- | --- |
| 黑 | #111110 | #f4f3ee | #a9a8a2 | #262523 | — | 照用 |
| 暖墨 | #1a1612 | #f3ebe0 | #ab9f90 | #2c251e | 聆听用 #f3ebe0 | 照用 |
| 夜蓝 | #0e1424 | #eef1f8 | #9aa3b8 | #1d263c | 聆听用 #eef1f8，思考提亮到 #8593ff 以免融进底色 | 照用 |
| 纸白 | #f4f3ee | #111110 | #55544f | #e3e1d8 | 聆听用黑，思考用 #2340e8，回答用 #f5b400 | 自动换成黑主题 |

- 暖墨适合暖色灯光的客厅和厨房，与小麦的麦色同一色系；夜蓝更冷更利落；纸白适合白天光线亮的房间。
- 默认是黑；新装或没选过时也用黑。选择保存在客户端，和自动熄屏、睡眠时段一样重启后保留。
- 纸白在亮底上的黄对比偏弱（约 1.7:1），回答时靠小麦的形状和「正在回答」大字补足，隔着房间的辨识度不如深色主题。

### Named Rules
**The One Field Rule.** 主屏底色在同一主题里始终不变，状态切换时不换底色；状态由小麦的颜色和形状、大字标题以及跟随小麦颜色的小部件表达。唯一的例外是响铃整屏朱红。新增界面不得给某个页面或状态单独起一种底色。

**The One Accent Rule.** 同一时刻屏幕上只有一种状态色，就是当前小麦的颜色（`--me`）。声波条、思考圆点和麦克风圆环取这个颜色，文字、按钮和消息不取。

**The Relative Ink Rule.** 组件不写死颜色，只取当前底色的「底」和「字」两个角色；反色按钮就是把这两个角色对调。这样同一个按钮在黑底主屏、纸白设置页和朱红响铃屏上都成立。

**The Dark Sleep Rule.** 睡眠时段屏幕保持全黑，不照亮房间，设置页也转成黑底；只有小麦本体可以带颜色。

## Typography

**Display Font:** Xiaomai Title（中文标题），回退 Archivo 和 Noto
**Body Font:** Archivo（数字和拉丁文）+ Noto Sans CJK SC（其余中文）

**Character:** **机主决定**：数字和拉丁文用 Archivo，中文标题用 Xiaomai Title，其余中文用 Noto。Archivo 的大号等线数字是海报的主角；Xiaomai Title 自带约 8° 的倾斜，只在标题出现，给严肃的版式留一点人味。

**字体命名（机主决定）：** Xiaomai Title 是从得意黑（Smiley Sans）裁出的子集。该字体的 OFL 许可保留了字体名，所以随仓库分发的子集改名为 Xiaomai Title，绝不能以 Smiley 或得意黑命名；来源和许可写在 `web/v2/fonts/OFL-xiaomai-title.txt`。

### Hierarchy
- **Clock**（600，竖屏 18.2rem，横屏 15.5rem，行高 0.9，字距 -0.04em，等宽数字）：待机和响铃的巨型时钟，贴左边缘。闹钟很多或有错过提醒时，横屏可缩到 12rem 和 9rem，竖屏可缩到 15rem。
- **Title**（Xiaomai Title，行高 1.08）：状态大字。待机和横屏对话 4.125rem，竖屏对话 5.25rem；还没有消息、小麦独占屏幕时，竖屏 8rem，横屏 7rem。设置和模型页标题 3.5rem，关机屏 6rem。
- **Reply**（500）：模型的回答。横屏 2rem，竖屏 2.25rem，行高 1.46；只有一条消息时放大到 3rem，行高 1.38，隔着房间也能读。
- **Row**（闹钟行标签 500，1.75rem；行内时间 600，2.125rem；设置项标题 600，1.75rem）：待机信息行和设置行。
- **Control**（600，1.625rem）：主屏的胶囊控件。响铃按钮放大到 700，2.25rem。
- **Hint**（400，1.375rem，行高 1.4）：标题下的一句提示，用次要文字色。
- **Note**（400，1.1875rem，行高 1.5）：设置页的说明，只在走近时读。
- **Timestamp**（400，1rem）：消息时间，系统里最小的字号。

### Named Rules
**The Tabular Time Rule.** 时间和时长都用等宽数字。「标签 + 时间」的行里时间靠右，并排的时间才对得上；巨型时钟是主角，贴左。

**The Title Only Rule.** Xiaomai Title 只用于标题，关闭字重合成，不用于正文、按钮或数字。子集只含页面标题用字和常见模型名，新增标题文案要重新裁切子集；字库外的字回退到 Noto。

## Layout

根字号在两种屏幕下都是 16px，所有尺寸用 rem，整页按比例一起缩放。方向只由系统视口决定，切换时内容不变。

- **横屏 1280×800：** 两栏。左栏 27rem 放小麦、状态和控件，右栏放时钟或对话，栏距 3.5rem，外边距 2.5rem。还没有消息时，小麦放大到 34rem，单独占满页面。
- **竖屏 800×1280：** 一栏从上读到下，外边距 3rem。待机依次是巨型时钟、日期、小麦与唤醒词并排、倒计时和闹钟行、错过提醒。对话时上方是小麦和大字状态，中间是回答，底部是控件。还没有消息时，小麦放大到 32rem。
- **顶栏：** 高 6rem，左边模型入口，右边依次是倒计时、时钟和设置。待机页已有巨型时钟，顶栏不再重复时间和倒计时。
- **贴边：** 横屏分页标签、错过提醒色带、待更新一行和模型格都穿过外边距直达屏幕边缘，这是海报式的满版，不是留白失误。
- **节奏：** 常用间距是 0.5、1、1.25、1.5、1.75、2.5rem。破坏性操作上方留出更大的 3.5rem。
- **密度：** 一屏只讲一件事。设置分三组，一次只显示一组；模型页横屏 4 列，竖屏 2 列。

## Elevation & Depth

系统没有投影，也没有模糊或发光。层次来自整层覆盖：设置页、响铃屏和关机屏都是完全不透明的整屏；用户消息气泡用比底色略亮的凸起面 (#262523) 退后一层；提示条和音量浮层是反色实块，靠颜色对比从底上分出来。唯一的立体感属于小麦的眼睛。

### Named Rules
**The Eyes Only Depth Rule.** （机主决定）3D 感只来自眼睛：眼睛按球面切线投影，靠边的一只约窄到 0.69 倍，转到背面时被身体遮住。身体永远是平的，不加明暗、高光或阴影。

**The Transform Only Rule.** （硬件约束：WebKitGTK，Adreno 506）只动画 transform 和 opacity。颜色、尺寸和布局一律瞬切。唯一的例外是小麦的绘制：引擎每帧重写 SVG 路径，所以限制在 `botFps`（15 帧），只在属性变化时写入。声音电平只驱动整层缩放，不重绘。

**The Character Carries The Change Rule.** 状态切换时底色不动，只有小麦变化：引擎用一次眨眼遮住变形，本体颜色瞬切（颜色不做过渡）。不再有整屏色层滑动（原 `.wipe` 撤掉）。时钟页和对话页互换时，新页面从下方 2.5rem 处上浮淡入（360ms），这是主屏唯一的整页动画。消息自己没有入场动画。

**The Settle First Rule.** （实测约束）动画等画面跟上变化后才开始，判断标准是变化后出现第一个快帧，最多等 0.5 秒。如果一变化就开始，计时会在设备绘制变化的 100–200ms 里照走，第一帧出来时已经过半。页面还在等待时又来一次变化，就重新等。唤醒时连接中和聆听只隔 40–50ms，因此页面只上浮一次。整页和主区常驻各自的合成层。屏幕外的历史消息用 `content-visibility` 跳过排版和绘制。

## Shapes

形状分三种语言，各有用途：

- **有机圆润：** 只属于小麦。身体由引擎生成：待机是正圆，其余状态见下面的对应表。
- **胶囊和正圆：** 隔着房间就要按的主屏控件，圆角等于高度的一半。麦克风是正圆。
- **圆角块：** 主屏上浮在黑底上的块，与胶囊控件同属一家。用户消息气泡圆角 1.75rem，右下角收成 0.5rem 指向说话的一侧；提示条 1.75rem；音量浮层 2rem；打断标记 0.5rem。圆角块不能按，所以不用胶囊（胶囊只给控件）。
- **直角：** 走近才用的纸白设置页：设置页按钮、分页标签、模型格、分段选项，以及贴边的错过提醒色带，圆角为 0。

厂商图标放在圆角小方块上（0.875rem，模型格里 1.125rem），用来容纳第三方标志。滑块轨道、声波条这类小部件的两端也是全圆，不构成新的形状语言。

## Components

### 小麦
隔着房间读状态的角色，也是系统的签名。
- **构成：** 引擎给出身体路径和两只眼睛；`BotView`（`app.js`）把身体填成 `--me`，眼睛填成 `--eye`，并用身体路径裁切眼睛。不要改动 `bot.js` 里的测量常量。
- **看向：** 由引擎决定：待机时目光缓慢漂移并眨眼，换状态时用一次眨眼遮住变形。
- **状态对应：** 待机 `idle`，有待汇报 `notify`，麦克风关闭 `sleep`，连接中 `comet`，聆听 `wide`，思考 `thinking`，回答 `play`，响铃 `exclaim`。聆听时整层随声音放大，回答时整层随声音压扁，都不重绘。
- **尺寸：** 待机横屏 19rem、竖屏 17rem；对话横屏 14rem、竖屏 10.5rem。

### Buttons
- **麦克风：** 6.5rem 正圆，反色实底。聆听时外圈加一道随声音放大的圆环，圆环取小麦的颜色；关闭时变成次要文字色描边并加斜杠。
- **主屏胶囊：** 高 5.5rem，等分剩余宽度，一只反色实底（打断），一只描边（结束）。只显示当前能按的控件。
- **响铃按钮：** 高 7rem（横屏 6.5rem）。停止是黑底朱红字，宽度是再睡的 1.4 倍；再睡是黑色粗描边。
- **设置页按钮：** 直角描边，高 4.5rem，字号 1.5rem。
- **破坏性按钮：** 默认只有描边，上方留出更大空白；按第一下变成朱红实底并改字（如「确认关机」），几秒内再按才执行，否则自动恢复。
- **按下反馈：** 全部是缩小（0.93 到 0.98，约 120ms）。这是无悬停的触屏，不设 hover 态。

### 待机信息行
- **闹钟和倒计时：** 顶部一道细线，左边是标签，右边是等宽时间。
- **倒计时条：** 高 0.4rem，长度表示剩余时间，用 scaleX 缩短。
- **错过提醒色带：** 朱红实底贴到屏幕边缘，黑字，右上角一只黑底朱红字的「知道了」胶囊。

### 对话
- **用户消息：** 靠右的凸起面气泡（#262523 底、纸白字，时间用次要文字色），圆角 1.75rem、右下角 0.5rem，宽度不超过 84%。提问比回答暗一层，回答才是主角。
- **模型回答：** 没有容器，文字直接落在黑底上。
- **等待中：** 用户说话时是一排随声音起伏的声波条；模型思考时是三个跳动的圆点。两者都取小麦的颜色。
- **打断标记：** 一个 0.5rem 圆角的细描边小标签，跟在被打断的回答后面。

### Cards / Containers
- **模型格：** 整格铺满，只用细线分隔，没有外框和圆角。图标在上，名称在下。
- **当前模型：** 整格反色，并标「使用中」。按下时透明度降到 0.7。

### Navigation
- **模型入口：** 图标、模型名、模型 ID 和向下箭头，整块可按，高 4.5rem。
- **设置和模型页：** 从底部滑入（320ms），有大字标题和右上角关闭按钮。
- **分页标签：** 三组。横屏是左侧 15rem 竖排并贴左边缘，竖屏是顶部横排等分。未选为次要文字色，选中为反色实块。

### Inputs / Fields
- **开关：** 全圆轨道加圆钮。关时轨道是细线色，开时轨道反色，圆钮平移（180ms）。
- **滑块：** 高 1rem 的平直轨道，3rem 圆钮，两端配小图标和大图标，整行高 4rem 方便手指。
- **分段选项：** 用细线连成一排的直角格子，选中项反色。
- **主题：** 在「屏幕和声音」里，排在屏幕亮度之后。标题行右侧显示当前主题名；下面是一排四格的分段选项（同「自动熄屏」的分钟选项），每格是一块 4rem 的圆角色样（底色上放一个麦色圆点，代表小麦）和主题名，选中格反色。下方一句说明：纸白只在白天用，睡眠时段自动换成黑底。
- **时间步进：** 两只直角描边的方形按钮夹住大号等宽时间。开关关闭时，这一组透明度降到 0.35。

### 提示和浮层
- **提示条：** 反色实块，圆角 1.75rem。主屏在顶部，设置页在底部，错误时用朱红实底。
- **音量浮层：** 居中的反色实块，圆角 2rem，含图标、平直进度条和等宽数字。
- **响铃屏：** 覆盖一切，包括设置页。朱红整屏，巨型时钟左对齐，小麦变成黑色感叹号；横屏时小麦退到右上方，给时钟让位。

## Do's and Don'ts

### Do:
- **Do** 让小麦的颜色、轮廓和大字标题同时表达状态，不只靠颜色区分；底色保持近黑。
- **Do** 在 800×1280 和 1280×800 两种形态下分别设计和验收每个界面。
- **Do** 通过当前底色的「底」和「字」两个角色给组件上色，让它在黑底主屏、纸白设置页和朱红响铃屏上都成立。
- **Do** 把时间和时长设成等宽数字，并让行内时间靠右。
- **Do** 让所有可按目标至少 3.5rem（56px）高。
- **Do** 用细线、留白和反色实块分组；描边按钮和细线分隔本来就是这个世界的材料。
- **Do** 把破坏性操作默认做成描边，并放在更大的空白之后，确认一次才变朱红。
- **Do** 在同一屏只显示当前能按的控件。

### Don't:
- **Don't** 给小麦加嘴、高光、明暗或阴影，也不要为了“好看”调整引擎的测量常量；Grok 的图标只在模型列表里代表它自己。
- **Don't** 在眼睛滑动之外再做任何 3D 效果。
- **Don't** 在小麦的绘制之外动画 transform 和 opacity 以外的属性，也不要用 backdrop-filter。
- **Don't** 用阴影、模糊，或任何看得出过渡的渐变。厂商标志保留原样；滑块已填充部分那种单色填充也不算渐变。
- **Don't** 用描边卡片包内容，也不要把胶囊用作标签或状态显示；胶囊只给能按的控件。
- **Don't** 把随仓库分发的标题子集命名为 Smiley 或得意黑。
- **Don't** 用等宽字体排任何界面文字；模型 ID 也用 Archivo（机主决定）。
- **Don't** 让声音电平驱动大面积部件。
- **Don't** 为某个状态整屏换色，或在同一屏放两种状态色（响铃除外）。
- **Don't** 在主屏用直角块；直角只留给纸白设置页和贴边色带。
