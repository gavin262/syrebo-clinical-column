# -*- coding: utf-8 -*-
"""Narrative copy for the 11 clinical-column articles.

Facts stay inside what the column already reported, plus the device and
outcome details the Huashan SY-HR03E pilot itself publishes (issue 05).
Numbers are framed as study findings. Issue 10 does not rank products.
"""

from __future__ import annotations

ARTICLES: dict[int, dict[str, dict]] = {}


def add(n: int, lang: str, **fields) -> None:
    ARTICLES.setdefault(n, {})[lang] = fields


# --- Chinese -----------------------------------------------------------------

add(
    1, "zh",
    title="急性期脑卒中手功能：NP 脑科医院机器人手辅助训练的随机对照研究",
    desc="土耳其 NP 脑科医院 30 例急性期脑卒中随机对照研究，在常规神经发育疗法之外增加机器人手训练，九孔柱、ABILHAND 与 Barthel 的组间结果以论文报告为准。",
    lead="脑卒中后的手，常常比腿更慢地回到日常生活：杯子、纽扣和餐具都会变成具体的障碍。急性期是神经功能变化较快的阶段，这个窗口里加进去的训练，需要随机对照而不是个案印象来衡量。2026 年《Scientific Reports》发表了土耳其 NP 脑科医院的一项随机对照研究，在常规神经发育疗法之外增加 Syrebo 机器人手辅助训练。论文报告，机器人手组在精细动作、双手日常活动和生活自理三项指标上的改善大于仅接受常规治疗的对照组；样本量只有 30 例，痉挛指标没有看到组间差异。",
    bg=[
        "手的恢复难，是因为它同时要求力量、分离运动和日常使用。下肢可以先把步行当作单一目标，手却要在不稳定的姿势里完成抓、放和双手配合。常规神经发育疗法已经是急性期康复的基础，但治疗师能一对一重复的次数有限，训练剂量和动作一致性不容易拉开。",
        "软体机器人手套用柔性驱动帮助手指反复开合，理论上可以在治疗师监督下把这部分重复做够。急性期患者的病情仍在变化，设备能不能安全地加进常规方案、加上之后功能指标是否跟着变化，都需要对照设计。这篇研究填的就是这个阶段的空白，而不是慢性期训练的又一次重复。",
    ],
    device="文中训练设备写为 SYREBO 机器人手。专栏配图为软体康复手套、主机与平板训练系统的产品照片，便于读者辨认设备形态；具体型号与参数以论文和临床方案为准。",
    design="单中心随机对照。机器人手组在常规神经发育疗法（NT）之外增加机器人手辅助训练；对照组只做常规神经发育疗法。主要看的是手部精细动作、双手日常活动能力和生活自理，而不是单一的肌力。",
    sample="土耳其 NP 脑科医院纳入 30 例急性期脑卒中患者并随机分组。机器人手训练为每周 3 次、共 8 周。论文同时观察了痉挛相关指标。",
    result="论文报告，机器人手组在九孔柱测试（精细动作）、ABILHAND（双手日常活动）和 Barthel 指数（生活自理）上的改善均大于对照组。这是该研究的组间发现，不能写成产品保证的恢复速度。痉挛指标的组间差异不显著，说明并不是每一项检查都随这套方案分开。",
    sig=[
        "这项研究把机器人手训练放进急性期、并且和常规神经发育疗法对照，补的是“最早这一段”的证据，而不是把慢性期结论往前挪。三项功能指标一起变化，提示论文作者看到的不只是某一次检查的波动。",
        "30 例的随机对照只能支持可行性方向上的谨慎阅读。它没有回答家庭长期使用，也没有证明每一种卒中类型都会得到同样的轨迹。后续方案仍应由接诊的医生或治疗师决定。",
    ],
    limit="样本量 30 例，属小样本；痉挛指标未见显著组间差异。上述分数变化是该研究的报告，不是对个体疗效的承诺。",
)

add(
    2, "zh",
    title="卒中后手功能：软体机器人手套与镜像疗法的单盲随机对照及 6 个月随访",
    desc="《Journal of Rehabilitation Medicine》49 例单盲随机对照，比较软体机器人手套与镜像疗法，并随访到 6 个月。盒与块、握力和 FMA-UE 的组间 P 值以论文报告为准。",
    lead="镜像疗法用视觉错觉带动患侧，是卒中后手康复里很常见的一种做法；软体机器人手套则用柔性驱动把开合重复做出来。二者谁能把变化留得更久，不能靠训练结束时的一次评估回答。《Journal of Rehabilitation Medicine》2025 年发表的一项单盲随机对照，把软体机器人手套和镜像疗法比较了 8 周，并随访到 6 个月。论文报告，干预结束时手套组在盒与块测试、握力和上肢 Fugl-Meyer 评分上的组间改善具有统计学意义，而且 6 个月时这种改善仍然维持。",
    bg=[
        "手功能训练最容易被问的不是“结束时有没有分差”，而是“回家以后还在不在”。镜像疗法设备简单，依赖患者对镜中影像的注意；软体手套把重复交还给外部助力，对注意力和体力的要求不同。两种都是康复手段，不是品牌之间的排名。",
        "如果只比较训练刚结束的分数，可能会把短期刺激当成稳定变化。带 6 个月随访的随机对照，才可能看出组间差异有没有留在干预结束之后。这篇论文要填的就是这段随访证据。",
    ],
    device="专栏配图为镜像训练场景中的 E12 设备。原文设备型号以论文为准，配图不单独构成型号对应。",
    design="单盲随机对照，比较软体机器人手套与镜像疗法。结局包括手的抓放灵活度（盒与块测试）、握力，以及上肢运动功能（FMA-UE）。随访设在干预结束后 6 个月。",
    sample="纳入 49 例脑卒中后患者，随机分入两组。干预 8 周，并在 6 个月时再次评估。试验注册号 NCT05898971。",
    result="论文报告，干预结束时手套组相对镜像疗法组的组间改善为：盒与块测试 P=0.004，握力 P=0.011，FMA-UE P=0.021。6 个月随访时，手套组的改善仍然维持。这些 P 值是该研究的统计报告，只说明这次样本里的组间差异，不能外推成每名患者的恢复幅度。",
    sig=[
        "相对只做到干预结束的试验，这篇论文多了一层时间信息：组间差异没有在随访点消失。对临床阅读来说，这比单看结束时的排名更有用。",
        "49 例仍然是小样本，两组的基线、病变侧和是否在家继续练习，都会影响随访分数。结论适用于本论文的纳入人群和对照方式。",
    ],
    limit="小样本（49 例）。P 值与“改善得以维持”均来自该研究的报告，不是产品疗效承诺。",
)

