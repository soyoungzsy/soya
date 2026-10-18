# 维护与恢复 / Maintenance and recovery

本文件为规范迭代候选，尚未提交或发布。源码可公开读取不等于安装、功能和发行物已验收。

## 版本与后续 AI 修改

使用现有版本源，不在提报时静默改变已发布 tag 或替换旧包。兼容修复增 patch，新功能增 minor，破坏性变化说明迁移并采用相应版本。合并前决定实际版本并同步更新 CHANGELOG、tag、Release 与下载引用。现有发行记录以 GitHub Releases 为准；无 Release 时不能凭 README 的版本号宣称已发行。

AI 修改使用独立分支和 PR，写明问题、最终行为、实际检查/未检查项、兼容性、恢复办法。不覆盖用户未提交修改。遵守分支保护，不擅自重写历史。

## 本项目恢复办法

恢复基于已知历史提交；保留恢复前快照。不要运行旧安装器。更新前备份用户 Skill 和输出；模板 CLI --list 已离线运行。

## 故障与隐私

提供当前版本、环境、复现、预期与实际结果及脱敏日志；公开 Issues 不含个人数据、工作材料、凭据。安全问题走已配置的私密渠道；无私密渠道时不要把秘密贴进 Issues，也不虚构支持邮箱或响应承诺。模型与外部服务的费用、处理和留存按各自规则执行。

## 发布后自检

每次真实发布后，从公开入口以首次接触者视角检查中文/英文介绍、目标用户、准备条件、安装/复制入口、成功结果、费用/权限、限制和故障恢复。记录仍有的疑问、修订与复查。未解决核心使用问题不能标为已验收；AI 视角自检不冒充真人反馈。

## English essentials

This is an unsubmitted maintenance candidate, not a release certificate. Use branches and reviewable PRs; record actual checks and limitations. Preserve existing tags/assets. Set the next version at merge and keep release references consistent. Back up source, local configuration and user data before upgrading; reverting code does not undo data migrations or external actions. Report sanitized reproductions through Issues, never work material or credentials. After each real release, review its public entry point as a newcomer in both languages, resolve blocking questions and recheck before acceptance. No independent-user validation is implied.
