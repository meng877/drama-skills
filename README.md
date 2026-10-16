# AI 微电影创作技能

面向编剧、导演和独立创作者的 AI 微电影工作流：从一个想法或改编材料，到完整单篇剧本、视觉资产、分镜、图片/视频提示词和剪辑成片。

本仓库是 [ZenStory AI Drama Skills](https://github.com/zenstory-ai/drama-skills) 的微电影方向分支，保留原项目 MIT 许可与工具链。十一项技能仍使用 `short-drama*` 名称以兼容既有安装；默认创作目标改为完整单片。[English](README_EN.md)

## 创作原则

- 以人物欲望、行动、关键选择和结尾变化组织完整故事。
- 用画面、空间、表演、声音与潜台词传递情绪，允许铺陈、沉默和余韵。
- 不默认五秒钩子、反转配额、爽点密度、峰值收尾或下集悬念。快节奏和强情节仍可自由选择。
- 分镜同时考虑电影叙事与 AI 可生成性，明确角色、空间、视线、持物和动作连续性。
- 默认单部、横屏 16:9；片长按项目决定，用户明确要求优先。已存在项目不自动修改。

## 安装

```bash
npx skills add meng877/drama-skills -y -g
```

开发分支尚未合并时，从本仓库对应 PR 下载或克隆该分支使用；上述命令安装默认分支。
脚本需要 **Python 3.9 或更新版本**，剪辑另需 `ffmpeg` / `ffprobe`。Claude Code 使用 `/short-drama`，Codex 使用 `$short-drama`。
每个技能可独立安装，缺少其他技能不妨碍完成已有输入支持的阶段。

## 快速开始

```text
用 $short-drama 初始化《最后一班渡船》AI 微电影，横屏 16:9，目标6分钟，一部完整短片。
用 $short-drama-develop 开发这个故事：渡工想提前收船，听障女孩坚持等父亲，结局渡工留下陪她等待。允许安静留白，不分集。
用 $short-drama-write 按创作简报写完整微电影，保留动作、环境声和沉默，不追加下集悬念。
用 $short-drama-assets 提取全片角色、场景、道具与连续性锁。
用 $short-drama-image-prompts 为已接受资产编写参考图提示词。
用 $short-drama-storyboard 做全片分镜，交接空间、视线、持物和动作，给复杂镜头提供可生成方案。
用 $short-drama-video-prompts 按分镜和我指定的目标模型写逐镜提示词；参考图由我手工挂载时列 PLAN 槽位。
用 $short-drama-produce 预览本批任务、参考、参数与费用信息，确认后再执行。
用 $short-drama-edit 把已有素材剪成完整短片，保留情绪停顿和结尾余韵。
用 $short-drama-review 审查全片因果、结尾、连续性与成片可用性。
```

已有剧本可以直接拆资产或分镜；只要文本时止步于文本。所有外部媒体生产继续遵循预览、明确确认、执行。

## 十一个技能

| 技能 | 微电影职责 |
| --- | --- |
| `short-drama` | 项目初始化、路由、视觉方向与 Dashboard |
| `short-drama-novel-analyze` | 从长材料选取可独立成立的单片改编切口 |
| `short-drama-develop` | 主题、人物、全片结构、结尾与制作边界 |
| `short-drama-write` | 完整剧本、视觉叙事、对白与声音 |
| `short-drama-assets` | 角色身份、造型、空间与道具状态 |
| `short-drama-image-prompts` | 风格帧与可复用资产参考图提示词 |
| `short-drama-storyboard` | 视点、调度、连续性与可生成镜头 |
| `short-drama-video-prompts` | 单镜运动、表演、摄影与声音提示词 |
| `short-drama-produce` | 确认后的素材生产与中断恢复 |
| `short-drama-edit` | 全片组接、入出点、字幕、声音与成片 |
| `short-drama-review` | 带证据的叙事、连续性与交付审查 |

## 文件与兼容

`剧集/EP001/` 是整部微电影的兼容容器，不代表要拆成短剧。场次使用 `EP001-SC001`，镜头使用 `SHOT-EP001-001`。

```text
项目/
├── short-drama.json
├── 项目开发/creative-brief.md
├── 剧集/EP001/
│   ├── 剧本.md
│   ├── 视觉设定.md
│   ├── 分镜.md
│   ├── 图片提示词.md
│   ├── 视频提示词.md
│   ├── 剪辑单.md
│   └── 制作成果/
└── 审查/EP001-审查.md
```

按任务创建所需文件，不预建空文档。单片开发不要求故事引擎、分集地图或节奏档案。
配置中的 `episode_count=1` 表示一部，`target_seconds_per_episode` 记录整片目标秒数；保留字段名以兼容校验、导出和 Dashboard。
旧连续剧项目仍遵循已接受配置，新连续剧可显式传 `--aspect-ratio 9:16 --episode-count 12`。

`$short-drama dashboard` 打开本地创作台。界面仍有“全剧”“集”标签，单片进入 EP001 即可；没有新增浏览器生产按钮。
导出沿用 `project_tool.py export <project> --out <项目外目录>`，只要文字加 `--no-media`。

## 示例与验证

- [微电影合成示例](examples/microfilm/README.md)：开发简报与完整小场景剧本；不宣称已生成媒体。
- [微电影工作流](docs/ai-microfilm-workflow.md)：阶段交接、AI 制作风险与迁移说明。
- [行为评估场景](evaluations/microfilm-scenarios.md)：单片、连续剧与复杂镜头的验收任务。
- 旧的 `examples/creator-first/` 等样例保留为上游历史示例和回归夹具，非本分支默认风格。
- [贡献约定](CONTRIBUTING.md)、[更新日志](CHANGELOG.md)、[MIT 许可](LICENSE)。

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
```

本地校验只验证文件与工具行为，不能保证模型生成的角色、口型、表演和混音质量。实际生成后需逐镜检查。