add(
    3, "zh",
    title="亚急性期单侧忽略：SY-HRE12 机器人镜像训练的随机对照研究",
    desc="《NeuroRehabilitation》24 例亚急性期随机对照。两组都使用 SY-HRE12，比较镜像功能与预设被动运动，每次 30 分钟、每周 3 次、共 5 周。",
    lead="有些亚急性期患者不只有手的无力，还会忽略身体一侧的空间，情绪也一起受影响。机器人镜像训练的做法，是让健手的动作去带动患手，在重复里同时给视觉和运动反馈。2025 年《NeuroRehabilitation》发表的一项随机对照，比较了同一款软体手套上的两种用法：镜像功能，和设备预设的被动运动。论文报告，镜像训练在单侧忽略和抑郁相关结局上更占优势。样本只有 24 例。",
    bg=[
        "单侧忽略会让康复评分变难解释：患者不是单纯“手抬不起来”，而是对一侧空间的注意不够。传统镜子可以制造患手在动的错觉，但患手本身往往没有同步的运动。机器人镜像是把健侧动作映射到患侧手套上，让“看到”和“做到”发生在同一次重复里。",
        "如果两组用的不是同一类设备，组间差异就可能来自设备而不是用法。这项研究让两组都使用 SY-HRE12，只改变驱动方式，问的是“怎么练”，不是“有没有一台新机器”。",
    ],
    device="论文中的设备为 SYREBO SY-HRE12 软体康复手套。专栏配图为 E12 系列的控制器、动力手套与镜像手套，用于说明系统组成；本研究对应的是 SY-HRE12。",
    design="随机对照。两组均使用 SY-HRE12。一组使用设备的镜像功能，由健手带动患手；另一组使用设备预设的被动运动。关注单侧忽略、抑郁相关结局和日常生活活动。",
    sample="24 例亚急性期脑卒中患者，每组 12 例。每次 30 分钟，每周 3 次，持续 5 周。",
    result="论文报告，在这 24 例里，机器人镜像训练相对于预设被动运动，在单侧忽略和抑郁相关结局上表现更有优势。这是同一设备、两种用法之间的研究发现，不能写成“手套本身治疗忽略或抑郁”。对照组不是普通的镜子盒子。",
    sig=[
        "这篇论文的新意在于把问题从“要不要用手套”换成“同一副手套用镜像还是用被动模式”。对同时存在忽略和情绪负担的亚急性期患者，这是一个更具体的临床问题。",
        "24 例的结果只支持在本研究条件下谨慎阅读。它没有比较家庭独立使用，也没有给出可以保证的情绪或注意改善幅度。",
    ],
    limit="小样本（每组 12 例）。对照组是设备预设的被动运动，不是普通镜像盒。结局差异是该研究的报告。",
)

add(
    4, "zh",
    title="卒中后握力与运动功能：机器人训练手套的随机对照研究",
    desc="《SPORT TK》30 例随机对照。论文报告握力组间均数差 1.87（95%CI 0.39–3.35，P=0.015），Fugl-Meyer 组间均数差 16.67（95%CI 3.9–29.4，P=0.012）。原文未标注具体型号。",
    lead="卒中后的手，临床上常被分成两件分开看的事：握得住，和动得出来。2025 年《SPORT TK-EuroAmerican Journal of Sport Sciences》发表的一项随机对照，同时看了握力和 Fugl-Meyer 运动功能。论文报告，机器人训练手套组相对对照组，两项指标的组间均数差都有统计学意义。样本 30 例，原文没有标注具体手套型号。",
    bg=[
        "握力变化不一定带来可用的动作，动作评分上升也不等于日常能拿起杯子。把力量和运动功能放在同一项随机对照里，是为了避免只报告其中更好看的一项。",
        "软体或机器人训练手套的文献里，型号经常写得不完整。没有型号，就不能把某一款产品的参数直接套进结果。这篇专栏因此只讨论论文写明的组间差异，不补写设备规格。",
    ],
    device="",
    design="随机对照，比较机器人训练手套辅助训练与对照组。共同结局是握力和 Fugl-Meyer 运动功能评分。组间差以均数差和 95% 置信区间呈现。",
    sample="30 例脑卒中患者，每组 15 例。原文未报告可以对应到某一上市型号的设备名称。配图是通用软体手套示意，不是该研究的设备鉴定。",
    result="论文报告的组间均数差为：握力 1.87（95% 置信区间 0.39–3.35，P=0.015）；Fugl-Meyer 运动功能评分 16.67（95% 置信区间 3.9–29.4，P=0.012）。均数差是两组均值之差，不是每一位患者的提高分。置信区间很宽，尤其是运动功能评分，说明这次小样本里的估计并不精密。",
    sig=[
        "两项结局同时给出组间差异和区间，比只写“优于对照组”更便于临床阅读：可以看出差异的方向，也看得出不确定性有多大。",
        "因为原文没有型号，这项结果不能被复述成某一款 Syrebo 手套的参数或适应证。30 例的区间也留着很大的抽样波动。",
    ],
    limit="小样本（30 例）。原文未标注型号，配图不作型号对应。均数差和 P 值是该研究的统计报告。",
)

add(
    5, "zh",
    title="早期亚急性期手功能：华山医院团队 SY-HR03E 软体手套的单盲随机对照试点",
    desc="复旦大学附属华山医院团队在《BioMedical Engineering OnLine》报告的单盲随机对照试点：20 例早期亚急性期患者，SY-HR03E，4 周。论文报告方案完成且无不良事件，并给出手功能与生活活动的初步信号。",
    lead="早期亚急性期的手还处在变化里，这个阶段首先要回答的不是“能提高多少分”，而是这套训练能不能做完、安不安全。复旦大学附属华山医院贾杰教授团队等在《BioMedical Engineering OnLine》发表了一项单盲随机对照试点，评估 Syrebo SY-HR03E 软体机器人手套用于早期亚急性期手功能康复的可行性、安全性和初步疗效。论文报告，20 名患者都完成了 4 周训练，没有脱落，也没有不良事件；手功能评分两组都有改善，手套组的改善幅度更大，生活活动能力的组内显著变化出现在手套组。",
    bg=[
        "上肢和手的恢复常常晚于下肢。进食、穿衣、洗漱依赖的是分离的手指动作，而不是一个总的肌力数字。常规手功能训练有效，但治疗师能提供的重复次数有限，病房里也不容易把动作做得一致。",
        "软体手套用气压驱动手指屈伸，重量落在手套上的部分可以很轻，因此有人希望把它用到床旁。早期亚急性期的患者仍在自发恢复，任何“初步疗效”都必须和这段自然恢复分开看。随机对照试点的任务，是先证明方案可行，再为更大的试验提供信号，而不是代替确证性试验。",
    ],
    device="论文中的 Syrebo SY-HR03E 是商用软体康复手套，由手套和桌面控制单元组成。论文报告系统总重约 3.5 公斤，手套本身约 110 克。手套背部的气动软体波纹管辅助屈伸；压力传感器监测患者主动尝试时的气压变化，超过 0.7 kPa 的预设阈值后，系统识别运动意图并充气或放气，使患者处在主动—辅助而不是完全被动带动之中。",
    design="单盲随机对照试点。机器人治疗组在标准康复之外接受软体手套辅助的手部开合；常规治疗组接受等时长的传统手部康复。两组每天都有 1 小时标准常规康复。治疗师监督姿势。注册号 ChiCTR2000034614。",
    sample="20 名早期亚急性期住院患者（发病 7 天至 3 个月），每组 10 人。手套组每天 30 分钟开合训练，每周 5 天，共 4 周。每次开合后保持约 3 秒，再进入下一次辅助。作者单位包括临床团队，论文亦披露上海司羿智能科技有限公司的作者隶属，阅读时需要把这层关系算进去。",
    result="论文报告，20 人都完成 4 周干预，无脱落、无不良事件。手部 Fugl-Meyer 评分两组均有改善，机器人治疗组的改善幅度大于常规治疗组。改良 Barthel 指数方面，论文报告仅机器人治疗组达到组内统计学显著（p<0.001），常规治疗组未达到显著水平。手部 Brunnstrom 分期同样只有机器人治疗组显示出显著的组内改善。这些是试点样本里的信号：组内显著不等于已经证明日常功能会被普遍提高。",
    sig=[
        "既往软体手套研究很多做在慢性期。这项试点把同一问题放到发病 7 天至 3 个月，补的是早期窗口的可行性和安全性，而不是把慢性期疗效直接前移。",
        "手功能评分和生活活动评分没有呈同样的统计形态：论文报告 Barthel 的组内显著变化只出现在手套组。这种分离值得后续试验单独检验，但不能在 10 对 10 的试点里写成“生活能力已经被解决”。110 克的手套重量和意图识别，只说明设备有条件被拿到病房以外讨论，本研究本身做在住院场景。",
    ],
    limit="先导随机对照，每组 10 例。初步疗效信号需要更大样本确认。p 值是论文对该结局的报告。作者隶属中包含设备相关单位，解读时需一并考虑。",
)

