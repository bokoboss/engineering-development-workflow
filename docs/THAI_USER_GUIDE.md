# คู่มือใช้งาน Engineering Development Workflow ภาษาไทย

เวอร์ชันคู่มือ: สำหรับ Workflow v1.7.4  
สถานะ: คู่มือการใช้งานภาษาไทย  
เอกสาร policy ภาษาอังกฤษใน repository ยังคงเป็น normative source of truth

---

## 1. คู่มือนี้เหมาะกับใคร

คู่มือนี้เขียนสำหรับผู้ที่ต้องการใช้ ChatGPT, Codex และ GitHub ช่วยพัฒนาซอฟต์แวร์อย่างเป็นระบบ โดยเฉพาะผู้ที่ไม่ได้เป็น software engineer เต็มเวลา แต่ต้องการให้ AI ช่วยพัฒนาโปรแกรมที่:

- ทำงานจริงได้;
- ตรวจสอบย้อนกลับได้;
- ลดการแก้แบบเดาสุ่ม;
- มีหลักฐานว่าทดสอบแล้ว;
- รักษาคุณภาพของงานวิศวกรรม;
- ไม่ให้ coding agent แก้ไฟล์หรือสร้างโฟลเดอร์นอก project โดยพลการ;
- เลือกความเข้มของ workflow ให้เหมาะกับความเสี่ยงของงาน;
- ไม่เสียเวลาและโควตากับขั้นตอนที่ไม่จำเป็น.

Workflow นี้ออกแบบโดยมีหลักสำคัญว่า:

> งานทุกงานต้องได้คุณภาพและปลอดภัย แต่ไม่จำเป็นต้องใช้ขั้นตอนหนักเท่ากันทุกงาน

---

## 2. ภาพรวมระบบ

ระบบแบ่งหน้าที่หลักเป็น 3 ส่วน:

```text
ChatGPT
Control Plane
คิด / วิเคราะห์ / วางแผน / เลือก work mode / review / accept
        |
        v
GitHub
Shared State / Evidence
Issue / Branch / Commit / PR / CI / Release
        ^
        |
        v
Codex
Execution Plane
แก้ไฟล์ / รันโปรแกรม / รัน test / browser / local environment
```

### ChatGPT ทำอะไร

ChatGPT ควรทำงานที่ไม่จำเป็นต้องแก้ local files ก่อน เช่น:

- inspect GitHub repository;
- ตรวจ current project state;
- วิเคราะห์ requirement;
- research;
- วาง architecture;
- ตรวจ UX/UI;
- หา root cause จาก evidence;
- ตัดสิน FAST / STANDARD / STRICT;
- เลือก model + reasoning effort;
- สร้าง prompt ให้ Codex;
- review PR/diff/CI;
- ตัดสิน accept / remediate / escalate.

### Codex ทำอะไร

Codex ใช้เมื่อจำเป็นต้องทำงานบนเครื่องหรือ local repository เช่น:

- แก้ source code;
- สร้าง/แก้ไฟล์;
- รัน unit/integration tests;
- เปิด local application;
- browser test;
- debug environment;
- build/package;
- commit/push/PR เมื่องานถูกกำหนด scope แล้ว.

### GitHub ทำอะไร

GitHub เป็นหลักฐานและสถานะกลาง เช่น:

- accepted commit;
- Issue;
- Pull Request;
- CI;
- review comments;
- release;
- changelog;
- project documentation.

คำรายงานของ Codex เช่น “tests passed” มีประโยชน์ แต่ไม่ควรมีน้ำหนักเท่าหลักฐานจริงจาก test output / CI / diff.

---

# ส่วน A — ตั้งค่า ChatGPT Project

## 3. สร้าง ChatGPT Project

แนะนำให้สร้าง ChatGPT Project แยกสำหรับแต่ละ software project เช่น:

- HCM Calculator
- Traffic Video Analytics
- Vehicle Engineering Database
- Airport Curbside Analysis Tool

เหตุผลคือแต่ละ project มี:

- requirement ต่างกัน;
- repository ต่างกัน;
- protected behavior ต่างกัน;
- current state ต่างกัน;
- conversation history ต่างกัน.

ไม่ควรใช้ ChatGPT Project เดียวรวม software projects หลายตัวถ้าไม่จำเป็น.

---

## 4. Project Instructions ต้องเอาจากไฟล์ไหน

ใช้ไฟล์นี้จาก repository workflow:

