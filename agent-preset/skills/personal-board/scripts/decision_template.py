#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
个人董事会 - 决策分析模板生成器
使用方法：python scripts/decision_template.py "你的问题描述"
"""

import sys
import json
from datetime import datetime

# 10 位董事会成员
BOARD_MEMBERS = {
    "曾国藩": {
        "role": "首席心性官",
        "expertise": ["心态调整", "自我管理", "逆境应对"],
        "quote": "天下事，在局外呐喊议论总是无益，必须躬身入局"
    },
    "查理·芒格": {
        "role": "首席理性官",
        "expertise": ["重大决策", "投资判断", "风险评估"],
        "quote": "反过来想，总是反过来想"
    },
    "埃隆·马斯克": {
        "role": "首席创新官",
        "expertise": ["创新突破", "目标设定", "高效执行"],
        "quote": "如果一件事足够重要，即使胜算不高也要做"
    },
    "凯文·凯利": {
        "role": "首席趋势官",
        "expertise": ["趋势判断", "职业规划", "长期主义"],
        "quote": "未来已来，只是分布不均"
    },
    "苏轼": {
        "role": "首席生活官",
        "expertise": ["情绪管理", "生活平衡", "逆境心态"],
        "quote": "莫听穿林打叶声，何妨吟啸且徐行"
    },
    "达·芬奇": {
        "role": "首席好奇心官",
        "expertise": ["创意激发", "跨界学习", "观察力提升"],
        "quote": "简单是终极的复杂"
    },
    "杨绛": {
        "role": "首席助理兼精神导师",
        "expertise": ["内心平静", "文档整理", "精神成长"],
        "quote": "我们曾如此期盼外界的认可，到最后才知道：世界是自己的"
    },
    "波伏娃": {
        "role": "首席自由官",
        "expertise": ["女性成长", "独立决策", "自我实现"],
        "quote": "一个人不是生下来就是女人，她是变成女人的"
    },
    "张小龙": {
        "role": "首席产品官",
        "expertise": ["产品设计", "用户洞察", "职业选择"],
        "quote": "好的产品是自然的，像水一样"
    },
    "俞军": {
        "role": "首席策略官",
        "expertise": ["策略制定", "数据分析", "业务增长"],
        "quote": "产品是解决用户问题的工具"
    }
}

# 问题类型推荐成员
PROBLEM_TYPE_MEMBERS = {
    "职业选择": ["芒格", "马斯克", "张小龙", "俞军"],
    "情绪困扰": ["曾国藩", "苏轼", "杨绛"],
    "创新突破": ["马斯克", "达·芬奇", "凯文·凯利"],
    "女性成长": ["波伏娃", "杨绛", "曾国藩"],
    "产品决策": ["张小龙", "俞军", "马斯克", "达·芬奇"],
    "重大决策": ["芒格", "曾国藩", "马斯克"],
    "默认": ["曾国藩", "芒格", "马斯克", "杨绛"]
}


def generate_template(problem, problem_type="默认"):
    """生成决策分析模板"""
    
    # 获取推荐的董事会成员
    members = PROBLEM_TYPE_MEMBERS.get(problem_type, PROBLEM_TYPE_MEMBERS["默认"])
    
    # 生成模板
    template = f"""# 个人董事会决策分析

**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 问题描述

{problem}

## 推荐的董事会成员

根据问题类型「{problem_type}」，推荐请教以下成员：

"""
    
    for member in members:
        info = BOARD_MEMBERS[member]
        template += f"- **{member}**（{info['role']}）：擅长 {', '.join(info['expertise'])}\n"
    
    template += """
## 各位建议

| 董事会成员 | 核心建议 | 关键理由 | 优先级 |
|----------|---------|---------|-------|
"""
    
    for member in members:
        template += f"| {member} |  |  | 高/中/低 |\n"
    
    template += """
## 汇总分析

### 共识点
（多位成员都提到的建议）

- 

### 分歧点
（不同视角的冲突）

- 

### 盲点
（我之前没想到的）

- 

## 我的决定

### 最终决策


### 行动计划
1. 
2. 
3. 

### 时间节点


## 复盘记录

**决策日期**：
**执行结果**：
**哪位成员的建议最准确**：
**学到的经验**：
"""
    
    return template


def list_members():
    """列出所有董事会成员"""
    print("\n=== 个人董事会成员列表 ===\n")
    for name, info in BOARD_MEMBERS.items():
        print(f"{name} - {info['role']}")
        print(f"  擅长：{', '.join(info['expertise'])}")
        print(f"  语录：{info['quote']}")
        print()


def main():
    if len(sys.argv) < 2:
        print("使用方法：")
        print("  python decision_template.py \"你的问题描述\" [问题类型]")
        print("\n问题类型可选：职业选择、情绪困扰、创新突破、女性成长、产品决策、重大决策")
        print("\n查看成员列表：")
        print("  python decision_template.py --list")
        return
    
    if sys.argv[1] == "--list":
        list_members()
        return
    
    problem = sys.argv[1]
    problem_type = sys.argv[2] if len(sys.argv) > 2 else "默认"
    
    template = generate_template(problem, problem_type)
    print(template)
    
    # 保存到文件
    filename = f"decision_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"\n✅ 模板已保存到：{filename}")


if __name__ == "__main__":
    main()