add(
    6, "zh",
    title="痰瘀阻络型卒中手功能障碍：手套结合电针的 200 例四组临床研究",
    desc="《湖南中医药大学学报》200 例四组研究。论文报告的总有效率：手套结合电针 88%，手套 76%，电针 77.6%，常规康复 70.8%。这是该研究的复合口径，不是产品有效率。",
    lead="把机器人手套和电针放在同一方案里，是中西医结合康复里的一种具体做法，但它回答的问题必须写清楚：看到的变化属于哪一条臂，不能自动算到手套头上。2022 年《湖南中医药大学学报》发表的一项四组临床研究，纳入 200 例痰瘀阻络型脑卒中手功能障碍患者，比较手套结合电针、单用手套、单用电针和常规康复。论文用“总有效率”报告：结合组 88%，手套组 76%，电针组 77.6%，常规康复组 70.8%。这是作者自己的复合判定，不是产品说明书上的有效率。",
    bg=[
        "手功能障碍在痰瘀阻络这一中医分型下，临床路径常常同时包含现代康复和电针。四组平行设计的好处，是可以把“联用”“单用设备”“单用电针”和“常规康复”放在同一口径下看，而不是只用前后对照讲一个上升的故事。",
        "总有效率把多种结局收成一个百分比，读的时候要先问清分母和判定标准。它便于组间对照，却不能还原成每一位患者的功能分变化，更不能被引用成“手套的有效率是 88%”。",
    ],
    device="",
    design="四组临床研究：康复机器人手套结合电针、单用手套、单用电针、常规康复。结局以论文报告的总有效率呈现。作者单位包括上海司羿智能科技有限公司，尹刚刚为共同作者，这一隶属需要在阅读时保留。",
    sample="200 例痰瘀阻络型脑卒中手功能障碍患者，是本专栏各篇里样本量最大的一项。原文未标注可以对应到某一型号的设备名称。配图为通用示意，不作型号宣称。",
    result="论文报告的总有效率为：手套结合电针组 88%，手套组 76%，电针组 77.6%，常规康复组 70.8%。结合组高于单用组，只能说明在该研究的判定口径下，联用臂的复合结局更高；不能把 88% 单独归因于手套，也不能把 76% 写成产品有效率。电针组与手套组的数字接近，更不支持把差异全部解释成某一种干预。",
    sig=[
        "四组、200 例，提供的是一个可以对照的复合结局，而不是一个可以印在产品页上的百分比。把它放回“总有效率”这一口径里，读者才能看出联用、单用和常规康复之间的差距其实有限。",
        "原文没有给出与本专栏其他随机对照相同的量表均数差。在那些量表公布之前，这篇论文更适合用来讨论方案如何组合，而不是用来承诺手功能会提高多少。",
    ],
    limit="总有效率是该研究的自有报告口径。联合组的结果不能单独归因于手套或电针。原文未标注具体型号。",
)

add(
    7, "zh",
    title="大脑中动脉梗死后的手康复：一例 66 岁患者的病例报告",
    desc="《Cureus》病例报告：66 岁女性，双侧大脑中动脉区域梗死，在专业人员指导下使用 Syrebo 手套康复方案。单例，不外推疗效。",
    lead="随机对照回答的是一组人的平均差异，病例报告回答的是一个人的康复是怎样被安排的。2024 年《Cureus》发表 Sharma 等人的病例报告，记录一位 66 岁女性在双侧大脑中动脉区域梗死之后，接受以 Syrebo 手套康复方案为核心的神经物理治疗。报告描述了观察和功能变化的过程。它是单例，不能外推成这套方案的普遍结果。",
    bg=[
        "大脑中动脉供血区梗死常常同时影响上肢、手和认知或语言相关功能，康复安排要比单一的手无力复杂。家属最需要的往往不是一个百分比，而是：病情稳定之后，手套训练在整个物理治疗里占哪一段、由谁监督。",
        "病例报告适合把这段过程写清楚。它不设平行对照，因此任何前后变化都同时包含自然恢复、常规治疗和手套训练，不能拆成设备的独立贡献。",
    ],
    device="论文讨论的是 Syrebo 手套康复方案。原文未标注具体型号。专栏中的手套与主机照片来自该开放获取论文的图 2（CC BY 4.0），已放在文首文献摘录，不是另一篇综述的配图。",
    design="单例病例报告，不是随机对照。干预是病情稳定后、由专业人员实施的神经物理治疗，其中包含 Syrebo 手套康复方案。",
    sample="66 岁女性，诊断为双侧大脑中动脉区域梗死。报告记录康复过程中的观察与功能变化，没有提供可与随机对照直接比较的组间统计。",
    result="这篇报告的价值是过程，不是一个可以引用的提高率。它说明在专业人员指导下，软体手套如何进入一位重症脑梗死患者的康复安排。读者不应把个例里的变化理解成产品保证的恢复程度。",
    sig=[
        "在本专栏以随机对照为主的序列里，保留一篇病例报告，是为了把“方案如何被用在一个人身上”写出来。它填的是叙事上的空白，不是证据等级上的升级。",
        "单例不能估计不良反应的发生率，也不能回答早期、亚急性或慢性哪一段更合适。那些问题仍然要回到对照研究。",
    ],
    limit="单病例报告，不外推为普遍疗效。功能变化不能单独归因于手套。",
)

