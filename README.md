# YATA-GAMIFIED (Yet Another Threat Antagonist)

> The Cybersecurity Ouroboros — Now Fully Gamified!

An autonomous security agent that attacks a codebase, heals the vulnerabilities it proves, attacks its own remediations, and learns from every assessment... **All visualized live in a retro 16-bit RPG dungeon!**

Most security tools stop at detection. **YATA refuses to trust detection alone.**
***A vulnerability is not accepted until YATA successfully exploits it.***
A patch is not accepted until YATA fails to break it.

**Attack. Heal. Attack Again. Learn.**

---

## 🎮 The Gamification Engine (Round 2 Addition!)

YATA isn't just a CLI anymore. We have built a complete, fully integrated **Canvas-based Gamification Engine** that visualizes the AI's internal state in real-time without breaking the core polling architecture!

### Features:
- **RPG Village Map:** The target repository is visualized as a Dungeon town (Townhall, Vault, Market Stall, Houses, Strongbox).
- **Demon Spawning:** As the `HUNTER` AI confirms vulnerabilities, different demons spawn on the afflicted buildings depending on the severity (Imps for Secrets, Hobgoblins for Command Injection, Big Demons for SQLi).
- **Epic Combat:** When the `VALIDATOR` confirms a patch works, a magical dragon swoops in, incinerates the demon with a devastating attack animation, and fades out, restoring peace to the building!
- **Interactive Parchment UI:** The 4-step Terminal approval workflow is mirrored perfectly onto a medieval parchment scroll in the game window.
- **Notification Stacking:** Rapid-fire terminal logs are cleanly caught and stacked as center-screen Toast notifications.

---

## 🤖 The Agents

1. **HUNTER (The Archer):** Scans the AST, builds attack paths, executes payloads, and confirms vulnerabilities.
2. **HEALER (The Sage):** Analyzes the broken code and generates secure, functional patches.
3. **VALIDATOR (The Knight):** Adversarial agent that takes the HEALER's patch and relentlessly tries to break it.
4. **LEARNER (The Scholar):** Maintains persistent security memory for the repository.
5. **MUTATOR:** **(New!)** A deterministic battery of known bypass techniques (e.g. `../../etc/passwd`, `' OR 1=1#`) that ensures the HEALER's patch isn't just a brittle regex, but a true structural fix!

---

## 🚀 Installation

YATA is fully packaged and installable natively.

### 1. Clone the Repository
```bash
git clone https://github.com/nishantx4/YATA-GAMIFIED.git
cd YATA-GAMIFIED
```

### 2. Create Virtual Environment
```powershell
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python -m venv .venv
source .venv/bin/activate
```

### 3. Install YATA
```bash
pip install -e .
```

### 4. Configure AI (Crucial for patches!)
Copy `.env.example` to `.env` and add your API Key so the Healer can write real patches!
*(If no key is found, YATA enters "Autonomous Fallback Mode", applying weak dummy patches that are designed to fail the Mutator Battery!)*

---

## 🎬 How to Run the Epic Demo

We have included a massive, extremely vulnerable repository specifically built to showcase YATA's full capabilities and animations!

### Step 1: Reset the Demo Environment
Because YATA's **LEARNER** agent remembers fixed vulnerabilities, you need to wipe its memory and reset the codebase before every demo run.
```powershell
cd test_repositories/epic_vulnerable_app
python demo_reset.py
```
*This instantly reverts all files and wipes YATA's memory for a fresh start.*

### Step 2: Launch the Assessment
Run YATA in interactive mode:
```powershell
yata assess . --interactive
```

### Step 3: Enjoy the Show
1. Open your browser to the Live Dashboard at `http://127.0.0.1:5050`
2. Watch the Dungeon map render.
3. Keep an eye out for Demons spawning on buildings as the Hunter finds vulnerabilities!
4. **Respond to the prompts in the Terminal!** (Continue -> Apply Patch -> Continue).
5. Watch the Parchment overlay in the game mirror your terminal choices.
6. Watch the Dragon incinerate the demons when patches pass the Mutator Battery!

*(P.S. There is an Easter Egg hidden in the bottom left corner of the map!)*

---

## 🛠️ CLI Commands Reference

YATA features a powerful, native CLI.

| Command | Usage | Description |
|---|---|---|
| `assess` | `yata assess <path> --safe` | Run a full offensive assessment. Mode flags: `--safe` (Sandbox), `--apply` (Overwrite), `--interactive` (Prompt User). |
| `discover` | `yata discover <path>` | Find all git repositories in a directory tree. |
| `memory` | `yata memory <repo_name>` | View the persistent security knowledge YATA has learned about a repo. |
| `history` | `yata history <repo_name>` | View a timeline of all past assessments. |
| `report` | `yata report <repo_name>` | Open the latest HTML executive summary report. |

---

# FAR AWAY 2026

Submitted under: **Agentic & Autonomous Systems**

> A security agent is only as trustworthy as its ability to defeat itself.

**Built by Team Seasaw.**
