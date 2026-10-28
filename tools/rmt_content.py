# -*- coding: utf-8 -*-
"""Verified study facts and column prose for issue 12 and supplements 01–08.

Numbers are taken from the public RMT evidence series, which cites the papers.
Fields that the source left unverified stay unverified here.
"""

STUDIES = []


def add(item):
    STUDIES.append(item)
    return item


add({
    "slug": "day12",
    "photo": "hr06",
    "figure": "qian",
    "pending": False,
    "doi": "10.3389/fneur.2025.1602896",
    "trial": "ChiCTR2200057613",
    "zh_index": "第 12 期 · 亚急性期上肢功能：SY-HR06 与镜像疗法的三组随机先导研究",
    "en_index": "Subacute upper-limb scores: a three-arm pilot of the SY-HR06 and mirror therapy",
    "root_en": "Robot glove plus mirror therapy: how to read the SY-HR06 three-arm pilot",
    "poster": {
        "zh": {
            "chip": "第 12 期",
            "cat": "临床先导研究 · 2025",
            "title": "亚急性期上肢功能：手套与镜像的三组先导研究",
            "sub": "论文设备记为羿生 SY-HR06。干预四周，没有随访。",
            "caption": "SYREBO品牌场景图（HR06E）｜非论文SY-HR06设备照片",
            "design_label": "研究设计",
            "key_label": "核心解读",
            "stats": [("3组", "镜像、手套、联合"), ("4周", "每周5次，每次30分钟"), ("52例", "完成分析，66例随机")],
            "result": {
                "type": "bars",
                "labels": ["联合组", "镜像组"],
                "values": [37.61, 23.63],
                "texts": ["37.61±11.09", "23.63±12.69"],
                "axis": "上肢运动评分（FMA-UE），治疗后",
            },
            "note": "解读提示　论文报告联合组这一项评分高于镜像组。联合组同时做了两件事，不能写成手套单独起效。",
            "boundary": "研究边界　先导研究，每组完成分析16至18例。只做4周，没有随访。14例退出未进入分析。",
            "source": [
                "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D",
                "Frontiers in Neurology, 2025;16:1602896",
                "DOI: 10.3389/fneur.2025.1602896",
            ],
            "footer": "syrebo.com · Syrebo 临床研究专栏。基于已发表研究整理，仅供康复科普参考，不构成医疗建议。",
        },
        "en": {
            "chip": "Issue 12",
            "cat": "Clinical pilot · 2025",
            "title": "Subacute upper limb: a three-arm pilot of glove and mirror therapy",
            "sub": "The paper names the device as the Yisheng SY-HR06. Four weeks, no follow-up.",
            "caption": "SYREBO brand scene (HR06E). Not a photograph of the SY-HR06 used in the study.",
            "design_label": "Study design",
            "key_label": "Main reading",
            "stats": [("3 arms", "Mirror, glove, both"), ("4 weeks", "Five 30-minute sessions a week"), ("52", "Analyzed; 66 randomized")],
            "result": {
                "type": "bars",
                "labels": ["Combined", "Mirror"],
                "values": [37.61, 23.63],
                "texts": ["37.61±11.09", "23.63±12.69"],
                "axis": "Post-treatment FMA-UE. The paper reports p=0.006.",
            },
            "note": "Reading note. The paper reports a higher score in the combined arm than in mirror therapy. That arm received both treatments, so the difference is not evidence that the glove alone did the work.",
            "boundary": "Limits. Pilot scale, 16 to 18 people analyzed per arm. Four weeks and no follow-up. Fourteen withdrawals were left out of the analysis.",
            "source": [
                "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D",
                "Frontiers in Neurology, 2025;16:1602896",
                "DOI: 10.3389/fneur.2025.1602896",
            ],
            "footer": "syrebo.com · Syrebo Clinical Research Column. Compiled from published studies. Not medical advice.",
        },
    },
    "zh": {
        "title": "亚急性期上肢功能：SY-HR06 与镜像疗法的三组随机先导研究",
        "desc": "武汉武昌医院的三组随机先导研究：66 例随机、52 例完成分析，比较镜像治疗、SY-HR06 与二者联合。论文报告联合组治疗后上肢运动评分高于镜像组。4 周，无随访。",
        "keywords": "亚急性期康复、镜像疗法、机器人手套、随机先导研究、上肢运动功能",
        "issue": "第 12 期",
        "h1": "亚急性期上肢功能：SY-HR06 与镜像疗法的三组随机先导研究",
        "paper_title": "Combination of robot-assisted glove and mirror therapy improves upper limb motor function in subacute stroke patients: a randomized controlled pilot study",
        "paper_authors": "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D",
        "paper_venue": "Frontiers in Neurology, 2025;16:1602896",
        "paper_meta": "DOI: 10.3389/fneur.2025.1602896 · ChiCTR2200057613",
        "lead": [
            "这项研究不是把“用手套”和“不用手套”放在一起比。武汉武昌医院的团队把镜像治疗、机器人手套、以及两者一起做，放进三个平行组。论文记录的设备是羿生 SY-HR06。完成分析的人里，联合组治疗后的上肢运动评分高于镜像组。联合组同时接受两种训练，这个差别不能写成手套单独带来的结果。干预只有 4 周，没有随访。",
        ],
        "background": [
            "上肢和手的练习，常常要在看着动作和自己动手之间来回切换。镜像治疗用健侧的影像来组织注意；气动手套把患手的开合重复做出来。两种做法可以分开用，也可以放在同一次训练里。分开用和一起用，不是同一件事。",
            "如果只报告“加了设备以后分数变了”，读者会把联合方案的变化算到设备上。三组设计的作用，是把镜像、手套、联合三条路径同时摆出来。它仍然是先导研究，回答的是这条路径值不值得继续做更大的试验，不是已经证明长期结果。",
        ],
        "overview": [
            "论文中的设备写的是羿生 SY-HR06，气动软体手套，戴在患侧手，做握紧和放松。三组之外都还有常规康复。结局包括上肢 Fugl-Meyer 评分（FMA-UE）、Brunnstrom 上肢与手分级、香港版上肢功能测试（FTHUE-HK）和功能独立性评定（FIM）。评估由不知晓分组的认证作业治疗师完成。专栏配图是品牌场景，不是这篇论文里的设备照片。",
        ],
        "design": "单盲、随机、对照的先导研究，三个平行组。镜像组看着健侧上肢的镜像做抓握。手套组用 SY-HR06 做开合。联合组把手套训练和镜像治疗放在同一次里。研究在武汉武昌医院进行，注册号 ChiCTR2200057613。",
        "sample": "100 人接受筛查，66 人随机分组。干预期间 14 人退出，并被排除出分析。进入分析的是镜像组 16 人、手套组 18 人、联合组 18 人，合计 52 人。准确的写法是“66 人随机、52 人完成分析”，不是“52 人随机”。每周 5 次，每次 30 分钟，共 4 周。",
        "results": "论文报告，多项指标在三组治疗后都较各自的基线有变化。组间比较里，联合组治疗后的上肢 Fugl-Meyer 评分为 37.61±11.09，镜像组为 23.63±12.69，论文给出的组间 p=0.006。联合组治疗后 Brunnstrom 上肢分级为 4.06±0.87，手分级为 4.67±1.24，功能独立性评定为 94.17±9.49；摘要写这些指标优于镜像组。摘要里最清楚的比较是联合组对镜像组，并不是每一项都证明联合组优于单独使用手套的那一组。",
        "meaning": [
            "这篇论文把看影像和患手重复放在同一次训练里，并用三个组把“一起做”和“分开做”同时留下。可以讨论的是，在常规康复之上，治疗师如何排列镜像、手套或两者同做。",
            "不能把联合组的分数写成这一件手套的效果，也不能写成已经看到长期维持。作者还提到联合组右侧半球病变的比例较高，各组实际抓握次数也没有比较。这些都会影响怎么读这个 p 值。",
        ],
        "limits": "先导研究，每组完成分析 16 至 18 人。只做 4 周，没有随访。14 人退出后未进入分析。病变侧的分布并不整齐，主动参与的次数没有量化。p 值是论文对这一项组间比较的报告。",
        "source": "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D. Combination of robot-assisted glove and mirror therapy improves upper limb motor function in subacute stroke patients: a randomized controlled pilot study. Frontiers in Neurology, 2025;16:1602896.",
        "photo_alt": "品牌场景中的手功能康复设备，不是 Qian 2025 论文中的 SY-HR06 照片",
        "photo_cap": "SYREBO品牌场景图（HR06E）｜非论文SY-HR06设备照片",
        "fig_alt": "Qian 等 2025 年论文图 1：镜像治疗、机器人手套训练、二者联合",
        "fig_cap": "原文图 1：三种干预。Qian 等，Frontiers in Neurology，2025，CC BY 4.0。",
    },
    "en": {
        "title": "Subacute upper-limb scores: a three-arm pilot of the SY-HR06 and mirror therapy",
        "desc": "A three-arm randomized pilot at Wuhan Wuchang Hospital: 66 people randomized and 52 analyzed, comparing mirror therapy, the SY-HR06, and both together. The paper reports a higher post-treatment upper-limb motor score in the combined arm than in mirror therapy. Four weeks, no follow-up.",
        "keywords": "subacute rehabilitation, mirror therapy, robotic glove, randomized pilot, upper-limb motor score",
        "issue": "Issue 12",
        "h1": "Subacute upper-limb scores: a three-arm pilot of the SY-HR06 and mirror therapy",
        "paper_title": "Combination of robot-assisted glove and mirror therapy improves upper limb motor function in subacute stroke patients: a randomized controlled pilot study",
        "paper_authors": "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D",
        "paper_venue": "Frontiers in Neurology, 2025;16:1602896",
        "paper_meta": "DOI: 10.3389/fneur.2025.1602896 · ChiCTR2200057613",
        "lead": [
            "This study did not compare a glove with no glove. At Wuhan Wuchang Hospital, the team placed mirror therapy, a robotic glove, and both together into three parallel arms. The paper names the device as the Yisheng SY-HR06. Among people who completed analysis, the combined arm had a higher post-treatment upper-limb motor score than the mirror-therapy arm. That arm received two treatments at once, so the difference cannot be written as the glove alone. Training lasted four weeks, with no follow-up.",
        ],
        "background": [
            "Upper-limb practice moves between watching a movement and making one. Mirror therapy uses the unaffected limb’s reflection to organize attention. A pneumatic glove repeats opening and closing of the affected hand. The two can be scheduled apart or in the same session. Those are different pathways.",
            "A sentence that only says the score changed after a device was added will be read as a device effect. The three-arm design puts mirror therapy, the glove, and the combination on the same page. It is still a pilot. It asks whether a larger trial is worth doing. It does not show that a result lasts.",
        ],
        "overview": [
            "The paper records a Yisheng SY-HR06 pneumatic soft glove on the affected hand for clench-and-relax practice. All three arms also received usual rehabilitation. Outcomes included FMA-UE, Brunnstrom stages for the upper limb and the hand, the FTHUE-HK, and the Functional Independence Measure. A certified occupational therapist who did not know the assignment did the assessments. The photograph in this column is a brand scene, not a photograph of the study device.",
        ],
        "design": "Single-blind randomized controlled pilot with three parallel arms. The mirror arm practiced grasp while watching the unaffected upper limb. The glove arm used the SY-HR06 for open-and-close practice. The combined arm did glove practice and mirror therapy in the same session. The site was Wuhan Wuchang Hospital. Registration: ChiCTR2200057613.",
        "sample": "One hundred people were screened and 66 were randomized. Fourteen left during the intervention and were excluded from the analysis. The analyzed sample was 16 in mirror therapy, 18 in the glove arm, and 18 in the combined arm: 52 in total. The accurate count is 66 randomized and 52 analyzed, not 52 randomized. Sessions were 30 minutes, five times a week, for four weeks.",
        "results": "The paper reports that several scores changed from each arm’s own baseline. For the between-arm comparison, post-treatment FMA-UE was 37.61±11.09 in the combined arm and 23.63±12.69 in the mirror arm; the paper gives p=0.006 for that comparison. In the combined arm, post-treatment Brunnstrom stage was 4.06±0.87 for the upper limb and 4.67±1.24 for the hand, and the Functional Independence Measure was 94.17±9.49. The abstract reports these as higher than in the mirror arm. The clearest abstract comparison is combined versus mirror, not a claim that the combined arm beat the glove-only arm on every outcome.",
        "meaning": [
            "The study put visual feedback and repeated movement of the affected hand in one session, and it kept the separate pathways in the same design. What can be discussed is how a therapist orders mirror therapy, glove practice, or both, on top of usual rehabilitation.",
            "The combined score cannot be rewritten as the effect of the glove by itself, and four weeks cannot be rewritten as a lasting result. The authors also note a higher share of right-hemisphere lesions in the combined arm, and grasp counts were not compared. Both belong next to the p value.",
        ],
        "limits": "Pilot scale, with 16 to 18 people analyzed per arm. Four weeks and no follow-up. Fourteen withdrawals were excluded from the analysis. Lesion side was uneven, and active repetitions were not counted. The p value is the paper’s report for that one comparison.",
        "source": "Qian J, Liang C, Liu R, Yu J, Yang T, Bai D. Combination of robot-assisted glove and mirror therapy improves upper limb motor function in subacute stroke patients: a randomized controlled pilot study. Frontiers in Neurology, 2025;16:1602896.",
        "photo_alt": "Brand scene of a hand-rehabilitation device, not a photograph of the SY-HR06 in Qian 2025",
        "photo_cap": "SYREBO brand scene (HR06E). Not a photograph of the SY-HR06 used in the study.",
        "fig_alt": "Figure 1 of Qian et al. 2025: mirror therapy, robotic glove training, and the combination",
        "fig_cap": "Original Figure 1, the three interventions. Qian et al., Frontiers in Neurology, 2025, CC BY 4.0.",
    },
})