add(
    8, "zh",
    title="卒中后上肢功能障碍：创新式镜像疗法的 60 例随机分组研究",
    desc="《新医学》2024 年 60 例随机分组、干预 4 周。论文报告创新式镜像疗法组在 FMA-UE、FMA-WH 和改良 Barthel 指数上的改善大于传统镜像疗法组。",
    lead="传统镜像疗法用一面镜子制造“患手在动”的视觉；创新式做法是让机器人手套带着患手，做出与镜中影像一致的动作，把看到和做到放在同一次训练里。2024 年《新医学》发表陈涛等人的随机分组研究，用 60 例患者比较了这两种做法，干预 4 周。论文报告，创新式镜像疗法组在上肢运动功能、腕手功能和日常生活能力上的改善大于传统镜像疗法组。",
    bg=[
        "镜像疗法被用了很多年，限制也清楚：如果患手本身动不了，视觉错觉缺少同步的运动输入。把手套的辅助屈伸接到镜像任务上，是为了让患侧在治疗师设定的范围内真正完成动作，而不是只看镜子。",
        "这种改动是否改变功能评分，需要和传统镜子对照，而不是和“什么都不做”对照。60 例、两组各半，是一个初步的随机分组规模。",
    ],
    device="原始期刊页面的训练图可见“羿生”标识。专栏据此对应官方资料中的 SY-HR08E，并配有含大屏、主机与手套的产品图。这一对应是资料核对，不是论文里的注册型号声明。",
    design="随机数表分组。创新式镜像疗法（镜像任务结合机器人手套）对照传统镜像疗法。结局包括 FMA-UE（上肢）、FMA-WH（腕手）和改良 Barthel 指数。",
    sample="60 例脑卒中上肢功能障碍患者，每组 30 例，干预 4 周。",
    result="论文报告，创新式镜像疗法组在 FMA-UE、FMA-WH 和改良 Barthel 指数上的改善大于传统镜像疗法组。这是该研究的组间描述。原文复核仍在进行时，具体均数与 P 值以期刊页面为准，本专栏不补写论文未在此处核对的数字。",
    sig=[
        "相对传统镜子，这项研究问的是“加上与影像一致的辅助动作之后，评分是否不同”。60 例给出的是初步对照，不是家庭康复方案的证明。",
        "品牌标识与 SY-HR08E 的对应只帮助读者辨认设备形态。功能差异是否稳定，还要等全文数字被独立复核。",
    ],
    limit="每组 30 例。评分差异以论文报告为准；均数和 P 值未在本页另作计算。设备型号对应来自期刊图与官方资料的核对。",
)

add(
    9, "zh",
    title="大脑中动脉梗死后的左侧偏瘫：法拉第电刺激联合机器人手的一例记录",
    desc="《IJPRCP》病例报告：60 岁男性，左侧偏瘫，卒中后 3 个月余开始法拉第电刺激联合 Syrebo C12，每周 5 次、共 4 周。单例联合干预，不单独归因。",
    lead="偏瘫后的手，有时会被安排两种同时进行的手段：电刺激试图兴奋肌肉，机器人手带动手指完成开合。2025 年《International Journal of Physiotherapy Research and Clinical Practice》的一篇病例报告，记录了一位左侧偏瘫患者接受法拉第电刺激联合 Syrebo C12 的 4 周过程。它是联合方案的实施记录，不是某一种设备的疗效试验。",
    bg=[
        "病程进入数月之后，手的变化通常变慢，临床人员会考虑在常规训练上叠加电刺激或外部助力。两种手段一旦同时使用，前后评分的变化就无法干净地分给其中一种。",
        "病例报告仍然有用：它把开始的时间、频率和设备写下来，让后来的方案有一个可核对的参照。它不提供发生率，也不提供与对照治疗的差异。",
    ],
    device="报告中的机器人手康复设备为 Syrebo C12。配图来自 C12 产品页的官方图片裁切，用于辨认控制器与手套，不增加论文没有写出的参数。",
    design="单例、联合干预：法拉第电刺激与 Syrebo C12 机器人手康复同时进行。没有平行对照组。",
    sample="60 岁男性，左侧偏瘫。于脑卒中后 3 个月 2 周开始，每周 5 次，持续 4 周。",
    result="本页不转写论文未在专栏中核对的功能分数。可以确定的是实施过程：电刺激与机器人手训练被一起用于这一例，因此任何变化都不能单独写成 C12 或电刺激的效果。",
    sig=[
        "这篇记录补充的是“病程三个月之后，联合方案可以怎样排进一周五次的治疗”。它不提高证据等级。",
        "左侧偏瘫、大脑中动脉梗死这一诊断路径下的个例，不能代表其他病灶或其他病程。",
    ],
    limit="单病例联合干预。变化不单独归因于 C12 或电刺激，不外推为普遍疗效。",
)

add(
    10, "zh",
    title="软体腕手矫形器：范德堡大学团队在《Wearable Technologies》的设计与初步评价",
    desc="Ledoux 与 Barth 在《Wearable Technologies》报告自行设计的 3D 打印腕手抓握矫形器。本文只介绍该设计研究，不引用商业产品排名，也不把它当作疗效试验。",
    lead="2024 年剑桥大学出版社的《Wearable Technologies》发表了范德堡大学 Ledoux 与 Barth 的一篇设计论文：作者制作的是他们自己的 3D 打印腕手抓握矫形器，并做了初步评价。论文在讨论可穿戴手部装置时提到了商用软体结构。本专栏不把这种讨论改写成产品之间的名次，也不把它当作 Syrebo 的疗效证据。",
    bg=[
        "手部装置要离开治疗室，首先面对的是重量、轮廓和患者能否自己穿脱。设计论文通常先写约束条件，再写样机，而不是先报告一份多中心的功能试验。把设计论文读成疗效论文，会把尚未测量的临床结局说成已经测量。",
        "软体路线和刚性外骨骼回答的工程问题不同。前者把材料的柔性当作减少轮廓的办法。这是设计选择，需要单独的人体试验才能谈论功能变化。",
    ],
    device="文首文献摘录是该开放获取论文的首页题录（CC BY 4.0），不是结果对照表。专栏产品图只说明 Syrebo 临床手套系统的外观，不表示该图来自这篇论文的试验。",
    design="设计、建模与初步评价。对象是作者自己的 3D 打印腕手抓握矫形器。论文不是针对 Syrebo 的随机对照，也不是上市产品之间的疗效比较。",
    sample="论文的人体部分是对样机的初步评价，规模和任务都以原文为准。本专栏不把这一样本复述成 Syrebo 的临床队列。",
    result="本页不摘录论文里的商业产品形容词，也不排列其他品牌。可以保留的信息只有：这是一项开放获取的设计研究，作者在讨论软体、可穿戴结构；其中的推测性用语（原文 presumably）说明作者自己没有把舒适度写成已测量的终点。",
    sig=[
        "把它收进专栏，是为了把“设计论文”和“疗效试验”分开。软体结构是否让设备更接近日常佩戴，仍然要由佩戴试验和功能试验分别回答。",
        "开放获取使读者可以直接核对原文用词。核对的目的是避免把推测句写成结论，而不是为了选出一个最轻的产品。",
    ],
    limit="不是 Syrebo 的疗效试验，也不作产品间排名。原文对舒适度使用了推测限定。首页截图不包含对照表。",
)

