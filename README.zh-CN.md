<div align="center">

<a href="https://v2fun.ai/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg" />
    <img src="assets/logo.svg" width="250" height="100" alt="V2Fun" />
  </picture>
</a>

# V2Fun Split to Print

**已有模型的分色、拆件与打印装配**

沿几何轮廓分色，制作有厚度的零件和配套连接，导出可检查的打印文件。

[English](./README.md) | [简体中文](./README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version: 1.0.0](https://img.shields.io/badge/version-1.0.0-green.svg)](#roadmap)
[![Runtime: Blender 4.x](https://img.shields.io/badge/runtime-Blender%204.x-E87D0D.svg)](https://www.blender.org/)
[![Tooling: Blender Python](https://img.shields.io/badge/tooling-Blender%20Python-3776AB.svg)](scripts)
[![Sponsor: V2Fun](https://img.shields.io/badge/Sponsor-V2Fun-16161A.svg)](https://v2fun.ai/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/2uBMRp275u)

</div>

---
## Live demos

真实工作流结果的离线 3D 示例。Assembled 与 Exploded 之间平滑切换；选择耗材颜色后，其他颜色的零件通过动画隐藏。无需服务器或联网。GitHub 文件页显示源码，下载 HTML 后在浏览器中打开。

| 示例 | 内容 | 打开 |
| --- | --- | --- |
| 150 mm / 5 colors / 13 parts | 装配／展开动画、按颜色隔离、旋转与缩放 | [View](example/index.html) |

[示例说明](example/README.md)

## What it does

输入已有白模与参考图，或已有贴图／顶点色模型。在 Blender 中沿语义和几何整理颜色，按需求拆成实体打印件，修复薄边，制作定位销孔和配套凹位。

- 分别管理色板和实体件数，同色不强制合件，双色也可以一体。
- 完整角色拆件默认处理头部／头颈连接；只上色、导出或局部返修时保留范围。
- 保留文字、Logo 和重要图案，交付实际顶点 RGB 与兼容材质。
- 根据实际尺寸、工艺和装入方向设计厚度与间隙。
- 按需生成离线装配演示，支持颜色隔离动画和基础色显示。

这是代理辅助工作流，不是一键自动分件器，不从零生成模型，不自动完成切片、打印机控制或可制造性认证。

## How it works

1. 检查源模型、参考图、单位与原有问题。
2. 确定色板和实体分件清单，沿真实根部和侧壁整理色界。
3. 先验证最难接口，再制作其余承接面与连接。
4. 检查连通实体、厚度、装配顺序、间隙与多视图。
5. 回读最终文件，确认顶点色、零件数和尺寸，再交付。

[Workflow](SKILL.md) · [Interfaces](references/seams-and-connectors.md) · [Validation](references/validation-and-export.md)

## Quick start

### 安装

将本目录复制到 `~/.codex/skills/v2fun-split-to-print/`；自定义 `CODEX_HOME` 时放在其 `skills/v2fun-split-to-print/` 下，确保 `SKILL.md` 直接位于目录内。需要支持本地技能的客户端及 Blender 4.x 和其内置 Python，无需另装兄弟技能、API 密钥或付费生成服务。

从 `v2fun-part` 迁移：先将旧目录备份到活动技能目录之外，安装新名称，再移除旧活动副本，避免重复发现。模型工程和输出继续保留；必要时刷新客户端技能列表。

### 使用

> 使用 $v2fun-split-to-print 处理这个已有模型。高 150 mm，FDM，0.4 mm 喷嘴，尽量拆成实用的单色打印件，交付原位工程、顶点色 OBJ/MTL 和逐件 STL。

以上尺寸只是示例，不是默认值。附上模型和必要的外观参考，说明尺寸、工艺／喷嘴、已知材料、颜色及不拆的部位；已确认的参数会直接沿用。

### 可选的仅材质导出辅助脚本

在安装目录内，将 `BLENDER` 替换为实际可执行程序：

```sh
BLENDER --background --python scripts/export_obj_bundle.py -- --help
```

该脚本要求已经检查、使用常量材质的 Blender 工程，不负责自动分件、修网格、烘焙顶点色或认证可打印性。详见 [导出范围](references/validation-and-export.md)。

没有 Blender 时先检查输入并说明缺少的运行环境。材质颜色来自联动节点时，应先烘焙或准备颜色，不能绕过脚本拒绝条件。预览不等于实物试配。

### 生成离线演示网页

可以说：“使用 $v2fun-split-to-print 为这些已完成的分件制作离线 demo。” 内置生成器输出一个 HTML，包含装配／展开动画、基础色显示、按耗材颜色淡出隔离，以及旋转缩放；不需要服务器或网络，也不改动打印工程。详见[输入配置、生成命令与检查方法](references/offline-demo.md)。

按上面的说明为当前模型准备分件配置后，在技能安装目录执行：

```sh
BLENDER --background --factory-startup --python-exit-code 1 --python scripts/build_demo.py -- --blend assembled.blend --manifest demo.json --output demo.html
```

生成文件需要 Blender 4.x，浏览器需要 JavaScript 和 WebGL。Three.js 已内置并保留 MIT 许可声明。默认预览中每个实体件使用一种均匀基础色，不显示贴图和顶点色图案。

## What you get

| 交付物 | 内容 |
| --- | --- |
| 原位 Blender 工程 | 可编辑分件与实际连接结构 |
| 顶点色 OBJ + MTL | 实际 RGB 数据、物体名称与材质兼容方案 |
| 按需逐件 STL | 不带颜色的独立打印实体 |
| 按需离线 HTML 演示 | 装配／展开动画、耗材颜色筛选、旋转与缩放 |
| 装配说明与必要检查 | 方向、改动、尺寸及未验证事项 |

未实物试打就不会宣称配合通过。OBJ 顶点色属于扩展；接收软件可能需要 MTL 或手动匹配耗材。

## Roadmap

### v1.0.0

- [x] 从旧名称迁移，保留分色、拆件和局部返修流程。
- [x] 默认角色头部连接与防薄片验收。
- [x] 顶点色交付要求、双语说明和离线结果示例。
- [x] 可复用离线 demo 生成器、可配置分件清单与内置查看器。

## Star history

V2Fun-Research/v2fun-split-to-print 为私有仓库，访问需要授权；保持私有期间不提供公开 Star History 图表数据。

[![Star History Chart](https://api.star-history.com/svg?repos=V2Fun-Research/v2fun-split-to-print&type=Date)](https://www.star-history.com/#V2Fun-Research/v2fun-split-to-print&Date)

## Sponsors

<table>
<tr><td align="center" width="160"><a href="https://v2fun.ai/"><img src="assets/sponsors/v2fun-square.png" width="96" height="96" alt="V2Fun" /></a><br /><strong>V2Fun</strong></td><td>V2Fun 支持将想法发展为三维创作成果。本技能关注已有模型生成之后的环节：梳理设计颜色，按真实形体拆分零件，制作能够配合的承接面与连接结构，并保留可编辑的工程和明确的输出。它使用本地 Blender 工作流，无需为了分件再次生成模型或调用付费服务。模型创建、分色装配和角色动画可以分别选择适合的技能；平台上其他功能并不会自动成为这个技能的能力。最终打印效果仍取决于模型细节、材料、设备与试打结果，数字验收不会替代实物确认。</td></tr>
</table>

维护：**V2Fun Team** · [V2Fun Discord](https://discord.com/invite/2uBMRp275u) · [V2Fun](https://v2fun.ai/)

## Acknowledgments

感谢 [Blender](https://www.blender.org/) 及其贡献者提供本地建模工具。README 展示结构沿用 V2Fun 模板，其版式受到 [img2threejs](https://github.com/img2threejs/img2threejs) 启发；不表示第三方背书。 离线查看器使用 MIT 许可的 [Three.js](https://threejs.org/) 及其 OrbitControls、BufferGeometryUtils 组件。

## License

[MIT License](LICENSE)<br>
Copyright © 2026 V2Fun Team.

适用于本项目代码与文档；Blender、品牌标识、输入模型和示例角色素材分别适用各自的权利范围。示例角色不包含在 MIT 授权中，公开再分发权尚未独立确认。详见 [第三方范围](THIRD_PARTY.md)。