add({
    "slug": "sup01",
    "photo": "hr08",
    "figure": None,
    "pending": True,
    "doi": "10.1007/978-981-99-6483-3_21",
    "trial": None,
    "zh_index": "补充研究 01 · 三周机器人手治疗：手功能变化有限，脑电与肌电的耦合有信号",
    "en_index": "Supplement 01 · Three weeks of robotic hand therapy: limited hand-function change, with an EEG–EMG coupling signal",
    "root_en": "Three weeks of robotic hand therapy: limited hand scores, a coupling signal on EEG and EMG",
    "poster": {
        "zh": {
            "chip": "补充研究 01",
            "cat": "临床与神经生理 · 2023",
            "title": "三周机器人手治疗：手功能与脑电信号要分开读",
            "sub": "论文设备为司羿 SY-HR08P。全文未取得，不补写样本量。",
            "caption": "SYREBO品牌场景图（HR08E）｜非论文SY-HR08P设备照片",
            "design_label": "研究设计",
            "key_label": "核心解读",
            "stats": [("3周", "机器人手治疗"), ("脑电＋肌电", "脑活动与神经肌肉耦合"), ("3种", "运动模式")],
            "result": {
                "type": "chips",
                "headline": "主动模式之后，β与γ频段的脑电—肌电相干性增加",
                "chips": ["β频段", "γ频段", "相干性升高"],
            },
            "note": "解读提示　摘要报告手功能改善有限，同时报告整体脑活动有变化。机制信号不能代替功能结局。",
            "boundary": "研究边界　全文未取得，样本量、对照和效应值不在这里补写。相干性不是日常生活能力。",
            "source": [
                "Xinhang Li, Minjun Zheng, Jinbiao Liu, et al.",
                "Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267",
                "DOI: 10.1007/978-981-99-6483-3_21",
            ],
            "footer": "syrebo.com · Syrebo 临床研究专栏。基于已发表研究整理，仅供康复科普参考，不构成医疗建议。",
        },
        "en": {
            "chip": "Supplement 01",
            "cat": "Clinical and neurophysiology · 2023",
            "title": "Three weeks of robotic hand therapy: read the hand score apart from the signals",
            "sub": "The abstract names the SY-HR08P. The full text was not available, so sample size is not filled in.",
            "caption": "SYREBO brand scene (HR08E). Not a photograph of the SY-HR08P in the paper.",
            "design_label": "Study design",
            "key_label": "Main reading",
            "stats": [("3 weeks", "Robotic hand therapy"), ("EEG + EMG", "Brain activity and coupling"), ("3 modes", "Movement conditions")],
            "result": {
                "type": "chips",
                "headline": "After the active mode, beta and gamma EEG–EMG coherence increased",
                "chips": ["Beta band", "Gamma band", "Coherence up"],
            },
            "note": "Reading note. The abstract reports limited change in hand function and a change in overall brain activity. A coupling signal is not a functional outcome.",
            "boundary": "Limits. Full text was not available. Sample size, control condition, and effect sizes are not supplied here. Coherence is not an activity of daily life.",
            "source": [
                "Xinhang Li, Minjun Zheng, Jinbiao Liu, et al.",
                "Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267",
                "DOI: 10.1007/978-981-99-6483-3_21",
            ],
            "footer": "syrebo.com · Syrebo Clinical Research Column. Compiled from published studies. Not medical advice.",
        },
    },
    "zh": {
        "title": "三周机器人手治疗：手功能变化有限，脑电与肌电的耦合有信号",
        "desc": "ICIRA 2023 会议论文摘要：SY-HR08P，三周，三种运动模式，同时记录脑电和肌电。摘要报告手功能改善有限；主动模式后 β 与 γ 频段相干性增加。全文未取得。",
        "keywords": "机器人手治疗、脑电图、肌电图、神经肌肉耦合、会议论文",
        "issue": "补充研究 01",
        "h1": "三周机器人手治疗：手功能变化有限，脑电与肌电的耦合有信号",
        "paper_title": "The Impact of Three-Week Passive Robotic Hand Therapy on Stroke Patients",
        "paper_authors": "Xinhang Li, Minjun Zheng, Jinbiao Liu, Li Zhang, Lizi Jiang, Shiwei Zheng, Linqing Feng, Tao Tang, Lei Ling, Xiangming Ye, Yina Wei",
        "paper_venue": "Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267",
        "paper_meta": "DOI: 10.1007/978-981-99-6483-3_21",
        "lead": [
            "这篇会议论文更适合当成“训练加上神经生理记录”，而不是一项已经证明手功能疗效的对照试验。摘要写到手功能的改善有限，同时又写到整体脑活动有变化。主动模式之后，β 和 γ 频段的脑电—肌电相干性增加。功能分数和生理信号要分成两句来说。",
        ],
        "background": [
            "手功能量表回答的是动作和分数。脑电和肌电回答的是记录当时的电活动，以及脑与肌肉之间有没有更同步。两套结果可以来自同一次训练，却不能互相替代。",
            "会议摘要通常短于期刊全文。样本量、有没有对照、退出了多少人，摘要里没有写清的，不能靠产品手册补上。",
        ],
        "overview": [
            "摘要写明设备是上海司羿智能科技有限公司的 SY-HR08P。研究用脑电图和肌电图观察三周机器人手治疗，并用源定位看左右感觉运动区。专栏配图是另一台设备的品牌场景，图注已标明不是论文中的 SY-HR08P。",
        ],
        "design": "比较三种运动模式的机器人手治疗，同时记录脑电和肌电。这是会议论文摘要能够确认的设计范围。摘要没有提供可以改写成随机对照试验的分组细节。",
        "sample": "治疗周期是 3 周。完整全文尚未取得，样本量、各组人数和退出情况不在本页补写。",
        "results": "摘要报告手功能改善有限，不应改写成显著的功能恢复。摘要同时报告整体脑活动有改善，但三种模式之间，感觉运动区的变化没有显著差异。主动模式之后，β 与 γ 频段的脑电—肌电相干性增加。作者把这解释为神经驱动肌肉的效率信号。它仍是生理指标，不是日常生活能力的随访结果。",
        "meaning": [
            "这篇摘要把训练模式和脑活动、神经肌肉耦合放在一起，提醒读机器人手训练时不要只看一次量表。机制信号要单独成句，并且标明全文还没有核对效应值。",
        ],
        "limits": "证据范围停在出版社摘要和书目。样本量、对照设置和精确统计量未核实，所以不写。手功能改善有限，不能改写成疗效已经确立。相干性不等于自理能力。",
        "source": "Xinhang Li, Minjun Zheng, Jinbiao Liu, Li Zhang, Lizi Jiang, Shiwei Zheng, Linqing Feng, Tao Tang, Lei Ling, Xiangming Ye, Yina Wei. The Impact of Three-Week Passive Robotic Hand Therapy on Stroke Patients. Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267.",
        "photo_alt": "品牌场景中的手功能康复设备，不是 Li 2023 论文中的 SY-HR08P",
        "photo_cap": "SYREBO品牌场景图（HR08E）｜非论文SY-HR08P设备照片",
    },
    "en": {
        "title": "Three weeks of robotic hand therapy: limited hand-function change, with an EEG–EMG coupling signal",
        "desc": "An ICIRA 2023 conference abstract: the SY-HR08P, three weeks, three movement modes, with EEG and EMG. The abstract reports limited hand-function change. Beta and gamma coherence rose after the active mode. The full text was not available.",
        "keywords": "robotic hand therapy, electroencephalography, electromyography, neuromuscular coupling, conference paper",
        "issue": "Supplement 01",
        "h1": "Three weeks of robotic hand therapy: limited hand-function change, with an EEG–EMG coupling signal",
        "paper_title": "The Impact of Three-Week Passive Robotic Hand Therapy on Stroke Patients",
        "paper_authors": "Xinhang Li, Minjun Zheng, Jinbiao Liu, Li Zhang, Lizi Jiang, Shiwei Zheng, Linqing Feng, Tao Tang, Lei Ling, Xiangming Ye, Yina Wei",
        "paper_venue": "Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267",
        "paper_meta": "DOI: 10.1007/978-981-99-6483-3_21",
        "lead": [
            "This conference paper reads as training plus a neurophysiology recording, not as a trial that has already established a hand-function effect. The abstract reports limited improvement in hand function and, separately, a change in overall brain activity. After the active mode, beta and gamma EEG–EMG coherence increased. The score and the signal need two sentences.",
        ],
        "background": [
            "A hand scale answers a question about movement and points. EEG and EMG answer a question about electrical activity at the time of recording, and about whether brain and muscle were more synchronous. The two can come from the same sessions and still not stand in for each other.",
            "A conference abstract is shorter than a journal article. Sample size, the presence of a control, and withdrawals, when the abstract does not state them, cannot be filled from a product sheet.",
        ],
        "overview": [
            "The abstract names the device as the SY-HR08P from Shanghai Siyi Intelligent Technology. The study used EEG and EMG across three weeks of robotic hand therapy and source localization over the sensorimotor areas. The photograph in this column is a brand scene of a different model. The caption says it is not the SY-HR08P in the paper.",
        ],
        "design": "Robotic hand therapy compared across three movement modes, with EEG and EMG. That is the design the abstract can support. The abstract does not give the allocation detail that would let this page call it a randomized controlled trial.",
        "sample": "The scheduled exposure is three weeks. The full paper was not available, so sample size, arm sizes, and withdrawals are not added on this page.",
        "results": "The abstract reports limited improvement in hand function. That should not be rewritten as a large functional recovery. It also reports a change in overall brain activity, without a significant difference among the three modes in the sensorimotor areas. After the active mode, beta and gamma EEG–EMG coherence increased. The authors read that as a signal of more efficient neural drive to muscle. It remains a physiological measure, not a follow-up of daily activity.",
        "meaning": [
            "The abstract ties a training mode to brain activity and to neuromuscular coupling. It is a reason to report more than one scale, and equally a reason to keep the mechanism sentence separate until effect sizes are checked in the full text.",
        ],
        "limits": "The checked source is the publisher abstract and the citation. Sample size, the control arrangement, and exact statistics were not verified, so they are not written. Limited hand-function change is not an established treatment effect. Coherence is not an activity of daily living.",
        "source": "Xinhang Li, Minjun Zheng, Jinbiao Liu, Li Zhang, Lizi Jiang, Shiwei Zheng, Linqing Feng, Tao Tang, Lei Ling, Xiangming Ye, Yina Wei. The Impact of Three-Week Passive Robotic Hand Therapy on Stroke Patients. Intelligent Robotics and Applications, ICIRA 2023, LNCS 14267.",
        "photo_alt": "Brand scene of a hand-rehabilitation device, not the SY-HR08P in Li 2023",
        "photo_cap": "SYREBO brand scene (HR08E). Not a photograph of the SY-HR08P in the paper.",
    },
})