```text
templates/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Repository:

```text
https://github.com/bokoboss/engineering-development-workflow
```

### วิธีใช้

1. เปิด ChatGPT Project ของ software project.
2. เข้า Project settings / Instructions.
3. เปิดไฟล์:

```text
templates/CHATGPT_PROJECT_INSTRUCTIONS.md
```

4. Copy เนื้อหาทั้งไฟล์.
5. Paste ลง Project Instructions.
6. Save.

อย่า copy workflow ทุกไฟล์ลง Project Instructions.

เหตุผลคือ:

- ChatGPT ควรอ่าน current upstream workflow;
- Instructions ควรกระชับ;
- policy เปลี่ยนได้โดยไม่ต้อง paste ทุกไฟล์ใหม่;
- ลด context duplication.

---

## 5. ChatGPT Project Instructions กับ workflow local ต่างกันอย่างไร

มี 2 ฝั่ง:

### ฝั่ง ChatGPT

ใช้:

```text
templates/CHATGPT_PROJECT_INSTRUCTIONS.md
```

เพื่อบอก ChatGPT ว่า:

- ChatGPT เป็น control plane;
- ต้องใช้ workflow;
- ต้องเลือก work mode;
- ต้องคำนึงถึง workspace safety;
- ต้องทำงานที่ทำใน ChatGPT ได้ก่อน;
- Codex ใช้เมื่อจำเป็น;
- ต้อง review evidence ก่อน accept.

### ฝั่ง Codex

ใน target repository จะมี:

```text
.engineering-workflow/
```

ซึ่งถูก install เข้า project โดย installer.

Codex เริ่มอ่านจาก:

```text
.engineering-workflow/SKILL.md
```

แล้วอ่านเฉพาะ policy/skill ที่ task ต้องใช้.

---

# ส่วน B — ติดตั้ง workflow ใน target repository

## 6. ต้องติดตั้ง workflow ก่อนใช้ Codex ไหม

สำหรับ project ที่จะใช้ workflow นี้จริงเป็นประจำ:

> แนะนำให้ติดตั้งและ validate workflow ก่อนให้ Codex เริ่ม feature/fix แรก

เหตุผลคือ Codex จะมี local pinned policy ของ project อยู่แล้ว เช่น:

```text
.engineering-workflow/
├── SKILL.md
├── WORK_MODE_ROUTING.md
├── WORKSPACE_SAFETY.md
├── ENGINEERING_DEV_WORKFLOW.md
├── MODEL_ROUTING_POLICY.md
├── CONTEXT_MANAGEMENT.md
├── SECURITY_AND_GOVERNANCE.md
├── ACCEPTANCE_AND_EVIDENCE.md
├── skills/
└── templates/
```

Codex จึงไม่ต้องเดาว่า workflow version ไหนต้องใช้.

---

## 7. สิ่งที่ต้องมีบนเครื่อง

สำหรับ installer:

- Python 3;
- target project directory;
- checkout ของ `engineering-development-workflow`.

ตัว installer:

```text
scripts/setup_project.py
```

เป็น stdlib-only และไม่มี network access.

หมายเหตุ:

> การ `git clone` workflow repository ใช้ network แต่ตัว Python installer เองไม่ใช้งาน network.

---

## 8. ตัวอย่างโครงสร้าง directory บน Windows

สมมติ:

```text
D:\R&D\engineering-development-workflow
D:\R&D\my-project
```

อย่าใช้:

```text
C:\
C:\Users\ชื่อผู้ใช้
D:\R&D
```

เป็น target ถ้า directory เหล่านี้เป็น parent กว้างที่มี project อื่นอยู่ด้วย.

Target ควรเป็น project root ที่ชัดเจน เช่น:

```text
D:\R&D\hcm-calculator
```

---

## 9. ติดตั้ง workflow ใน project ใหม่

เปิด PowerShell.

เข้า workflow repository:

```powershell
cd D:\R&D\engineering-development-workflow
```

ตรวจ project ก่อน:

```powershell
python scripts\setup_project.py inspect "D:\R&D\my-project"
```

จากนั้น install:

```powershell
python scripts\setup_project.py install "D:\R&D\my-project"
```

แล้ว validate:

```powershell
python scripts\setup_project.py validate "D:\R&D\my-project"
```

ผลที่ต้องการ:

```text
VALIDATION PASS
```

ถ้า installer รายงาน conflict:

> ห้าม force overwrite.

ให้หยุดและอ่านว่าไฟล์ไหน conflict ก่อน.

---

## 10. ติดตั้งผ่าน Codex ได้ไหม

ได้ แต่ prompt ต้องชัดว่า Codex:

- ใช้ workflow checkout เป็น read-only installer source;
- target เขียนได้เฉพาะ project root;
- ห้ามไปแก้ workflow source checkout;
- ห้ามสร้าง staging folder นอก project;
- ห้าม global install;
- ห้าม force overwrite conflict.

ตัวอย่าง prompt:

```text
ติดตั้ง Engineering Development Workflow v1.7.3 เข้า repository นี้ก่อนเริ่มงาน feature

Workflow source:
D:\R&D\engineering-development-workflow

Target project:
D:\R&D\my-project

Work mode: FAST
Scope: workflow adoption only

ก่อนทำ:
1. inspect target
2. ใช้ scripts/setup_project.py จาก workflow source
3. ห้ามแก้ workflow source checkout
4. writable boundary คือ D:\R&D\my-project เท่านั้น
5. ห้ามเขียนไฟล์/สร้าง directory นอก target
6. ห้าม global install หรือแก้ system/user config

