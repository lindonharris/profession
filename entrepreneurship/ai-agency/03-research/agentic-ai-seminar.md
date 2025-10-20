# Agentic AI Seminar Notes

**Date:** October 14, 2025
**Source:** How to Build Million-Dollar AI Agents
**Relevance:** Foundational knowledge for agent design and architecture decisions

---

## Key Characteristics of Agentic AI

1. **Self-Reflection**
2. **Tool Access**
3. **Advanced Reasoning**
4. **Multi-Agent Collaboration**
5. **Automation**

---

## How Agentic AI Works (Perplexity Example)

1. Query
2. LLM creates plan
3. LLM takes actions using external tools
4. LLM processes and double-checks results
5. LLM translates results into output for user

---

## Examples of Agentic AI with Computer Browser Use

- **Anthropic Computer Use**
- **Manus**
- **OpenAI Agent Mode**

These systems use computer browsers live to interact with web interfaces and applications.

---

## Multi-Agent Collaboration Platforms

- **n8n**
- **Make.com**
- **OpenAI AgentKit**
- **Microsoft Power Automate**
- **Dify**

---

## 3 Fundamental Components of AI Agents (First Principles)

**Analogy:**
- Intelligence = Brain
- Orchestration = Spinal cord
- Capabilities = Muscular and skeletal structure

**Key Insight:** Foundational models take care of intelligence and orchestration. Capabilities is where we are "building".

### #1 Intelligence
Base model providing the ability to reason, think, and process information.

**Base models:**
- OpenAI
- Claude
- Deepseek

**Model types:**
- Reasoning
- GPT
- Audio (TTS and STT)
- Video
- Embedding models

**Note:** Without the other two parts, intelligence is just like a brain in a jar.

### #2 Orchestration
Central control plane mechanism that manages and coordinates interactions between AI agents and tools.

**Types:**
- Coding
- No-code

### #3 Capabilities
Everything from memory to action capabilities for taking actions in the real world.

**Includes:**
- Memory
- Function calling
- MCPs (Model Context Protocol)
- A2A (Agent-to-Agent communication)

---

## Agentic AI Runtime Stack (Technology Landscape)

### Intelligence Layer (Bottom - Foundation)
LLM/inference layer providing raw AI reasoning power.

**Model providers:**
- OpenAI
- Meta LLaMA
- DeepSeek
- etc.

### Orchestration Layer (Middle - Coordination Engine)
Manages how AI agents execute complex workflows.

**Agent Frameworks:**
- LangChain
- LlamaIndex
- CrewAI
- Agno

**Durable Execution:**
- Temporal
- AKKA
- DBOS
- Inngest

(Ensures reliable, fault-tolerant execution of long-running agent tasks - crucial for production systems)

### Capabilities Layer (Top - Action & Context)
Where agents interact with the real world and maintain state.

**MCP or UTCP** (central protocol layer)
- Model Context Protocol / Universal Tool Calling Protocol
- Critical interface standard between capabilities and orchestration

**Components:**
- **Knowledge:** Pinecone, Danswer (RAG/retrieval)
- **Memory:** Zep, Mem0 (persistent agent memory across sessions)
- **UI Automation:** Browser Use, OpenAI Operator (web interaction)
- **Sandboxes:** E2B (safe code execution)
- **Integrations:** Composio
- **App-specific tools:** Stripe, Blender, etc.
- **Orchestration platforms:** Dify, Letta, Agno (span multiple capability areas)
- **Actuators** and **Context** (periphery)

**Key Insight:** Modern AI agents require a full stack of infrastructure, not just the LLM. The orchestration layer is where real complexity and differentiation happens in production systems. MCP/UTCP is becoming a standardization point in the ecosystem.

---

## Pre-Planning Principles for AI Agent Development

**Core Message:** Start with clarity, not code. "Measure twice, cut once" philosophy.