add(
    11, "zh",
    title="面向居家的手指康复机器人：日本机器人学会誌中的开发记述",
    desc="《日本机器人学会誌》2023 年文章讨论面向居家的片麻痺手指康复机器人，并提到 Syrebo 是少数已产品化的例子之一。这不是临床试验。",
    lead="居家手康复说了很多年，真正写进学会论文的产品化例子仍然少。2023 年《日本机器人学会誌》刊登古館裕大等人的文章，主题是面向居家使用的片麻痺手指康复机器人，以及开发过程中如何与医疗人员协作。作者在论述中指出，已实现产品化的案例很少，并把 Syrebo 手功能康复手套列为其中的例子。这是一篇开发与协作的记述，不是疗效试验。",
    bg=[
        "从病房到家庭，中间差的是穿脱、安全边界和没有治疗师在场时的使用。工程论文会把这些约束写在与临床人员的协作里。被点名，说明作者在举例时想到了这一产品，不等于学会完成了一项对照研究。",
        "“少数已经产品化”同时是一种限制：作者强调这类例子仍然少。读成“居家康复已经普遍实现”，会把举例写成流行病学结论。",
    ],
    device="该文没有刊出手套照片。专栏所用的手套与主机图片来自 Sharma 等人 2024 年《Cureus》病例报告的图 2（CC BY 4.0），已在图注中说明，不能当作日本机器人学会这篇论文的原图。",
    design="学会期刊上的开发记述，讨论居家场景下的手指康复机器人，以及与医疗人员的协作。没有随机分组，没有功能量表的组间比较。",
    sample="不适用临床样本量。文章评论的是产品化路径，而不是一批患者的结局。",
    result="论文的表述是：面向家庭、已经产品化的手指康复机器人仍然少，Syrebo 是被提到的例子之一。本专栏按这个范围引用，不把它改写成疗效、市场排名或“患者在家一定能完成训练”。",
    sig=[
        "这篇记述的价值，是把居家使用写成一个需要和医疗人员一起定义的工程问题。产品化例子的存在，只说明有设备走完了从样机到产品的一步。",
        "家庭里能否安全、持续地使用，仍然要看适应证、监督和单独的临床研究。学会论文没有提供这些数据。",
    ],
    limit="不是针对 Syrebo 的临床试验。原文强调产品化案例仍少。配图来自另一篇开放获取病例报告。",
)

# --- English (source for the other locales) ---------------------------------

add(
    1, "en",
    title="Hand function in acute stroke: a randomized trial of robot-assisted training at NP Brain Hospital",
    desc="A 30-patient randomized trial at NP Brain Hospital added robot-assisted hand training to neurodevelopmental therapy. Nine-Hole Peg, ABILHAND, and Barthel findings are reported as study results.",
    lead="After stroke, the hand often returns to daily tasks more slowly than walking: a cup, a button, or a utensil becomes a specific obstacle. The acute window changes quickly, so anything added there needs a randomized comparison rather than a case impression. In 2026 Scientific Reports published a randomized trial from NP Brain Hospital in Turkey that added Syrebo robot-assisted hand training to conventional neurodevelopmental therapy. The paper reports greater gains on dexterity, bimanual activities, and self-care than therapy alone. The sample is 30 people, and spasticity did not separate the groups.",
    bg=[
        "The hand is difficult because it needs force, fractionated movement, and actual use. Gait can be practiced as one target; the hand has to grasp and release inside an unsteady posture. Neurodevelopmental therapy is already the base of acute rehabilitation, but a therapist cannot repeat every grasp indefinitely, so dose and consistency are hard to stretch.",
        "A soft robotic glove can, in principle, supply those repetitions under supervision. Acute patients are still changing. Whether the device can be added safely, and whether functional scores move with it, is a controlled question. This trial addresses that stage rather than repeating a chronic-phase study.",
    ],
    device="The paper names the device as a SYREBO robotic hand. The photograph shows a soft glove, console, and tablet so readers can see the form factor. Model details belong to the paper and the clinical protocol.",
    design="A single-center randomized comparison. One group received robot-assisted hand training plus neurodevelopmental therapy (NT). The control group received NT alone. The outcomes were fine dexterity, bimanual daily activities, and self-care, not strength alone.",
    sample="NP Brain Hospital enrolled 30 people in the acute phase and randomized them. Robot-assisted sessions were three times a week for eight weeks. Spasticity measures were collected as well.",
    result="The paper reports larger improvements in the robot-assisted group on the Nine-Hole Peg Test, the ABILHAND questionnaire, and the Barthel Index. That is a between-group finding in this sample. It is not a promised recovery speed. Spasticity did not show a significant between-group difference, so not every measure moved apart.",
    sig=[
        "The useful part is the timing: robot-assisted practice was tested in the acute phase against ongoing neurodevelopmental therapy, rather than borrowed from chronic-phase results. Three functional measures moving together is more informative than a single score.",
        "Thirty randomized patients can only support a cautious reading. The trial does not answer long-term home use, and it does not show that every stroke subtype follows the same path. The treating clinician still sets the plan.",
    ],
    limit="Small sample (n=30). No significant between-group difference on spasticity. Score changes are the study’s report, not an individual promise.",
)

add(
    2, "en",
    title="Post-stroke hand function: a single-blind RCT of a soft robotic glove and mirror therapy, with 6-month follow-up",
    desc="Journal of Rehabilitation Medicine, 2025: 49 participants, soft robotic glove versus mirror therapy, eight weeks plus six-month follow-up. Between-group P values are the paper’s report.",
    lead="Mirror therapy uses visual input to recruit the affected side. A soft robotic glove uses compliant actuation to repeat opening and closing. Which change lasts longer cannot be answered at the last training day. A 2025 single-blind randomized trial in the Journal of Rehabilitation Medicine compared the two approaches for eight weeks and followed people to six months. The paper reports statistically significant between-group gains for the glove on the Box and Block Test, grip strength, and FMA-UE at the end of training, and reports that those glove-group gains were still present at six months.",
    bg=[
        "The question that matters after hand training is whether the change is still there after people go home. Mirror therapy is simple and depends on attention to the reflected limb. A glove shifts repetition onto an external actuator, with a different demand on attention and endurance. Both are rehabilitation methods. This is not a ranking of brands.",
        "A score on the final training day can confuse a short stimulus with a stable change. A randomized comparison with a six-month visit is what makes that distinction possible.",
    ],
    device="The column photograph shows an E12 mirror-training setup. The study device is whatever the paper specifies; the photo is not a model match.",
    design="Single-blind randomization of a soft robotic glove against mirror therapy. Outcomes were grasp-and-release dexterity (Box and Block), grip strength, and upper-limb movement (FMA-UE), with a visit six months after training.",
    sample="Forty-nine people after stroke were randomized. Training lasted eight weeks. The registry entry is NCT05898971.",
    result="At the end of training the paper reports between-group differences favoring the glove: Box and Block P=0.004, grip P=0.011, FMA-UE P=0.021. At six months the glove group’s gains were still present. Those P values describe this sample. They do not assign a recovery size to every patient.",
    sig=[
        "The extra information is time. The between-group difference had not disappeared at the follow-up visit. That is more useful clinically than a ranking on the last training day.",
        "Forty-nine people is still a small trial. Baseline differences, lesion side, and practice after discharge can all move a six-month score. The finding belongs to this population and this contrast.",
    ],
    limit="Small sample (n=49). P values and maintained gains are the study’s report, not a product promise.",
)