ทำตามลำดับ:
inspect -> install -> validate

ถ้ามี conflict ให้หยุดและรายงาน ห้าม force overwrite
```

---

## 11. หลัง install จะเกิดอะไรขึ้น

โดยทั่วไป target project จะมี:

```text
AGENTS.md
PROJECT_PROFILE.md
.engineering-workflow.json
.engineering-workflow/
docs/development/
.github/ISSUE_TEMPLATE/
```

### AGENTS.md

เป็น instruction สำหรับ coding agent ใน project นี้.

ใช้เก็บ permanent project-specific rules ได้ เช่น:

- ห้ามเปลี่ยนสูตรบางส่วน;
- ต้องรักษา Thai/English UI;
- test command;
- architecture rules;
- file ownership;
- business constraints.

### PROJECT_PROFILE.md

เป็น project contract แบบกระชับ.

ควรมีข้อมูลที่ตรวจสอบได้ เช่น:

- current accepted baseline;
- architecture;
- important commands;
- protected behavior;
- validation matrix;
- current next objective.

อย่าใส่ข้อมูลที่เดา.

### .engineering-workflow.json

เป็น manifest ของ workflow ที่ติดตั้งใน project.

ใช้บันทึก:

- workflow version;
- managed files;
- hashes;
- local workflow directory.

ช่วยให้ upgrade ปลอดภัยและ detect local modification/conflict ได้.

### .engineering-workflow/

เป็น pinned local workflow snapshot สำหรับ Codex.

ตั้งแต่ v1.7.4 execution/evidence templates ที่ installer จัดการมีชุดเดียวที่:

```text
.engineering-workflow/templates/
```

ไม่มีการติดตั้ง duplicate อีกชุดใต้ `docs/development/templates/` แล้ว.

ไม่ควรแก้ไฟล์ managed ใน `.engineering-workflow/` โดยตรง.

ถ้าต้องการอัปเดตให้ใช้ installer `upgrade`.

---

# ส่วน C — อัปเกรด workflow ใน project เดิม

## 12. เมื่อไรควร upgrade

ควร upgrade เมื่อ:

- project ยังใช้ workflow version เก่า;
- workflow ใหม่แก้ safety/quality/routing;
- ก่อนเริ่ม development stage ใหม่ที่มี Codex ทำงานต่อเนื่อง;
- ChatGPT พบ upstream/local version mismatch.

ไม่จำเป็นต้อง upgrade ทุก repository พร้อมกันทันที.

หลักที่แนะนำ:

> Upgrade เมื่อ project นั้นกำลังจะกลับมาทำงานจริง.

---

## 13. วิธีดูว่า project ใช้ version ไหน

เปิด:

```text
.engineering-workflow.json
```

ดู:

```json
"workflow_version": "1.7.4"
```

หรือรัน:

```powershell
python scripts\setup_project.py inspect "D:\R&D\my-project"
```

จาก workflow checkout ล่าสุด.

---

## 14. Upgrade project

จาก workflow checkout:

```powershell
cd D:\R&D\engineering-development-workflow
```

รัน:

```powershell
python scripts\setup_project.py inspect "D:\R&D\my-project"
python scripts\setup_project.py upgrade "D:\R&D\my-project"
python scripts\setup_project.py validate "D:\R&D\my-project"
```

### ถ้าเจอ locally modified managed file

installer จะ block.

ในการ upgrade จากเวอร์ชันเก่า v1.7.4 อาจ retire ไฟล์ duplicate/protocol เก่าที่ installer เคยจัดการ แต่จะลบเฉพาะไฟล์ใน allowlist ที่ manifest เดิมยืนยัน ownership และ hash ยังไม่ถูกแก้เท่านั้น. ถ้าไฟล์นั้นถูกแก้ locally จะไม่ลบและจะ block upgrade เพื่อให้ตรวจสอบก่อน.

อย่าใช้ force overwrite.

ให้ตรวจว่า:

- ใครแก้;
- แก้เพราะอะไร;
- เป็น project-specific rule ที่ควรอยู่ใน AGENTS.md หรือไม่;
- ต้อง preserve หรือ migrate อย่างไร.

---

# ส่วน D — การเริ่ม task ใหม่

## 15. เริ่มจาก ChatGPT ก่อน

สำหรับ task ปกติ ให้เริ่มจาก ChatGPT Project ไม่ใช่ Codex โดยตรง.

ตัวอย่าง:

```text
ไปต่อ Issue #XX
```

หรือ:

```text
ช่วยตรวจสถานะ repo แล้ววางแผนแก้ defect นี้
```

หรือ:

```text
ต้องการเพิ่ม feature X ช่วยวาง scope และดูว่าต้องใช้ Codex อย่างไร
```

ChatGPT ควร:

1. inspect current state;
2. เลือก work mode;
3. ทำ research/review ที่ทำได้;
4. ระบุ scope;
5. เลือก model/effort;
6. สร้าง Codex packet เมื่อจำเป็น.

---

# ส่วน E — FAST / STANDARD / STRICT

## 16. Work mode คืออะไร

Work mode ควบคุม:

- ความละเอียดของ process;
- จำนวน gate;
- validation depth;
- review intensity.

ไม่ได้ควบคุม:

- คุณภาพขั้นต่ำ.

ทุก mode ต้อง:

- inspect ก่อน modify;
- scope ชัด;
- ไม่แก้นอกเรื่อง;
- validation เหมาะสม;
- review actual diff;
- ไม่ประกาศ DONE เมื่อ mandatory gate fail.

---

## 17. FAST

ใช้เมื่อ:

- งานเล็ก;
- scope ชัด;
- reversible;
- ไม่แตะ protected logic;
- regression surface แคบ;
- มี concrete proof path.

FAST ต้องตอบได้ว่า:

> จะพิสูจน์ว่าแก้ถูกได้อย่างไร?

proof path อย่างน้อยหนึ่งแบบ:

- reliable reproducer;
- existing test ที่ test behavior ตรง;
- deterministic before/after check.

### ตัวอย่าง FAST

- typo;
- แก้ text UI;
- spacing;
- test fixture ที่ไม่เปลี่ยน production semantics;
- bug เล็กที่ reproduce ได้แน่นอน;
- config project-local ที่มี deterministic validation.

### Flow

```text
inspect เฉพาะที่เกี่ยว
-> compact FAST packet
-> bounded change
-> targeted validation
-> diff review
-> required CI
-> accept
```

FAST โดย default ไม่ต้อง:

- Deep Research;
- full scrutiny;
- independent review;
- full repository reconstruction;
- full test suite.

ถ้าไม่จำเป็น.

---

## 18. สิ่งที่ดูเหมือน FAST แต่ไม่ใช่

จำนวนบรรทัดน้อยไม่ได้แปลว่า low risk.

ตัวอย่าง:

### แก้สูตรวิศวกรรม 1 บรรทัด

```text
STRICT
```

### แก้ authentication 1 บรรทัด

```text
STRICT
```

### เปลี่ยน network exposure config นิดเดียว

```text
STRICT
```

### schema/migration เล็ก

```text
STRICT
```

### dependency version bump ที่ไม่รู้ compatibility

```text
STANDARD หรือ STRICT
```

### bug ที่ reproduce ไม่ได้

```text
STANDARD
```

ถ้า blast radius สูง:

```text
STRICT
```

---

## 19. STANDARD

ใช้กับงาน feature/bug ปกติ.

เช่น:

- feature หลายไฟล์;
- normal refactor;
- integration;
- UI flow;
- bug ที่ต้องแก้หลาย module;
- dependency change ที่ bounded ได้.

Flow:

```text
inspect
-> scope
-> conditional research/scrutiny
-> execute
-> targeted + relevant regression tests
-> PR/CI
-> ChatGPT review
-> accept
```

STANDARD เป็น default เมื่อ task ไม่ชัดพอสำหรับ FAST แต่ยังไม่มี STRICT trigger.

---

## 20. STRICT

ใช้กับงานเสี่ยงสูง เช่น:

- engineering formula;
- methodology;
- threshold;
- safety;
- security;
- auth;
- secrets;
- privacy;
- legal/regulatory;
- schema migration;
- destructive operation;
- architecture;
- public API;
- production-critical behavior;
- system/global modification;
- external filesystem write;
- high-impact uncertainty.

STRICT ใช้ full evidence-first workflow ตามความเสี่ยง.

ไม่ได้แปลว่าต้องใช้โมเดลแพงที่สุดเสมอ.

---

# ส่วน F — การเลือก Model และ Effort

## 21. Work mode ไม่เท่ากับ model tier

ตัวอย่าง:

### FAST

มักเหมาะกับ:

```text
Luna / Medium
```

หรือ High ถ้าซับซ้อนขึ้นเล็กน้อย.

### STANDARD

มักเหมาะกับ:

```text
Luna / High หรือ Max
```

และอาจใช้ Terra High/Max เมื่องานยัง bounded แต่ต้องใช้ judgment หรือ cross-module synthesis มากขึ้น.

### STRICT

ไม่ได้แปลว่าต้องใช้ Astra หรือโมเดลแพงที่สุดเสมอ.

ตัวอย่าง:

ChatGPT อาจทำ engineering reasoning ที่ยากเสร็จแล้ว และสร้าง implementation packet ที่ mechanical มาก.

Codex อาจยังใช้ Luna ได้ถ้า:

- scope ชัด;
- tests strong;
- execution mechanical;
- acceptance/review เข้ม.

### Astra เหมาะเมื่อใด

Astra High เหมาะกับงาน end-to-end ที่ยากและมีหลายส่วนประกอบพร้อมกัน เช่น:

- แก้ code พร้อมรัน terminal/runtime/browser;
- integration หลาย technology stack;
- performance / packaging / security evidence เป็นส่วนหนึ่งของงาน;
- งานยาวหลายขั้นตอนที่ต้องรักษา task state และ follow-through;
- ต้องปรับตัวตามผล test/runtime ระหว่างทาง;
- มี adjacent scope ที่ต้องห้ามหลุดไปทำก่อนเวลา.

สำหรับงานแบบนี้ การใช้ Astra High ตั้งแต่ต้นอาจถูกกว่าการ retry Luna/Terra หลายรอบ.

อย่าใช้ Astra เพียงเพราะ:

- งานเป็น STRICT;
- repo ใหญ่;
- prompt ยาว;
- งาน routine แต่เยอะ;
- packet ยังไม่ชัด.

Astra XHigh/Max ควรสงวนไว้สำหรับงานที่ยากที่สุด เช่น architecture evidence ขัดกัน, major migration, unknown root cause ที่ซับซ้อนมาก หรือ independent adjudication ที่มีความเสี่ยงสูง.

Sol High/Max ยังใช้เป็น fallback ได้ถ้า Astra ยังไม่มีใน account/surface ปัจจุบัน, allowance จำกัด, หรือ continuity ของ Sol context เดิมช่วยลด cost to verified completion.

---

## 22. ChatGPT ควรระบุอะไรให้ก่อน Codex

ก่อนส่ง Codex ควรเห็นข้อมูลประมาณนี้:

```text
Work mode: STANDARD
Mode confidence: high
Mode rationale: ...