**Key Analogy:** AI agents are analogous to probabilistic computers, whereas we have only learned how to use deterministic computers.

### #1 Clear Objective - Define the End State
AI agents need a **clearly stated end objective**, not just vague capabilities.

**Warning:** "It's not a magic wand (at least yet, which can do everything)"

**Example:** Move from "I want an AI assistant" to "I want an agent that schedules meetings based on email requests"

### #2 Define Success - Make It Measurable
Build concrete success criteria that can be consistently measured.

**Requirements:**
- Metrics must be objective and clear
- Prevents scope creep and endless iteration
- Success needs to be very distinctly defined

**Critical:** Agents don't inherently understand subtext and context.

**Examples:** Response time? Accuracy rate? Task completion percentage?

### #3 Have All Steps - Map the Complete Process
Understand every step required to achieve the objective and document the resources needed at each stage.

**Key Point:** Agents can't magically figure out your workflow - you need to explicitly map it out.

**Deeper Implication:** AI agents automate processes, they don't create them. You need to understand your process deeply enough to articulate it clearly before you can delegate it to an AI agent.

---

## Implementation Principles: Prompt Engineering is Agent Engineering

**Core Message:** Moving from planning to execution. These are essential success factors, not optional.

### #1 Context Matters - Set the Stage

**System instructions:** Define what the LLM is trying to emulate to its best capability to be.

**Key:** "Think of it as the persona of the person(s) who do this task"

You're not just programming logic, you're creating a role. The agent needs to understand not just *what* to do but *how* to think about the problem - the mood, tone, and what details are relevant.

**Warning:** Without this framing, the LLM will hallucinate its own context, often incorrectly.

### #2 Include Examples - Show, Don't Just Tell

**Guide it:** Even powerful LLMs need concrete examples showing the right format, tone, and level of detail for responses.

**Critical observation:** "AI is born people please" - LLMs are trained to be helpful and agreeable, which means they'll try to fulfill requests even when they shouldn't.

**Impact:** Showing examples of *when to say no* or *when to ask for clarification* can reduce hallucinations to near zero.

**Technique:** Few-shot prompting as a core engineering practice. Examples define the boundaries of acceptable behavior.

**Temperature setting:** Whenever you want to reduce hallucination, reduce temperature to 0.

### #3 Evals and RL (Reinforcement Learning) - Iterate Toward Excellence

**Reality:** "Going from 80% to 95% requires you to test and retest, and do something in the form of reinforcement training."

Prompt engineering alone gets you to "pretty good" but production-grade agents need systematic improvement.

**Reinforcement Learning reframed:** "Think of RL as including examples on steroids, where you are forcing it to converge to the kind of behaviour you want for different states."

Reinforcement Learning = scaled, automated example-giving across the full state space of possible agent situations.

**Key:** You can't anticipate every edge case manually, so you need a feedback loop that teaches the agent correct behavior across the distribution of real-world scenarios.

---

## Meta-Insight: Building Reliable AI Agents is More Like Teaching Than Programming

The progression:
1. **Context** - Give it identity and context (like training a new employee)
2. **Examples** - Show it good and bad behavior (like mentoring)
3. **RL** - Continuously improve through feedback (like performance reviews)

This represents increasing levels of sophistication in agent behavior shaping.

---

## References & Resources

**Presenter:** Divyanshu, Vipul
**Email:** vdivyanshu@mba2026.hbs.edu

**GitHub Repository (Workshop Materials):**
https://github.com/vipuldivyanshu92/agent-workshop
- Contains agent implementations: accounts-payable-agent, simple-weather-agent
- Python-based workshop for building AI agents

**Substack (21 AI Agent Guides - Q3 2025):**
https://vipuldivyanshu.substack.com/p/21-ai-agent-guides-q3-2025?utm_campaign=post&showWelcomeOnShare=true

**Agentic AI Survey:**
https://form.typeform.com/to/KtlJRf6r