add(
    3, "en",
    title="Unilateral neglect in subacute stroke: a randomized comparison of robotic mirror training on the SY-HRE12",
    desc="NeuroRehabilitation, 2025: 24 people in the subacute phase, all using the SY-HRE12. Mirror mode versus preset passive motion, 30 minutes, three times a week, for five weeks.",
    lead="Some people in the subacute phase have more than a weak hand. They may also neglect one side of space, and mood may suffer with it. Robotic mirror training maps the less-affected hand onto the affected one, so vision and movement arrive in the same repetition. A 2025 randomized trial in NeuroRehabilitation compared two ways of using the same soft glove: its mirror function, and a preset passive mode. The paper reports an advantage for mirror training on neglect-related and depression-related outcomes. The sample is 24 people.",
    bg=[
        "Neglect makes scores hard to read. The problem is not only that the hand will not lift; attention to one side of space is reduced. A conventional mirror can suggest that the affected hand is moving when it is not. Robotic mirroring tries to make the affected glove move with the other hand, so seeing and doing occupy the same trial.",
        "If the groups used different devices, any difference could be the hardware. This trial gave both groups the SY-HRE12 and changed only the mode. The question is how the glove was driven, not whether a new machine was present.",
    ],
    device="The paper used the SYREBO SY-HRE12. The photograph shows an E12 controller, powered glove, and mirror glove so the system is recognizable. The study device is the SY-HRE12.",
    design="Randomized comparison. Both groups used the SY-HRE12. One group used the mirror function. The other used preset passive motion. Outcomes included unilateral neglect, depression-related measures, and daily activities.",
    sample="Twenty-four people in the subacute phase, 12 in each group. Sessions lasted 30 minutes, three times a week, for five weeks.",
    result="In this sample the paper reports an advantage for robotic mirror training over preset passive motion on neglect-related and depression-related outcomes. That is a difference between two modes of one device. It does not mean the glove treats neglect or depression. The control condition was not an ordinary mirror box.",
    sig=[
        "The shift in question is from “whether to use a glove” to “which mode of the same glove.” For people who also have neglect and mood burden, that is a more precise clinical question.",
        "Twenty-four participants support only a cautious reading. The trial does not test unsupervised home use, and it does not offer a guaranteed change in attention or mood.",
    ],
    limit="Small sample (12 per group). The control mode was preset passive motion, not a mirror box. Differences are the study’s report.",
)

add(
    4, "en",
    title="Grip and motor scores after stroke: a randomized trial of robotic training gloves",
    desc="SPORT TK, 2025: 30 participants. Reported mean differences: grip 1.87 (95% CI 0.39–3.35, P=0.015) and Fugl-Meyer 16.67 (95% CI 3.9–29.4, P=0.012). No model is named.",
    lead="After stroke, clinicians often split the hand into two practical problems: whether it can grip, and whether it can move with control. A 2025 randomized trial in SPORT TK-EuroAmerican Journal of Sport Sciences measured both. The paper reports statistically significant between-group mean differences favoring robotic training gloves on grip and on the Fugl-Meyer motor score. Thirty people took part, and the paper does not name a commercial model.",
    bg=[
        "A change in grip need not produce a usable movement, and a higher motor score need not mean a person can lift a cup. Measuring force and movement in the same randomized comparison avoids publishing only the kinder of the two.",
        "Glove papers often omit the model. Without a model, a result cannot be copied onto a product specification. This summary therefore stays with the contrasts the paper actually gives.",
    ],
    device="",
    design="Randomized comparison of robotic training-glove practice against a control condition. Shared outcomes were grip and the Fugl-Meyer motor score, reported as mean differences with 95% confidence intervals.",
    sample="Thirty people after stroke, 15 in each group. The paper does not identify a marketed model. The generic glove photograph is an illustration, not a device identification.",
    result="The reported between-group mean differences are grip 1.87 (95% CI 0.39 to 3.35, P=0.015) and Fugl-Meyer 16.67 (95% CI 3.9 to 29.4, P=0.012). A mean difference is not the gain of each person. The motor-score interval is wide, which is what a small sample looks like when the estimate is imprecise.",
    sig=[
        "Publishing both the difference and the interval is more usable than the sentence “better than control.” The direction is visible, and so is the uncertainty.",
        "Because no model is named, the result cannot be retold as a specification or an indication for a particular Syrebo glove. Thirty people also leave room for sampling noise.",
    ],
    limit="Small sample (n=30). No model is identified, and the photo is not a match. Mean differences and P values are the study’s statistics.",
)

add(
    5, "en",
    title="Early subacute hand function: a single-blind pilot RCT of the SY-HR03E from the Huashan team",
    desc="A single-blind pilot RCT in BioMedical Engineering OnLine: 20 inpatients, SY-HR03E, four weeks. The paper reports full completion, no adverse events, and preliminary signals on hand scores and daily activities.",
    lead="In the early subacute phase the first question is not how many points a score might rise. It is whether the sessions can be finished, and whether they are safe. A team led by Professor Jia Jie at Huashan Hospital, Fudan University, published a single-blind pilot randomized trial in BioMedical Engineering OnLine on the Syrebo SY-HR03E for hand rehabilitation in that window. The paper reports that all 20 participants finished four weeks, with no dropouts and no adverse events. Hand scores improved in both groups, with a larger change in the glove group. A within-group change in daily activities reached statistical significance in the glove group.",
    bg=[
        "The arm and hand usually recover later than walking. Eating, dressing, and washing depend on fractionated finger movement, not on one strength number. Conventional hand therapy helps, but the number of repetitions a therapist can deliver is limited, and the same movement is hard to repeat at the bedside.",
        "A pneumatic glove can flex and extend the fingers with little mass on the hand, which is why bedside use is discussed. People in the early subacute phase are also recovering spontaneously. Any “preliminary effect” has to be read against that background. A pilot randomized trial is there to show that a protocol is feasible and to leave a signal for a larger study. It does not replace a confirmatory trial.",
    ],
    device="The paper describes the SY-HR03E as a commercial soft glove plus a tabletop controller. Reported mass is about 3.5 kg for the system and about 110 g for the glove. Pneumatic bellows on the back of the hand assist flexion and extension. Pressure sensors watch the change produced when the person tries to move; above a preset threshold of 0.7 kPa the controller treats that change as movement intention and inflates or deflates. The intended mode is active-assist, not a fully passive pull.",
    design="Single-blind pilot randomization. The robotic group added glove-assisted opening and closing to standard rehabilitation. The conventional group received traditional hand therapy of the same session length. Both groups also received one hour a day of standard rehabilitation. A therapist supervised posture. Registry: ChiCTR2000034614.",
    sample="Twenty inpatients, 7 days to 3 months after onset, 10 in each group. Glove sessions were 30 minutes a day, five days a week, for four weeks. Each open-close was held for about three seconds. Author affiliations include the clinical team and, as disclosed in the paper, Shanghai Siyi Intelligent Technology. That relationship belongs in the reading.",
    result="The paper reports that all 20 people completed four weeks, with no dropouts and no adverse events. Hand Fugl-Meyer scores improved in both groups, with a larger improvement in the robotic group. On the modified Barthel Index, only the robotic group’s within-group change is reported as statistically significant (p<0.001); the conventional group’s within-group change is not. Hand Brunnstrom stage likewise showed a significant within-group change only in the robotic group. In a 10-versus-10 pilot, a within-group P value is a signal, not evidence that daily function will rise for patients in general.",
    sig=[
        "Many soft-glove studies enroll people in the chronic phase. This pilot moves the feasibility and safety question into the window from 7 days to 3 months. It does not move chronic-phase efficacy claims earlier.",
        "Hand scores and daily-activity scores did not take the same statistical shape: the paper reports a significant within-group Barthel change only in the glove group. That split is worth testing again. It is not a statement that activities of daily living have been solved. A 110 g glove and intent detection make bedside and, later, home discussion possible. This study itself was done with inpatients.",
    ],
    limit="Pilot randomization, 10 per group. Preliminary signals need a larger sample. The P value is the paper’s report for that outcome. A device-related affiliation is disclosed and should be weighed.",
)