Quality floor: ...

Target project root:
D:\R&D\my-project

Workspace write boundary:
target project root only

External writes allowed:
No

Required local workflow/skills:
- .engineering-workflow/SKILL.md
- systematic-debug

Model:
Luna

Reasoning effort:
High

Chat:
same chat / new chat

Scope:
...

Evidence reusable:
...

Success gates:
...

Stop/escalation conditions:
...
```

ถ้า ChatGPT ไม่ระบุ work mode ก่อน Codex execution สามารถถามได้ว่า:

```text
งานนี้ควรเป็น FAST / STANDARD / STRICT และใช้ model/effort เท่าไหร่
```

---

# ส่วน G — Workspace Safety

## 23. กฎสำคัญที่สุด

Writable boundary โดย default คือ:

> target project root เท่านั้น

ตัวอย่าง:

```text
D:\R&D\my-project
```

Codex สามารถแก้:

```text
D:\R&D\my-project\src
D:\R&D\my-project\tests
D:\R&D\my-project\docs
```

แต่โดย defaultห้ามแก้:

```text
D:\R&D\another-project
C:\Users\...
C:\Program Files\...
workflow source repo
Windows Registry
global Git config
shell profile
SSH keys
global PATH
```

---

## 24. ห้ามสร้าง folder นอก project เพื่อความสะดวก

เช่น:

```text
C:\temp\codex-work
D:\scratch-project
Desktop\test-output
```

ไม่ควรสร้างเองถ้า project-local directory ทำได้.

ควรใช้:

```text
D:\R&D\my-project\.tmp
D:\R&D\my-project\artifacts
D:\R&D\my-project\test-output
```

ตามความเหมาะสมและถ้าไม่ขัดกับ project policy.

---

## 25. Global installation

โดย defaultห้าม:

```powershell
npm install -g ...
pip install ... แบบ global
```

ห้ามแก้:

- PATH;
- registry;
- services;
- scheduled tasks;
- global Git config;
- user shell profile.

ถ้าจำเป็นจริง:

1. Codex ต้องหยุด;
2. ระบุ exact change;
3. บอกเหตุผล;
4. เสนอ project-local alternative;
5. ขอ explicit approval.

---

## 26. Symlink / Junction

Directory ที่ดูเหมือนอยู่ใน project อาจ link ไปที่อื่น.

เช่น:

```text
D:\R&D\my-project\data
```

อาจจริง ๆ ชี้ไป:

```text
D:\Shared\client-data
```

ถ้าไม่สามารถพิสูจน์ containment ได้:

> ห้ามเขียนผ่าน path นั้น.

---

## 27. Dirty worktree

ถ้า repository มี uncommitted changes ที่ไม่รู้ที่มา:

Codex ไม่ควร:

- reset;
- clean;
- overwrite;
- stash แบบไม่ถาม;
- delete.

ควรรายงาน:

```text
พบ pre-existing changes:
- file A
- file B

