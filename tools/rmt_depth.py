# -*- coding: utf-8 -*-
"""Extra clinical context for the nine RMT posts.

Paragraphs explain how to read a published design. They do not add sample
sizes, p values, or effect sizes beyond the fields already checked.
"""

RELATED = {
    "day12": [
        ("day02.html", "第 02 期 · 软体手套与镜像疗法，并随访到 6 个月", "Issue 02 · Soft glove versus mirror therapy, with follow-up to 6 months"),
        ("day05.html", "第 05 期 · 早期亚急性期软体手套的单盲随机试点", "Issue 05 · Early-subacute soft-glove pilot"),
        ("sup02.html", "补充研究 02 · 两组都用了手套，组间差别来自多出来的干预", "Supplement 02 · Both arms used the glove; the gap is the added intervention"),
        ("sup03.html", "补充研究 03 · 在任务导向镜像之上比较有没有手套", "Supplement 03 · Task-oriented mirror therapy with or without a glove"),
    ],
    "sup01": [
        ("day05.html", "第 05 期 · 同一早期窗口里，用手功能量表回答可行性", "Issue 05 · Feasibility answered with hand scales in a similar early window"),
        ("sup05.html", "补充研究 05 · 当次脑激活，同样不是疗程后的功能分数", "Supplement 05 · Activation during a task, not a score after a course of care"),
    ],
    "sup02": [
        ("day12.html", "第 12 期 · 镜像、手套、联合三条路径分开记录", "Issue 12 · Mirror, glove, and both, kept as separate paths"),
        ("day02.html", "第 02 期 · 手套与镜像分开比较，并看到随访", "Issue 02 · Glove and mirror compared apart, with follow-up"),
    ],
    "sup03": [
        ("day12.html", "第 12 期 · 三组设计把联合和单做同时留下", "Issue 12 · A three-arm design keeps the combination and the single paths"),
        ("day02.html", "第 02 期 · 手套与镜像的对照，带 6 个月随访", "Issue 02 · Glove versus mirror, with a 6-month follow-up"),
    ],
    "sup04": [
        ("sup02.html", "补充研究 02 · 另一种叠加上常规路径的组合方案", "Supplement 02 · Another program stacked on top of a shared path"),
        ("day01.html", "第 01 期 · 在常规治疗之外增加手部训练的随机对照", "Issue 01 · Hand training added beside usual care"),
    ],
    "sup05": [
        ("sup01.html", "补充研究 01 · 三周训练里的脑电与肌电，功能变化有限", "Supplement 01 · EEG and EMG across three weeks, with limited hand-score change"),
        ("day05.html", "第 05 期 · 用完成情况和手功能量表回答早期可行性", "Issue 05 · Early feasibility read from completion and hand scales"),
    ],
    "sup06": [
        ("sup07.html", "补充研究 07 · 另一项台架工程：气源，不是手功能", "Supplement 07 · Another bench study: a gas source, not hand function"),
        ("sup05.html", "补充研究 05 · 任务中的脑激活，同样不是疗效试验", "Supplement 05 · Task activation, also not an efficacy trial"),
    ],
    "sup07": [
        ("sup06.html", "补充研究 06 · 健康人身上的接口可行性，不是疗程结局", "Supplement 06 · Interface feasibility in healthy adults, not a treatment outcome"),
    ],
    "sup08": [
        ("sup05.html", "补充研究 05 · 品牌或型号未核对时，不计入已确认的设备实验", "Supplement 05 · Unchecked brand or model is not counted as a confirmed device experiment"),
        ("day11.html", "第 11 期 · 学会综述里的产品记述，和单次实验不是同一件事", "Issue 11 · A society note that names a product is not the same as one experiment"),
    ],
}

