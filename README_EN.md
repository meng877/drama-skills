# AI Microfilm Skills

An AI short-film workflow for writers, directors and independent creators: develop a complete story, write a screenplay, design assets and shots, prepare image/video prompts, produce media and edit the film.

This is a microfilm-focused fork of [ZenStory AI Drama Skills](https://github.com/zenstory-ai/drama-skills), retaining its MIT license and eleven `short-drama*` skill names for compatibility. [中文](README.md)

## Install

```bash
npx skills add meng877/drama-skills -y -g
```

This installs the default branch. Until the feature PR is merged, check out its branch to use these changes. Scripts require **Python 3.9 or newer**; editing also requires `ffmpeg` / `ffprobe`.
Claude Code uses `/short-drama`; Codex uses `$short-drama`. Each skill is independently installable.

## Workflow

1. Initialize one complete film, defaulting to landscape 16:9. Choose the total duration for the project.
2. Develop theme, protagonist, causal action, decisive choice and ending in `项目开发/creative-brief.md`. A series engine, episode map and numerical rhythm profile are optional and are not required for a standalone film.
3. Write the full screenplay. Visual storytelling, subtext, silence, observation and an emotional aftermath are valid choices. Fast pacing is also welcome; no hook deadline or reversal quota is imposed.
4. Define identities, costumes, locations, props and continuity locks. Prepare reusable reference images and representative style frames.
5. Design motivated shots with screen direction, eyelines, action and start/end-state continuity. Split difficult generated actions while preserving their dramatic purpose.
6. Translate accepted shots into model-specific prompts without inventing model capabilities. Distinguish planned references from inspected media.
7. Preview exact production tasks and parameters, obtain explicit confirmation, then generate. Interrupted tasks are recovered before resubmission.
8. Edit readable, existing media into a complete film. Preserve meaningful pauses and sound continuity. Advanced transitions/mixing beyond the renderer require real external processing.
9. Review causal clarity, character choices, ending, continuity and actual media quality with evidence. Text checks cannot certify unseen media.

## Compatible storage

`剧集/EP001/` holds the entire film. `EP001-SC001` identifies a scene and `SHOT-EP001-001` a shot. These identifiers do not require serialized storytelling.
The existing documents remain `剧本.md`, `视觉设定.md`, `分镜.md`, `图片提示词.md`, `视频提示词.md`, and, after production, `剪辑单.md`.
Create only the documents needed for the request. `format.episode_count=1` means one film; `target_seconds_per_episode` stores the total target seconds.
Existing projects retain their accepted settings. Explicit series requests use the original serialized workflow, including user-selected portrait formats and episode counts.

Use `$short-drama dashboard` for the local workspace; legacy episode labels remain. Export with `project_tool.py export <project> --out <outside-project-directory>`, adding `--no-media` for text only.

## Skills

`short-drama` routes the workflow. Its ten companion skills are `short-drama-novel-analyze`, `short-drama-develop`, `short-drama-write`, `short-drama-assets`, `short-drama-image-prompts`, `short-drama-storyboard`, `short-drama-video-prompts`, `short-drama-produce`, `short-drama-edit`, and `short-drama-review`.

See the [synthetic film example](examples/microfilm/README.md), [workflow](docs/ai-microfilm-workflow.md), and [evaluation scenarios](evaluations/microfilm-scenarios.md). Historical upstream examples remain regression fixtures, not the default artistic style.

## Validation and attribution

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
```

See [CONTRIBUTING](CONTRIBUTING.md), [CHANGELOG](CHANGELOG.md) and the original [MIT license](LICENSE). Media generation quality requires inspection of the actual outputs.