ยังไม่ทราบ ownership
จึงหยุดก่อน mutation ที่อาจกระทบไฟล์เหล่านี้
```

---

# ส่วน H — Evidence และ Testing

## 28. Evidence reuse

ไม่จำเป็นต้อง rerun test ทุกชุดทุก stage ถ้า evidence ยัง valid.

ตัวอย่าง:

```text
HEAD A
unit tests PASS
```

ต่อมาแค่ review เอกสารโดย code ไม่เปลี่ยน:

ไม่จำเป็นต้อง rerun test เพราะ stage เปลี่ยน.

แต่ถ้า:

```text
HEAD A -> HEAD B
```

และ code ที่ test cover ถูกแก้:

ต้อง run ใหม่ตามความเสี่ยง.

---

## 29. Targeted test กับ full regression

### FAST

มักใช้:

- targeted test;
- direct reproducer;
- required CI.

### STANDARD

มักใช้:

- targeted test;
- relevant regression;
- CI.

### STRICT

อาจใช้:

- focused unit;
- integration;
- full regression;
- real data;
- browser/UAT;
- engineering cross-check;
- independent review;
- human approval.

ตาม risk.

---

## 30. Codex บอก PASS แล้ว เชื่อได้เลยไหม

ไม่ควรใช้คำรายงานอย่างเดียว.

ควรดู:

- command;
- output;
- test count;
- exit status;
- changed files;
- diff;
- GitHub CI;
- artifacts;
- real runtime evidence.

ChatGPT ควร review actual GitHub evidence ก่อน final acceptance เมื่อทำได้.

---

# ส่วน I — GitHub Workflow

## 31. Issue

Issue คือ work order.

ใช้เก็บ:

- objective;
- scope;
- out-of-scope;
- gates;
- known risks;
- decision;
- current state.

ไม่จำเป็นต้องเปิด Issue สำหรับ typo เล็กทุกครั้งถ้า workflow/project policy ไม่ต้องการ.

---

## 32. Branch

งานที่ควร review ควรแยก branch.

เช่น:

```text
fix/login-validation
feat/report-export
docs/thai-user-guide
```

Codex ไม่ควรแก้ unrelated branches/repositories.

---

## 33. Pull Request

PR ใช้สำหรับ review:

- actual diff;
- tests;
- CI;
- scope;
- limitations.

ChatGPT สามารถตรวจ PR โดยตรงผ่าน GitHub ก่อน accept.

---

## 34. CI

CI เป็น deterministic gate.

ถ้า CI FAIL:

> ยังไม่ถือว่างานเสร็จ.

ควรหา root cause.

อย่า retry ซ้ำแบบสุ่มโดยไม่วิเคราะห์ failure.

---

## 35. Releases

Stable workflow release ใช้:

```text
vX.Y.Z
```

เช่น:

```text
v1.7.3
```

Stable release ต้องผูกกับ accepted commit ที่แน่นอน.

Project ที่ต้องการ pin workflow สามารถอ้าง:

- version;
- tag;
- commit SHA.

---

# ส่วน J — Workflow ในการทำงานประจำวัน

## 36. ตัวอย่างงาน FAST

User:

```text
ปุ่ม Save ชิดขอบเกินไป ช่วยแก้
```

ChatGPT:

1. inspect current UI implementation;
2. classify FAST;
3. ระบุ proof path เช่น screenshot/browser assertion;
4. สร้าง compact Codex packet;
5. Codex แก้เฉพาะไฟล์ที่เกี่ยว;
6. targeted UI/browser test;
7. review diff;
8. required CI;
9. accept.

---

## 37. ตัวอย่าง STANDARD

User:

```text
เพิ่ม export Excel ในหน้ารายงาน
```

ChatGPT:

1. inspect architecture;
2. classify STANDARD;
3. หา existing export pattern;
4. define scope;
5. choose model/effort;
6. Codex implement;
7. focused + relevant regression test;
8. PR/CI;
9. ChatGPT review;
10. accept/remediate.

---

## 38. ตัวอย่าง STRICT

User:

```text
แก้สูตร capacity calculation ให้เป็นเกณฑ์ใหม่
```

ChatGPT:

1. classify STRICT;
2. verify engineering source/methodology;
3. establish protected behavior;
4. scrutiny;
5. explicit execution contract;
6. Codex implement;
7. numerical/engineering validation;
8. regression;
9. fresh/independent review;
10. human acceptance.

แม้ code เปลี่ยนเพียง 1-2 บรรทัดก็ยัง STRICT.

---

# ส่วน K — การใช้ Skills

## 39. Skills ไม่ต้องใช้ทุกตัว

Codex/ChatGPT ไม่ควรโหลดทุก skill ทุก task.

### research-gate

ใช้เมื่อยังไม่รู้:

- feasibility;
- dependency;
- compatibility;
- methodology;
- licensing;
- current external facts.

### scrutinize

ใช้ challenge:

- architecture;
- high-risk plan;
- merge readiness;
- protected change.

### systematic-debug

ใช้เมื่อ:

- bug;
- regression;
- failing test;
- failing CI;
- runtime defect.

### independent-review

ใช้เมื่อ acceptance risk สมควรมี fresh second pass.

### postmortem

ใช้หลัง incident/defect ที่มีบทเรียน reusable.

### technical-status

ใช้สรุป output ยาว/ซับซ้อนให้ decision-ready.

### long-task-guard

ใช้กับ task ยาวหลายขั้น/หลาย worker.

### loop-readiness

ใช้กับ recurring automation / continuous operation.

---

# ส่วน L — Continuous Operations

## 40. ต้องใช้ทุก project ไหม

ไม่.

Continuous Operations เป็น optional advanced layer.

เหมาะเมื่ออยาก:

- monitor PR/CI;
- recurring checks;
- event-driven workflow;
- scheduled operation.

New loop เริ่ม A1 observe/report ก่อน.

อย่าเปิด unattended mutation เพียงเพราะทำได้.

สำหรับ project ปกติ:

> ยังไม่ต้อง configure continuous loop ตอนเริ่มต้น.

---

# ส่วน M — Troubleshooting

## 41. install แล้วขึ้น conflict

ความหมาย:

installer พบไฟล์ที่จะถูก overwrite แต่:

- ไม่ใช่ managed file;
- หรือถูกแก้หลัง install.

ทำ:

1. หยุด;
2. inspect file;
3. ดูว่าเป็น project-owned change หรือไม่;
4. ถ้า project-specific ให้ย้าย rule ไป AGENTS.md/PROJECT_PROFILE.md ตามเหมาะสม;
5. reconcile แล้วค่อย upgrade.

ห้าม:

```text
force overwrite
```

---

## 42. validate FAIL

อ่าน error ทีละรายการ.

ตัวอย่าง:

```text
missing managed file
```

อาจหมายถึง local workflow snapshot ถูกลบ.

ใช้:

```powershell
python scripts\setup_project.py inspect "D:\R&D\my-project"
```

แล้วพิจารณา upgrade.

---

## 43. ChatGPT กับ local workflow version ไม่ตรง

ตัวอย่าง:

upstream:

```text
v1.7.3
```

project local:

```text
v1.7.1
```

ไม่จำเป็นต้อง panic.

ChatGPT ควรดูว่า task ต้องใช้ policy ใหม่หรือไม่.

ถ้ากำลังจะให้ Codexทำงานจริงและ version ใหม่มี safety/routing ที่เกี่ยว:

> upgrade ก่อน.

อย่า mix policy เงียบ ๆ.

---

## 44. Codex อยากสร้าง folder นอก project

ให้หยุด.

ถาม:

- ทำไมจำเป็น;
- project-local alternative คืออะไร;
- exact external path คืออะไร.

Default answer:

> ไม่อนุญาต.

อนุญาตเฉพาะเมื่อมีเหตุผลและ explicit approval.

---

## 45. Codex อยากติดตั้ง global tool

ให้ถามก่อน:

```text
มีวิธี project-local ไหม
```

เช่นใช้:

- local virtualenv;
- local npm dependency;
- portable binary ใน project;
- project script.

ถ้าจำเป็นต้อง global จริง:

STRICT + explicit approval.

---

## 46. CI fail หลัง Codex บอก local pass

ถือว่า:

```text
งานยังไม่ complete
```

หา environment difference / test mismatch / dependency / packaging issue.

ไม่ ignore CI.

---

# ส่วน N — Checklists

## 47. Checklist โปรเจกต์ใหม่

- [ ] สร้าง GitHub repository
- [ ] สร้าง ChatGPT Project
- [ ] Copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` เข้า Project Instructions
- [ ] clone workflow repository รุ่นที่ต้องการ
- [ ] inspect target repository
- [ ] install workflow
- [ ] validate workflow
- [ ] ตรวจ `.engineering-workflow.json`
- [ ] fill `PROJECT_PROFILE.md` จาก facts จริง
- [ ] เพิ่ม project-specific rules ใน `AGENTS.md`
- [ ] ให้ ChatGPT inspect project ก่อน task แรก
- [ ] ให้ ChatGPT เลือก FAST/STANDARD/STRICT
- [ ] ค่อย invoke Codex