add(
    6, "en",
    title="Hand impairment with phlegm-stasis pattern: a 200-person, four-arm study of a glove plus electroacupuncture",
    desc="Journal of Hunan University of Chinese Medicine: 200 participants, four arms. Reported total effective rates were 88%, 76%, 77.6%, and 70.8%. Those figures are the study’s composite, not a product rate.",
    lead="Putting a robotic glove and electroacupuncture in one plan is a specific integrative choice, and the result has to stay attached to the arm that produced it. A 2022 four-arm study in the Journal of Hunan University of Chinese Medicine enrolled 200 people with stroke hand impairment of the phlegm-stasis pattern and compared glove plus electroacupuncture, glove alone, electroacupuncture alone, and usual rehabilitation. The paper’s own “total effective rates” are 88%, 76%, 77.6%, and 70.8%. That composite is the authors’ summary. It is not a product efficacy rate.",
    bg=[
        "Under this pattern diagnosis, pathways often combine modern rehabilitation with electroacupuncture. A four-arm layout can show combination, device alone, acupuncture alone, and usual care on one scale, instead of a before-after story with no contrast.",
        "A total effective rate collapses several judgments into one percentage. It is useful for a coarse contrast and useless as a person’s change on a named scale. It cannot be quoted as “the glove’s efficacy is 88%.”",
    ],
    device="",
    design="Four arms: robotic glove plus electroacupuncture, glove alone, electroacupuncture alone, and usual rehabilitation. The outcome discussed here is the paper’s total effective rate. Author affiliations include Shanghai Siyi Intelligent Technology, with Yin Ganggang as a coauthor. That disclosure stays with the reading.",
    sample="Two hundred people with hand impairment after stroke in the phlegm-stasis pattern. This is the largest sample in the column. The paper does not name a model that can be matched to a current product, and the generic photograph is not such a match.",
    result="The reported total effective rates are 88% for glove plus electroacupuncture, 76% for the glove alone, 77.6% for electroacupuncture alone, and 70.8% for usual rehabilitation. A higher composite in the combined arm means only that, under this study’s rule, that arm scored higher. It does not assign 88% to the glove, and 76% is not a product rate. The glove-alone and electroacupuncture-alone figures sit close together, which also argues against explaining the whole pattern by one component.",
    sig=[
        "Two hundred people and four arms give a contrastable composite, not a percentage for a product page. Read as a total effective rate, the gaps between combination, single modalities, and usual care are limited.",
        "The paper, as summarized here, does not supply the same mean differences used in the column’s other trials. Until those scales are on the table, the study is about how the components were combined, not about how many points a hand score will rise.",
    ],
    limit="The percentages are the study’s own total effective rates. The combined arm cannot be attributed to the glove or to electroacupuncture alone. No model is named.",
)

add(
    7, "en",
    title="Hand rehabilitation after middle-cerebral-artery infarction: a case report of one 66-year-old patient",
    desc="Cureus case report: a 66-year-old woman with bilateral MCA-territory infarction received a Syrebo glove program under clinical supervision. A single case is not a general result.",
    lead="A randomized trial describes an average difference. A case report describes how rehabilitation was arranged for one person. In 2024 Cureus, Sharma and colleagues reported a 66-year-old woman with infarction in the middle-cerebral-artery territories who received neurophysiotherapy built around a Syrebo glove program. The report follows the course of observation and functional change. It is one case, and it does not generalize.",
    bg=[
        "Infarction in this territory often affects the arm and hand together with language or cognition, so the plan is more than a weak hand. Families usually need to know when glove practice sat inside physiotherapy, and who supervised it, more than they need a percentage.",
        "A case report can write that sequence down. It has no parallel control, so any before-after change mixes spontaneous recovery, usual care, and the glove. Those pieces cannot be separated.",
    ],
    device="The paper discusses a Syrebo glove program and does not name a model. The glove-and-console photograph is Figure 2 of that open-access report (CC BY 4.0), shown in the excerpt at the top. It is not a figure from a different review.",
    design="A single case report, not a randomized trial. After the person was medically stable, clinicians delivered neurophysiotherapy that included the Syrebo glove program.",
    sample="A 66-year-old woman with bilateral MCA-territory infarction. The report records observations and functional change. It does not provide between-group statistics.",
    result="The value of the report is the course of care, not a rate of improvement. It shows how a soft glove was placed inside rehabilitation for one person with a severe infarct, under professional supervision. A change in a single case is not a promised degree of recovery.",
    sig=[
        "Among a column that is mostly randomized trials, one case report is here to show how a program was used for a person. It fills a narrative gap. It does not raise the level of evidence.",
        "One case cannot estimate how often adverse events occur, and it cannot say whether the acute, subacute, or chronic phase is the better fit. Those questions stay with controlled studies.",
    ],
    limit="Single case. Not a general effect. Functional change cannot be assigned to the glove alone.",
)

add(
    8, "en",
    title="Upper-limb impairment after stroke: a 60-person randomized study of innovative mirror therapy",
    desc="New Medicine, 2024: 60 people, four weeks. The paper reports larger gains on FMA-UE, FMA-WH, and the modified Barthel Index with innovative mirror therapy than with conventional mirror therapy.",
    lead="Conventional mirror therapy uses a mirror to suggest that the affected hand is moving. The innovative version asks a robotic glove to carry the affected hand through the same action the mirror shows, so seeing and doing share the session. In 2024 New Medicine published a randomized study by Chen and colleagues that compared the two versions in 60 people over four weeks. The paper reports larger gains for innovative mirror therapy on upper-limb movement, wrist-hand movement, and daily activities.",
    bg=[
        "Mirror therapy has a known limit: if the affected hand does not move, the visual suggestion has no paired motor input. Connecting assisted flexion and extension to the mirror task is an attempt to have the affected side actually complete a movement inside a range the therapist sets.",
        "Whether that change shows up on scores has to be tested against conventional mirror therapy, not against doing nothing. Sixty people, split evenly, is a preliminary randomized size.",
    ],
    device="A training image on the journal page shows a Yisheng mark. The column maps that mark to the SY-HR08E in official materials and shows a product photograph with screen, console, and glove. The mapping is an identification note, not a model claim printed as a trial registration.",
    design="Random-number allocation. Innovative mirror therapy, combining a mirror task with a robotic glove, was compared with conventional mirror therapy. Outcomes included FMA-UE, FMA-WH, and the modified Barthel Index.",
    sample="Sixty people with upper-limb impairment after stroke, 30 in each group, for four weeks.",
    result="The paper reports greater improvement for innovative mirror therapy on FMA-UE, FMA-WH, and the modified Barthel Index. That is the study’s between-group description. Means and P values are not recalculated on this page; where the journal page is still being checked, those figures stay with the paper.",
    sig=[
        "The question is whether adding an assisted movement that matches the mirror changes scores relative to the mirror alone. Sixty people provide a preliminary contrast, not a home-program proof.",
        "Linking the journal image to the SY-HR08E only helps a reader recognize the device. Whether the score difference is stable waits on an independent check of the full numbers.",
    ],
    limit="Thirty people per group. Differences follow the paper. Means and P values are not recomputed here. The model link is a check between the journal figure and official materials.",
)

