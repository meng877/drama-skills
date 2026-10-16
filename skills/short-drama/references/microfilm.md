# 微电影项目路由

- **craft_default · FILM-01**：新项目单部、横屏 16:9，时长不预设；用户明确的画幅、片数和时长覆盖默认。
- **structural_invariant · FILM-02**：沿用 short-drama.json、剧集/EP001 和五文档协议，整片仅一个容器；场次不能伪装成集。单片总时长写入 format.target_seconds_per_episode，episode_count=1。
- **craft_default**：故事简报 → 全片剧本 → 视觉设定 → 参考图/分镜 → 视频提示词 → 生产 → 剪辑。按用户需要进入任一阶段，不补齐空文件。
- **taste_option**：真人感、动画、水墨属于视觉形态，不决定叙事节奏。微电影不自动提出或接受短剧 rhythm_profile；需要自定数值时才走原有决策流程，不写不受支持的新字段。

初始化：`python3 {技能目录}/scripts/project_tool.py init ./my-film --title "渡口" --aspect-ratio 16:9 --episode-count 1 --target-seconds 360`。
只有用户已选 6 分钟时才使用 360；未知时省略 --target-seconds。旧项目继续沿用自身配置。
Dashboard 的“全剧”“集”及 EP001 是兼容界面用语；单部作品选择 EP001 即进入全片。导出命令和生产确认流程不变。