---

## 48. Checklist ก่อนส่ง Codex

- [ ] Work mode ชัด
- [ ] target project root ชัด
- [ ] external writes = No โดย default
- [ ] local workflow installed/validated
- [ ] scope ชัด
- [ ] protected/out-of-scope ชัด
- [ ] model + effort ชัด
- [ ] same/new chat ชัด
- [ ] relevant skills เท่านั้น
- [ ] success gates ชัด
- [ ] stop/escalation conditions ชัด
- [ ] evidence reuse ชัด

---

## 49. Checklist หลัง Codex ทำเสร็จ

- [ ] changed files อยู่ใน scope
- [ ] ไม่มี external writes ที่ไม่ได้อนุมัติ
- [ ] ไม่มี global/system change ที่ไม่ได้อนุมัติ
- [ ] targeted tests ผ่าน
- [ ] regression ที่จำเป็นผ่าน
- [ ] actual diff ถูก review
- [ ] CI ผ่าน
- [ ] artifacts/runtime evidence ถูกตรวจถ้าจำเป็น
- [ ] independent review ถ้า risk ต้องการ
- [ ] GitHub state/PR สอดคล้องกับ report
- [ ] ค่อย accept/merge

---

## 50. Checklist upgrade workflow

- [ ] project กำลังจะใช้งานจริงหรือมีเหตุผลต้อง upgrade
- [ ] workflow source checkout อยู่ที่ release/commit ที่ตั้งใจ
- [ ] inspect target
- [ ] ตรวจ dirty/local modifications
- [ ] upgrade
- [ ] validate
- [ ] ตรวจ `.engineering-workflow.json`
- [ ] ห้าม force conflict
- [ ] review diff
- [ ] CI ถ้า project policy ต้องการ