EXTRA = {
    "day12": {
        "zh": {
            "background": [
                "拿杯子、扣纽扣、握笔，靠的是手指分开活动，步行往往更早回来。亚急性期神经仍在变化，量表上的差别可能混有自发恢复。治疗师读先导研究时，先核对它比较的是哪几条训练路径、评估的人知不知道分组、观察停在第几周。这篇论文把镜像、手套和两者同做放在同一张设计里，就是为了避免把联合方案的分数算到其中一件事情上。",
            ],
            "overview": [
                "干预可以分成三句。镜像组看着健侧上肢在镜中的影像做抓握。手套组把论文所记的羿生 SY-HR06 戴在患侧，做握紧和放松。联合组在同一次训练里安排手套和镜像。三组之外都保留常规康复。每次 30 分钟，每周 5 次，共 4 周。",
                "结局用中文名称来读：上肢运动损伤看上肢 Fugl-Meyer 评定（文献缩写 FMA-UE）；上肢和手的恢复阶段看 Brunnstrom 分期；上肢在功能任务中的表现看香港版上肢功能测试（文献缩写 FTHUE-HK）；生活活动里的独立程度看功能独立性评定（文献缩写 FIM）。评分由不知晓分组的认证作业治疗师完成。",
            ],
            "meaning": [
                "排程时可以讨论的是：镜像和患手重复开合写在同一节，还是分成两节，应当作为不同方案留下记录。记录里写清路径、周数、退出人数，以及评估者是否知道分组。联合组的分数不能单独放进某一件手套的说明，也不能写成已经看到长期维持。",
            ],
            "limits_add": "文中人数、分数和 p 值均引自该论文，不换算成提升比例，也不作为产品承诺。",
        },
        "en": {
            "background": [
                "Holding a cup, fastening a button, or keeping a pen depends on separated finger movement, and walking often returns sooner. In the subacute period the nervous system is still changing, so a score gap can include spontaneous recovery. A therapist reading a pilot checks which training paths were compared, whether the assessor knew the assignment, and the week the observation stopped. This paper places mirror therapy, the glove, and both together in one design so a combined score is not assigned to one of those pieces.",
            ],
            "overview": [
                "The intervention is three sentences. The mirror arm grasped while watching the unaffected upper limb. The glove arm wore the Yisheng SY-HR06 named in the paper on the affected hand and practiced clench and relax. The combined arm scheduled the glove and mirror therapy in the same session. All three arms kept usual rehabilitation. Sessions were 30 minutes, five times a week, for four weeks.",
                "Outcomes, by the names used in practice: motor impairment with the upper-limb Fugl-Meyer assessment (FMA-UE); recovery stage with Brunnstrom stages for the upper limb and the hand; functional tasks with the Hong Kong version of the Functional Test for the Hemiplegic Upper Extremity (FTHUE-HK); independence in daily activity with the Functional Independence Measure (FIM). A certified occupational therapist who did not know the assignment did the scoring.",
            ],
            "meaning": [
                "What can be discussed in scheduling is whether mirror therapy and repeated opening of the affected hand are written as one session or as two, and that those are different plans to record. The record names the path, the weeks, the withdrawals, and whether the assessor knew the assignment. The combined score does not go into a description of the glove alone, and four weeks is not a lasting result.",
            ],
            "limits_add": "Counts, scores, and the p value are quoted from the paper. They are not converted into a percentage gain and they are not a product claim.",
        },
    },
    "sup01": {
        "zh": {
            "background": [
                "病房里的手功能问题，首先是能不能完成抓握、松开和简单的日常动作。脑电和肌电回答的是记录当时脑与肌肉是否更同步。早期训练如果只报告一次生理曲线，治疗师无法知道手的分数有没有一起变化。这篇会议摘要把有限的手功能变化和相干性信号放在一起，正好要求这两句话分开写。",
            ],
            "overview": [
                "摘要能够确认的干预，是为期 3 周的机器人手治疗，设备写明为上海司羿智能科技有限公司的 SY-HR08P，并比较三种运动模式。记录手段是脑电图和肌电图，并用源定位观察左右感觉运动区。专栏照片是另一型号的品牌场景，图注写明不是论文中的 SY-HR08P。",
                "结局也要分成两层。功能层是手功能变化，摘要的用语是改善有限。生理层是整体脑活动，以及主动模式之后 β 与 γ 频段的脑电—肌电相干性。摘要没有给出可以改写成随机对照的分组人数。",
            ],
            "meaning": [
                "对临床阅读，这篇摘要的用处是提醒：训练模式可以同时留下量表和生理记录，但生理记录不能代替手功能或生活活动。在全文核对样本量、对照和效应值之前，它只适合作为机制线索，不适合写进产品说明。",
            ],
            "limits_add": "未在摘要中出现的人数和 p 值不补写。",
        },
        "en": {
            "background": [
                "On a ward, the hand question is whether grasp, release, and simple daily tasks can be completed. EEG and EMG ask whether brain and muscle were more synchronous at the moment of recording. If an early program reports only a physiological trace, a therapist still does not know whether the hand score moved with it. This conference abstract places limited hand-function change next to a coherence signal, which is why the two sentences stay apart.",
            ],
            "overview": [
                "What the abstract can confirm is three weeks of robotic hand therapy, on the SY-HR08P from Shanghai Siyi Intelligent Technology, compared across three movement modes. The recordings were EEG and EMG, with source localization over the sensorimotor areas. The photograph in this column is a brand scene of another model. The caption says it is not the SY-HR08P in the paper.",
                "Outcomes sit on two layers. The functional layer is hand function, which the abstract describes as limited improvement. The physiological layer is overall brain activity, and beta and gamma EEG–EMG coherence after the active mode. The abstract does not give the headcount that would turn this page into a randomized-trial summary.",
            ],
            "meaning": [
                "For clinical reading, the abstract is a reminder that a training mode can leave both a scale and a physiological trace, and that the trace does not stand in for hand function or daily activity. Until sample size, the control, and effect sizes are checked in the full text, it is a mechanism clue, not a passage for a product sheet.",
            ],
            "limits_add": "Headcounts and p values that are absent from the abstract are not supplied.",
        },
    },
    "sup02": {
        "zh": {
            "background": [
                "卒中后手和上肢的练习，常常同时包含药物、常规康复和某一种手部训练。如果两组都做了同一种手套训练，组间比较回答的是多出来的那一项，不是手套相对于完全不用手套。火针的频次和时长都不同于机器人训练，所以句子的主语必须是组合。",
            ],
            "overview": [
                "对照路径：常规药物和康复，加上羿生 SY-HR03Y。健侧数据手套采集动作并带动患侧，先做屈伸，再做抓球；机器人训练每天 1 次、每周 5 次，共 4 周。观察路径在同一套安排上增加火针，每次约 5 分钟、每周 3 次，共 4 周。",
                "结局的中文名称包括：手部运动评分（手部 Fugl-Meyer 评定）、屈伸方向的峰力矩、平均功率、总功、均方根值、协同收缩率，以及生活活动的改良 Barthel 指数。配图不是论文中的 SY-HR03Y。",
            ],
            "meaning": [
                "康复科如果把手套镜像训练和另一种疗法排在同一周，记录时应写明两组是否都使用了手套。本文能支持的说法是：在都使用 SY-HR03Y 的前提下，加火针的那一组在文中若干指标上更高。它不能支持把组间差别写成手套单独的效果，也没有随访来说明分数是否留下。",
            ],
            "limits_add": "数字引自该文，不写成产品提升比例。",
        },
        "en": {
            "background": [
                "Practice for the hand and upper limb after stroke often includes medication, usual rehabilitation, and one hand program at the same time. When both arms already do the same glove training, the between-arm comparison answers what the extra piece adds. It does not answer the glove against a program that never uses one. Fire needle has its own visits and minutes, so the subject of the sentence is the combination.",
            ],
            "overview": [
                "The shared path was usual medication and rehabilitation plus the Yisheng SY-HR03Y. A data glove on the unaffected side drove the affected side, flexion and extension first, then ball grasp, once a day, five days a week, for four weeks. The observation path added fire needle on that same plan, about five minutes a session, three times a week, for four weeks.",
                "Outcomes by their clinical names included the hand motor score (hand Fugl-Meyer), peak torque in flexion and extension, average power, total work, root-mean-square, the co-contraction ratio, and the modified Barthel index for daily activity. The photograph is not the SY-HR03Y in the paper.",
            ],
            "meaning": [
                "If a service schedules glove mirror training and another therapy in the same weeks, the record should say whether both arms used the glove. What this paper can support is that, with the SY-HR03Y in both arms, the arm that added fire needle was higher on several measures the paper reports. It cannot support writing that gap as the glove alone, and there is no follow-up to show whether the scores remained.",
            ],
            "limits_add": "The figures are quoted from the paper and are not rewritten as a product percentage.",
        },
    },
    "sup03": {
        "zh": {
            "background": [
                "任务导向训练把练习放进接近日常的动作里。镜像治疗用健侧影像来组织注意。两者已经是一套方案时，再加手套，问的是多一个设备之后量表有没有进一步的差别。非盲和 30 人的规模，决定了摘要里的“有差异”还不能当成确证。",
            ],
            "overview": [
                "两组都先接受 30 分钟常规治疗，再接受 30 分钟指定干预，每天 1 次、每周 5 次，共 8 周。A 组是机器人手套辅助的任务导向镜像治疗。B 组是任务导向镜像治疗。摘要写明机器人为 SYREBO，完整型号尚未用全文核对，因此配图只作为品牌场景。",
                "三项结局的中文名称：盒与块测试（文献缩写 BBT）看抓起并移动木块；上肢 Fugl-Meyer 评定（文献缩写 FMA-UE）看上肢运动损伤；上肢动作研究量表（文献缩写 ARAT）看上肢在抓、握、捏和粗大动作中的表现。",
            ],
            "meaning": [
                "治疗师能从摘要里讨论的，是在任务导向镜像已经排进课表时，加手套这一项有没有被报告为组间差别。对外表述要同时带上非盲、30 人、全文未核对的效应值，以及型号尚未确认。未读清的 p 值不能补进交班或产品材料。",
            ],
            "limits_add": "品牌名称不是型号确认。",
        },
        "en": {
            "background": [
                "Task-oriented practice places the exercise inside an action that resembles daily use. Mirror therapy uses the unaffected limb’s image to organize attention. When those two are already one program, adding a glove asks whether one more device is followed by a further difference on the scales. An unblinded design and a sample of 30 people mean a sentence that says “a difference” is not yet a confirmatory result.",
            ],
            "overview": [
                "Both arms had 30 minutes of usual care and then 30 minutes of the assigned intervention, once a day, five days a week, for eight weeks. Arm A was robotic-glove-assisted task-oriented mirror therapy. Arm B was task-oriented mirror therapy. The abstract names the robot as SYREBO. The full model has not been checked in the full text, so the photograph is only a brand scene.",
                "The three outcomes by their clinical names: the Box and Block Test (BBT) for picking up and moving blocks; the upper-limb Fugl-Meyer assessment (FMA-UE) for motor impairment; the Action Research Arm Test (ARAT) for grasp, grip, pinch, and gross movement.",
            ],
            "meaning": [
                "What a therapist can discuss from the abstract is whether, once task-oriented mirror therapy is already on the timetable, adding a glove was reported as a between-group difference. Any public sentence has to carry the unblinded design, the 30 people, the unchecked effect sizes, and the unconfirmed model. A p value that could not be read is not filled into a handover or a product sheet.",
            ],
            "limits_add": "A brand name is not a confirmed model.",
        },
    },
    "sup04": {
        "zh": {
            "background": [
                "慢性期的手，距离发病已经数月，自发恢复不再是亚急性期那种主要解释。此时仍要把握力和精细操作分开。握力是力量。钉板是把小栓放进孔里。电刺激和机器人手绑在同一节里时，对照若只有常规物理治疗，组间差别属于这一套组合相对于常规治疗，而不是手套单独相对于空白。",
            ],
            "overview": [
                "研究组先做机器人手与同步神经肌肉电刺激 20 分钟，再做常规物理治疗 30 分钟。对照组做常规物理治疗 50 分钟。每周 3 次，共 6 周。纳入年龄 50 至 65 岁、病程 6 至 24 个月。检索片段只支持品牌关联到 SY 开头，完整型号不猜测。",
                "本页转写的结局是握力（千克）和患手 Purdue 钉板。生活质量在题名里出现，完整分表尚未逐项核对，因此不展开。",
            ],
            "meaning": [
                "方案讨论可以停在论文已经分开的两句：握力的组间比较见该文 p=0.002；患手钉板的组间 p=0.076，不称作组间显著。向同事转述时保留组合方案、42 人完成和 6 周这些边界，不把千克的变化写成产品提升比例。",
            ],
            "limits_add": "不把未逐项核对的生活质量分数补进本页。",
        },
        "en": {
            "background": [
                "In the chronic period, months after the stroke, spontaneous recovery is no longer the main reading of a score. Grip and dexterity still have to be separated. Grip is force. A pegboard is the task of placing small pegs. When stimulation and a robotic hand share a session, and the control arm is usual physical therapy, the between-group gap belongs to that combination against usual care. It is not the glove alone against an empty hour.",
            ],
            "overview": [
                "The study arm had 20 minutes of robotic hand therapy with synchronized neuromuscular stimulation and then 30 minutes of usual physical therapy. The control arm had 50 minutes of usual physical therapy. Sessions were three times a week for six weeks. Inclusion was age 50 to 65 years and six to 24 months after stroke. A retrieved fragment supports a brand link only as far as a model string that begins with SY. The full model is not guessed.",
                "The outcomes transcribed here are grip, in kilograms, and the affected-hand Purdue pegboard. Quality of life is in the title. The full subscale table has not been checked item by item, so it is not expanded.",
            ],
            "meaning": [
                "A case discussion can stop at the two sentences the paper already separates: the between-group comparison for grip is the paper’s p=0.002, and the affected-hand pegboard between-group p=0.076 is not called significant between groups. A handover keeps the combined program, the 42 people who completed, and the six weeks. The change in kilograms is not rewritten as a product percentage.",
            ],
            "limits_add": "Quality-of-life scores that were not checked item by item are not added on this page.",
        },
    },
    "sup05": {
        "zh": {
            "background": [
                "治疗师有时会把“脑区更活跃”听成“恢复更好”。近红外记录的是任务进行时的皮层血氧，不是数周以后的手功能分数。健康人和卒中后患者的激活高低，还可以来自用力、注意和代偿。所以这类先导实验要和疗效试验分开放。",
            ],
            "overview": [
                "三种任务：机器人手套辅助的被动抓握；观看虚拟抓握影像；两者一起做。采集覆盖前额叶、运动皮层和枕叶，分析激活和功能连接。没有把上肢 Fugl-Meyer 评定或上肢动作研究量表设成主要结局。品牌和型号未在方法中核对，本页不放产品照片，以免用另一台设备顶替。",
            ],
            "meaning": [
                "它可以进入机制讨论：被动动作加上视觉场景，是否在当次任务里伴随更广的皮层激活。它不能进入疗效讨论，也不能在型号写进方法学之前被计成某一产品的实验。激活更高不等于功能更好。",
            ],
            "limits_add": "不把摘要中的激活差别换算成功能恢复比例。",
        },
        "en": {
            "background": [
                "A more active cortical map is sometimes heard as better recovery. Near-infrared recording is cortical oxygenation during a task, not a hand score weeks later. Differences between healthy adults and people after stroke can also come from effort, attention, and compensation. That is why this kind of pilot stays apart from an efficacy trial.",
            ],
            "overview": [
                "The three tasks were glove-assisted passive grasp, watching a virtual grasp, and both together. Recordings covered prefrontal, motor, and occipital cortex, with activation and functional connectivity. The upper-limb Fugl-Meyer assessment and the Action Research Arm Test were not the primary outcomes. Brand and model are not confirmed in the methods. This page shows no product photograph, so a different device is not asked to stand in.",
            ],
            "meaning": [
                "The paper can enter a mechanism discussion: whether passive movement plus a visual scene is accompanied by wider cortical activation during that task. It cannot enter an efficacy discussion, and it cannot be counted as an experiment on a named product before the model is written into the methods. Higher activation is not better function.",
            ],
            "limits_add": "Activation differences in the abstract are not converted into a recovery percentage.",
        },
    },
    "sup06": {
        "zh": {
            "background": [
                "软体外骨骼要跟着人的意图动，就需要一种信号告诉机器手想做什么。表面肌电是常见选择。幅度模式超声改看前臂的回波。对康复科来说，这仍是接口能不能识别规定动作的问题，不是患者疗程结束后的功能问题。",
            ],
            "overview": [
                "对象是 5 名健康受试者。任务是 7 种来自标准化评估协议的抓握，比较主动与被动条件。当前资料不足以确认识别准确率、交叉验证的完整流程，以及外骨骼的品牌和型号。本页不放产品照片，也不从其他超声论文借用准确率。",
            ],
            "meaning": [
                "工程阅读可以把它当作一条不同于表面肌电的意图通路，规模停在五名健康人和七种抓握。走到日常使用，还需要另行讨论可用性、稳定性和安全。在方法学写明品牌之前，不把它放进某一产品的证据表。",
            ],
            "limits_add": "其他论文的识别率不移植到本页。",
        },
        "en": {
            "background": [
                "A soft exoskeleton that is meant to follow intent needs a signal for what the hand is about to do. Surface electromyography is a familiar choice. Amplitude-mode ultrasound looks instead at forearm echoes. For a rehabilitation service this is still a question of whether an interface can recognize prescribed grasps. It is not a question of function after a course of care.",
            ],
            "overview": [
                "The participants were five healthy adults. The tasks were seven grasps drawn from a standardized assessment protocol, compared under active and passive conditions. The material in hand is not enough to confirm recognition accuracy, the full cross-validation procedure, or the brand and model of the exoskeleton. This page shows no product photograph and does not borrow accuracy figures from other ultrasound papers.",
            ],
            "meaning": [
                "An engineering reading can treat it as an intent path that is not surface electromyography, at the scale of five healthy adults and seven grasps. Daily use still needs a separate discussion of usability, stability, and safety. Until the methods name a brand, it does not go on a product’s evidence list.",
            ],
            "limits_add": "Recognition rates from other papers are not copied here.",
        },
    },
    "sup07": {
        "zh": {
            "background": [
                "软体结构靠气体改变形状。气泵的体积、热量、噪声和电路，会影响设备能放在什么房间。换一种供气方式，回答的是气源试样在台架上的压力、流量、温度和声音。它不回答手的分数，也不回答某一次训练是否安全。",
            ],
            "overview": [
                "摘要描述的系统用磷酸与碳酸氢铯的反应产生气体，把吸热和放热过程放在一起以约束发热，并用被动机械部件按系统状态调节，不使用电子控制元件。评价停留在气源试样。本页不补充制作步骤，也不放产品照片。是否在全文中演示了某一品牌的康复设备，尚未核实。",
            ],
            "meaning": [
                "设备讨论里，它只提供“泵以外的供气思路”这一句工程信息。台架读数不能改写成临床安全承诺，也不能改写成手功能变化。品牌关联未核实之前，不放入产品性能表。",
            ],
            "limits_add": "不补充反应配比或制作步骤。",
        },
        "en": {
            "background": [
                "A soft structure changes shape when it has gas. The size, heat, noise, and electronics of a pump affect the room a device can sit in. Another way of supplying gas answers how a source specimen behaves on a bench: pressure, flow, temperature, and sound. It does not answer a hand score, and it does not answer whether one training session was safe.",
            ],
            "overview": [
                "The system in the abstract generates gas from phosphoric acid and cesium bicarbonate, places endothermic and exothermic processes together to limit heat, and uses passive mechanical parts that follow system state. There is no electronic controller. The measurements stay with the source specimen. This page adds no fabrication steps and shows no product photograph. Whether the full text demonstrates a named rehabilitation device is unverified.",
            ],
            "meaning": [
                "In a hardware discussion, the paper supplies one engineering sentence: a supply idea that is not a conventional pump. Bench readings are not a clinical safety promise and not a change in hand function. Until a brand link is verified, they do not go on a product specification.",
            ],
            "limits_add": "Reaction ratios and fabrication steps are not added.",
        },
    },
    "sup08": {
        "zh": {
            "background": [
                "用品牌检索文献，引言里的产品名单也会被命中。命中只说明作者写过这个名字。方法里写明的那一台装置，才是实验设备。把二次提及收成产品研究，会让证据表和真正上过实验台的硬件对不上。",
            ],
            "overview": [
                "实验装置由清迈大学制作，用来测量手指静态最大屈曲，不是本品的手套。对照工具是手指量角器。同一天的上午和下午各测一次。系统分辨率在文中写为 0.01 度，量角器通常按 5 度读取。文献摘录的图是原文图 1，画面是这项研究自己的装置。",
                "结局是测量学指标，不是治疗结局：与量角器的一致性、重测相关、测量标准误，以及 95% 最小可检出变化。对象是 10 名健康、右利手、无症状的成年人。",
            ],
            "meaning": [
                "收录本篇，是为了让检索品牌的人先看方法学里的装置名称。测量学上的一致性和重测表现，属于这台高校自研装置。它们不能改写成品牌设备的验证，也不能外推到患者或动态抓握。",
            ],
            "limits_add": "引言中的品牌名单不是实验设备清单。",
        },
        "en": {
            "background": [
                "A search on a brand name also hits product lists in introductions. A hit means the authors wrote the name. The apparatus named in the methods is the device that was tested. Counting a secondary mention as a product study breaks the link between an evidence table and the hardware that was actually on the bench.",
            ],
            "overview": [
                "The apparatus was built at Chiang Mai University to measure static maximum finger flexion. It is not a glove from this brand. The comparison instrument was a finger goniometer. Measures were repeated on the same day, morning and afternoon. System resolution is given as 0.01 degrees, while a goniometer is usually read to 5 degrees. The figure in the excerpt is original Figure 1 and shows that study’s own apparatus.",
                "The outcomes are measurement properties, not treatment outcomes: agreement with the goniometer, retest correlation, the standard error of measurement, and the 95% minimal detectable change. The participants were 10 healthy, right-handed, asymptomatic adults.",
            ],
            "meaning": [
                "The paper is included so that a brand search starts with the apparatus named in the methods. Agreement and retest behavior belong to that university-built instrument. They cannot be rewritten as validation of a branded device, and they do not extend to patients or to dynamic grasp.",
            ],
            "limits_add": "A brand list in the introduction is not the list of apparatus.",
        },
    },
}