add(
    9, "en",
    title="Left hemiparesis after MCA infarction: one record of faradic stimulation plus a robotic hand",
    desc="IJPRCP case report: a 60-year-old man with left hemiparesis started faradic stimulation plus the Syrebo C12 about three months after stroke, five times a week for four weeks. One combined case is not assigned to either component.",
    lead="A hemiparetic hand is sometimes given two inputs at once: electrical stimulation aimed at the muscle, and a robotic hand to open and close the fingers. A 2025 case report in the International Journal of Physiotherapy Research and Clinical Practice records four weeks of faradic stimulation plus a Syrebo C12 for one man with left hemiparesis. It is a record of a combined plan, not an efficacy trial of either piece.",
    bg=[
        "Months after stroke, hand change is usually slower, and clinicians sometimes add stimulation or external assistance to ordinary practice. Once both are used, a before-after change cannot be given cleanly to either one.",
        "The report is still useful. It states when the plan started, how often it ran, and which device was in the room. It does not give a rate, and it does not give a difference against a control.",
    ],
    device="The robotic device in the report is the Syrebo C12. The photograph is a crop from the official C12 product page so the controller and glove can be recognized. It does not add specifications the paper omitted.",
    design="A single combined intervention: faradic stimulation together with Syrebo C12 robotic hand practice. There is no parallel control group.",
    sample="A 60-year-old man with left hemiparesis. The plan began 3 months and 2 weeks after stroke, five times a week, for four weeks.",
    result="This page does not reprint functional scores that have not been checked against the paper for the column. What is clear is the arrangement: stimulation and robotic practice were used together, so a change cannot be written as the effect of the C12 alone or of stimulation alone.",
    sig=[
        "The record adds a concrete schedule: about three months after stroke, five sessions a week, two modalities together. It does not raise the level of evidence.",
        "One left-hemiparetic case after MCA infarction does not stand in for other lesions or other times after onset.",
    ],
    limit="Single combined case. Change is not assigned to the C12 or to stimulation, and it is not a general effect.",
)

add(
    10, "en",
    title="A soft wrist-hand orthosis: design and preliminary evaluation in Wearable Technologies",
    desc="Ledoux and Barth report their own 3D-printed wrist-hand orthosis in Wearable Technologies. This note stays with that design paper. It does not rank commercial products and it is not an efficacy trial.",
    lead="In 2024 Wearable Technologies, from Cambridge University Press, published a design paper by Ledoux and Barth at Vanderbilt University. The device they built and preliminarily evaluated is their own 3D-printed wrist-hand grasping orthosis. The paper mentions commercial soft structures while discussing wearable hands. This column does not turn that discussion into a ranking, and it does not treat the paper as efficacy evidence for Syrebo.",
    bg=[
        "A hand device that leaves the therapy room has to answer weight, profile, and whether a person can put it on. Design papers usually state those constraints and then describe a prototype. They do not first report a multicenter functional trial. Reading a design paper as an efficacy paper invents clinical endpoints that were not measured.",
        "A soft structure and a rigid exoskeleton answer different engineering problems. Softness is one way to reduce profile. Talking about functional change still requires a human study of its own.",
    ],
    device="The excerpt at the top is the open-access first page (CC BY 4.0), not a comparison table. The product photograph shows a Syrebo clinical glove system. It is not a figure from this experiment.",
    design="Design, modeling, and preliminary evaluation of the authors’ own 3D-printed orthosis. The paper is not a randomized trial of Syrebo and not an efficacy comparison among marketed devices.",
    sample="The human portion is a preliminary look at the authors’ prototype. Its size and tasks are those of the paper. It is not restated here as a Syrebo cohort.",
    result="This page does not quote commercial adjectives and does not list other brands. What remains is that the paper is an open-access design study about a soft, wearable structure. The authors’ word “presumably” marks comfort as something they did not treat as a measured endpoint.",
    sig=[
        "The paper is in the column so a design study stays distinct from an efficacy trial. Whether a soft structure makes a device easier to wear in daily life is a wearing study and a functional study, separately.",
        "Open access lets a reader check the wording. The point of checking is to keep a presumption from becoming a conclusion, not to elect a lightest product.",
    ],
    limit="Not an efficacy trial of Syrebo, and not a product ranking. The source hedges comfort with “presumably.” The first-page crop does not include a comparison table.",
)

add(
    11, "en",
    title="Finger robots intended for home use: a development note in the Journal of the Robotics Society of Japan",
    desc="A 2023 article in the Journal of the Robotics Society of Japan discusses home-use finger robots for hemiparesis and names Syrebo among the few commercialized examples. It is not a clinical trial.",
    lead="Home hand rehabilitation has been discussed for years. Commercialized examples in the society literature are still few. In 2023 the Journal of the Robotics Society of Japan published an article by Furudate and colleagues on a finger-rehabilitation robot intended for home use after hemiparesis, and on developing it with clinicians. The authors note that commercialized home-use cases remain rare, and they name the Syrebo hand glove as one such case. The article is a development and collaboration note, not an efficacy trial.",
    bg=[
        "Between the ward and the home sit donning, safety limits, and use when no therapist is in the room. Engineering papers put those constraints inside the work with clinicians. Being named means the authors chose this product as an example. It does not mean the society ran a controlled study.",
        "“Few have been commercialized” is also a limit. Reading it as “home rehabilitation is already generally available” turns an example into an epidemiologic claim.",
    ],
    device="The article does not print a glove photograph. The glove-and-console image in this column is Figure 2 of the 2024 Cureus case report by Sharma and colleagues (CC BY 4.0). The caption says so. It is not the original figure of the Japanese society paper.",
    design="A society-journal development article about finger robots for home use and about working with clinicians. There is no randomization and no between-group functional comparison.",
    sample="A clinical sample size does not apply. The article discusses a path to a product, not outcomes in a cohort.",
    result="The statement, as used here, is that commercialized finger robots aimed at the home are still few, and that Syrebo is one example the authors name. The column keeps that scope. It is not rewritten as efficacy, as a market rank, or as a promise that training at home will be completed.",
    sig=[
        "The note’s value is that home use is treated as an engineering problem defined with clinicians. A commercialized example shows that one device moved from prototype to product.",
        "Whether it can be used safely and repeatedly at home still depends on indication, supervision, and separate clinical studies. The society paper does not provide those data.",
    ],
    limit="Not a clinical trial of Syrebo. The source stresses that commercialized examples remain few. The photograph is from a different open-access case report.",
)


def _load_locales() -> None:
    from column_i18n_a import register as reg_a
    from column_i18n_b import register as reg_b
    from column_i18n_c import register as reg_c
    from column_i18n_d import register as reg_d
    from column_i18n_e import register as reg_e
    from column_i18n_f import register as reg_f
    from column_i18n_g import register as reg_g

    for reg in (reg_a, reg_b, reg_c, reg_d, reg_e, reg_f, reg_g):
        reg(add)


_load_locales()