---

# ส่วน O — Prompt ตัวอย่าง

## 51. Prompt เริ่มงานทั่วไปใน ChatGPT

```text
ใช้ Engineering Development Workflow ของเราในการทำงานนี้

ช่วยตรวจ current repository/project state ก่อน
จากนั้น:
1. เลือก Work mode: FAST / STANDARD / STRICT
2. อธิบายเหตุผล
3. ทำงานฝั่ง ChatGPT ให้ได้มากที่สุดก่อน
4. ถ้าต้องใช้ Codex ให้ระบุ model, reasoning effort, same/new chat
5. ระบุ target project root และ workspace write boundary
6. external writes ให้เป็น No โดย default
7. เลือกเฉพาะ skills ที่จำเป็น
8. ระบุ success gates
9. ระบุ stop/escalation conditions
10. สร้าง prompt สำหรับ Codex พร้อมใช้
```

---

## 52. Prompt ตรวจงาน Codex หลังทำเสร็จ

```text
ช่วย review งานจาก Codex ตาม Engineering Development Workflow

ตรวจ:
- actual diff
- scope
- work mode ยังเหมาะสมหรือไม่
- tests
- CI
- protected behavior
- workspace safety
- unresolved findings

อย่าอาศัย executor summary อย่างเดียว
ถ้ามี defect ให้ระบุ root cause และ remediation
ถ้าผ่านให้บอก acceptance basis ชัดเจน
```