def _walk_strings(value, fn):
    if isinstance(value, str):
        return fn(value)
    if isinstance(value, list):
        return [_walk_strings(item, fn) for item in value]
    if isinstance(value, dict):
        return {key: _walk_strings(item, fn) for key, item in value.items()}
    return value


def _zh_units(text: str) -> str:
    return (
        text.replace("7 bar", "7巴")
        .replace("6 L/min", "每分钟6升")
        .replace("36°C", "36摄氏度")
        .replace("40 dBA", "40分贝")
        .replace("air-guitar", "气吉他")
    )


def apply_depth(studies) -> None:
    for study in studies:
        slug = study["slug"]
        extra = EXTRA[slug]
        study["related"] = RELATED[slug]
        for lang in ("zh", "en"):
            block = extra[lang]
            page = study[lang]
            for key in ("background", "overview", "meaning"):
                page[key] = list(page[key]) + list(block.get(key, []))
            if block.get("limits_add"):
                if lang == "zh":
                    page["limits"] = page["limits"].rstrip("。") + "。" + block["limits_add"]
                else:
                    page["limits"] = page["limits"].rstrip(".") + ". " + block["limits_add"]
        if slug == "sup07":
            study["zh"] = _walk_strings(study["zh"], _zh_units)
            study["poster"]["zh"] = _walk_strings(study["poster"]["zh"], _zh_units)
        if slug == "sup08":
            zh = study["zh"]
            title = zh["paper_title"]
            study["zh"] = _walk_strings(zh, _zh_units)
            study["zh"]["paper_title"] = title
            poster = study["poster"]["zh"]
            study["poster"]["zh"] = _walk_strings(poster, _zh_units)