---

## 53. Prompt upgrade workflow ใน project

```text
ก่อนเริ่ม feature ใหม่ ช่วยตรวจว่า project นี้ใช้ Engineering Development Workflow version อะไร

ถ้า local .engineering-workflow.json เก่ากว่า version ที่ควรใช้:
- inspect ก่อน
- upgrade แบบ conflict-safe
- validate
- ห้าม force overwrite
- ห้ามแก้ไฟล์นอก project root
- ห้ามแก้ workflow source checkout
- ห้าม global/system changes

หลัง upgrade ให้รายงาน version, changed managed files, conflicts, validation และ external writes
```

---

# ส่วน P — หลักที่ควรจำ

## 54. 10 กฎสั้น ๆ

1. เริ่มจาก ChatGPT ก่อน Codex เมื่อทำได้.
2. ChatGPT ต้องเลือก FAST / STANDARD / STRICT.
3. FAST ลดพิธีการ ไม่ลดคุณภาพ.
4. งานวิศวกรรม/security/ระบบสำคัญอาจ STRICT แม้แก้ 1 บรรทัด.
5. Codex เขียนได้ใน project root เท่านั้นโดย default.
6. ห้ามสร้าง/แก้ไฟล์นอก project เพื่อความสะดวก.
7. ห้าม global/system change โดยไม่มี explicit approval.
8. เชื่อ evidence มากกว่า agent confidence.
9. ใช้ GitHub เป็น shared accepted state.
10. ถ้ามี uncertainty/risk เพิ่ม ให้ escalate workflow ก่อนทำต่อ.

---

## 55. เอกสารอ้างอิงหลัก

ถ้าต้องการรายละเอียด policy:

- `WORK_MODE_ROUTING.md` — FAST / STANDARD / STRICT
- `WORKSPACE_SAFETY.md` — filesystem/system safety
- `ENGINEERING_DEV_WORKFLOW.md` — core workflow
- `MODEL_ROUTING_POLICY.md` — model/effort routing
- `ACCEPTANCE_AND_EVIDENCE.md` — evidence and acceptance
- `SECURITY_AND_GOVERNANCE.md` — security/governance
- `CONTEXT_MANAGEMENT.md` — context management
- `docs/CHEAT_SHEET.md` — one-page summary
- `docs/installation.md` — installer details
- `docs/chatgpt-project-setup.md` — ChatGPT Project setup
- `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` — Project Instructions ที่ต้อง copy เข้า ChatGPT

---

## 56. ลำดับใช้งานที่แนะนำที่สุด

สำหรับผู้ใช้ทั่วไป ใช้ลำดับนี้:

```text
1. สร้าง GitHub repo
2. สร้าง ChatGPT Project
3. ใส่ Project Instructions
4. ติดตั้ง workflow เข้า target repo
5. validate
6. ให้ ChatGPT inspect project
7. ChatGPT เลือก FAST/STANDARD/STRICT
8. ChatGPT ทำ research/planning/review ที่ทำได้
9. ส่ง bounded prompt ให้ Codex
10. Codex execute เฉพาะใน project root
11. tests / PR / CI
12. ChatGPT review actual evidence
13. accept / remediate
14. release เมื่อเหมาะสม
```

นี่คือ default path ที่ควรใช้ เว้นแต่ project-specific policy ระบุเป็นอย่างอื่น.
